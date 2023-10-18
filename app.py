from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    redirect,
    url_for,
    flash,
    session,
)


from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from functools import wraps
from flask_wtf import FlaskForm
from wtforms.validators import EqualTo
from itsdangerous import URLSafeTimedSerializer
import  os
from flask_security import current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo
from uuid import UUID
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_manager,
    current_user,
)
from werkzeug.utils import redirect
from datetime import date

class CustomRegisterForm(FlaskForm):
    email = StringField("Email", [DataRequired(), Email()])
    password = PasswordField("Password", [DataRequired()])
    password_confirm = PasswordField(
        "Confirm Password",
        [DataRequired(), EqualTo("password", message="Passwords must match")],
    )
    name = StringField("Name", [DataRequired()])
    surname = StringField("Surname", [DataRequired()])
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is already in use. Please choose a different one.')


class CustomLoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])

    def validate(self, *args, **kwargs):
        if not super(CustomLoginForm, self).validate():
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()

        # Check if user is not None before accessing its attributes
        if user is None:
            self.email.errors.append("Does not exist ! Create an account first !")
            return False

        print(f"User email: {user.email}")
        print(f"User active status: {user.active}")

        password_check_result = check_password_hash(user.password, self.password.data)
        print(f"Password check result: {password_check_result}")

        if not user.active:
            self.email.errors.append("Have not been confirmed yet, Please confirm your email!")
            return False

        if not password_check_result:
            self.email.errors.append("Invalid email and/or password")
            return False

        return True
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Old Password", validators=[DataRequired()])
    new_password = PasswordField("New Password", [DataRequired(), EqualTo("confirm_new_password", message="Passwords must match")])
    confirm_new_password = PasswordField("Confirm New Password", validators=[DataRequired()])
class PasswordResetForm(FlaskForm):
    new_password = PasswordField("New Password", [DataRequired(), EqualTo("confirm_new_password", message="Passwords must match")])
    confirm_new_password = PasswordField("Confirm New Password", validators=[DataRequired()])
class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
app = Flask(__name__)
from models import db, User, Role, init_app
csrf = CSRFProtect(app)
CORS(app)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "SQLALCHEMY_DATABASE_URI", "sqlite:///mydatabase.db"
)
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER")
app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT", "587"))
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_DEBUG"] = True
app.config["MAIL_SUPPRESS_SEND"] = False
app.config["MAIL_ASCII_ATTACHMENTS"] = False
app.config["SECURITY_PASSWORD_SALT"] = os.getenv("SECURITY_PASSWORD_SALT")
today = date.today().strftime("%Y-%m-%d")

mail = Mail(app)
login_manager = LoginManager()
login_manager.init_app(app)


db.init_app(app)
def custom_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to continue")
            return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function

def generate_confirmation_token(email):#good
    serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    return serializer.dumps(email, salt=app.config["SECURITY_PASSWORD_SALT"])


def confirm_token(token, expiration=3600):#good
    serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    try:
        email = serializer.loads(
            token, salt=app.config["SECURITY_PASSWORD_SALT"], max_age=expiration
        )
    except:
        return False
    return email


def send_confirmation_email(user_email):
    token = generate_confirmation_token(user_email)
    verification_url = url_for(
        "confirm_email", token=token, _external=True
    )  
    html = render_template(
        "emailverification.html", verification_url=verification_url
    )  
    msg = Message(
        "Please confirm your email",
        sender=app.config["MAIL_USERNAME"],
        recipients=[user_email],
        html=html,
    )
    mail.send(msg)



@login_manager.user_loader
def load_user(user_id):
    try:
        uuid_obj = UUID(user_id)  
        return User.query.filter(User.fs_uniquifier == uuid_obj).first()
    except ValueError:
        return None
    
def send_reset_email(email, reset_url):
    html = render_template('reset_password_email.html', reset_url=reset_url)
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[email], html=html)
    mail.send(msg)

@app.route('/reset_token/<token>', methods=['GET', 'POST'])
def reset_token(token):
    # Check the token, and redirect to login if it's invalid
    email = confirm_token(token)
    if not email:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('login'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first()
        if user:
            user.password = generate_password_hash(form.new_password.data)
            db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    else:
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                flash(f'{fieldName}: {err}') 
    return render_template('reset_token.html', form=form ,token=token)

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user:
            token = generate_confirmation_token(user.email)
            reset_url = url_for('reset_token', token=token, _external=True)
            send_reset_email(user.email, reset_url)
            flash('A password reset email has been sent to your mail.', 'info')
            return redirect(url_for('login'))
        else:
            flash('The email address does not exist. Please provide a correct email address', 'error')
            return redirect(url_for('reset_password'))
    return render_template('reset_password.html', form=form)




@app.route('/change_password', methods=['GET', 'POST'])
@custom_login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=session['user_id']).first()  # get user from DB
        if not user or not check_password_hash(user.password, form.old_password.data):
            flash('Incorrect current password')
        else:
            user.password = generate_password_hash(form.new_password.data)
            db.session.commit()
            flash('Your password has been updated.')
            return redirect(url_for('login'))
    return render_template('change_password.html', form=form)

@app.route("/register", methods=["GET", "POST"])#good
def register():
    form = CustomRegisterForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            password=generate_password_hash(form.password.data),
            name=form.name.data,
            surname=form.surname.data,
            active=False,  # user is not active until confirmation
        )
        db.session.add(user)
        db.session.commit()
        try:
            send_confirmation_email(user.email)  # send confirmation email
        except Exception as e:
            flash(f"Either the email or pass for flask SMTP GMAIL setup is failing ... the error : {str(e)}")
            db.session.rollback()  # if there is a problem with sending email - rollback db changes
            return render_template("register.html", register_form=form)
        return redirect(url_for("registration_successful"))
    else:
        print("Form validation failed")
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"This {field} {error}")
    return render_template("register.html", register_form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))#redirect index if sucessfuly authenticated
    form = CustomLoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print("Form validation passed")
            user = User.query.filter_by(email=form.email.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                session["user_id"] = user.id
                session["user_name"] = user.name
                session["user_surname"] = user.surname
                session["user_email"] = user.email
                
                next_page = (
                    request.form["next"]
                    or request.args.get("next")
                    or url_for("login")#redirect to login after creating account
                )
                return redirect(next_page)
        else:
            print("Form validation failed")
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"This {field}  {error}")                
    return render_template("login.html", form=form)



@app.route("/confirm/<token>", methods=["GET", "POST"])#good
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash("Confirmation link is invalid or has expired.", "danger")
        return redirect(url_for("login"))
    user = User.query.filter_by(email=email).first_or_404()
    if user.active:
        flash("Account already confirmed. Please log in.", "success")
    else:
        user.active = True
        db.session.add(user)
        db.session.commit()
        flash("Thank you for confirming your email!", "success")
    return redirect(url_for("index"))


@app.route("/registration_successful")#good
def registration_successful():
    return render_template("registration_successful.html")



@app.context_processor
def inject_user():
    return dict(current_user=current_user)


@app.route('/', methods=['GET', 'POST'])
@custom_login_required
def index():
    return render_template('index.html')




@app.errorhandler(400)
def handle_bad_request(e):
    return jsonify({'message': str(e), 'success': False}), 400



@app.route("/logout")
@custom_login_required#use this line wherever you want user to log iin to continue
def logout():
    session.pop("user_id", None)
    session.pop("user_name", None)
    session.pop("user_surname", None)
    session.pop("user_email", None)
    
    logout_user()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)