<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>FlaskAuthFrame</h1>
<h3>◦ FlaskAuthFrame A perfect starting point for an app !</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style&logo=JavaScript&logoColor=black" alt="JavaScript" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style&logo=HTML5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
</p>

</div>

---

## 📖 Table of Contents

- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
  - [🔧 Installation](#-installation)
  - [🤖 Running FlaskAuthFrame.git](#-running-FlaskAuthFrame.git)

- [🤝 Contributing](#-contributing)
- [📄 License](#-license)


---

## 🎬 Demo

You can see a live demo of the application running at [FLASKAUTHFRAME](http://auth.pythonanywhere.com)

---

## 📍 Overview

The project is a Flask application designed to provide a comprehensive user authentication framework. It supports fundamental features like user registration, login, email verification, and password resetting, thereby enhancing the security aspect of web applications. The use of Python libraries such as Flask-SQLAlchemy, Flask-Mail and Flask-Login streamline the creation of such secure environments. The project presents a valuable foundation for developers working on platforms requiring trustworthy user authentication and can expedite the initial development process significantly.

---

## 📦 Features

|     | Feature          | Description                                                                                                                                          |
| --- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| ⚙️  | **Architecture** | Implements the Model-View-Controller (MVC) architectural pattern. Uses Flask as the web framework for Python-based backend.                          |
| 🔗  | **Dependencies** | Main dependencies include Flask, SQL Alchemy, and WTForms for form handling. Secured on HTTPS with Flask-Talisman.                                   |
| 🧩  | **Modularity**   | Separate modules for routes, models, and forms to increase maintainability.                                                                          |
| ⚡️ | **Performance**  | Efficient use of Flask and minimalistic design strategies for increased speed.                                                                       |
| 🔐  | **Security**     | Uses WTForms for CSRF protection and Flask Login for user session management.                                                                        |
| 🔌  | **Integrations** | Integrated with SQL Alchemy for object-relational mapping                                                                                            |
| 📶  | **Scalability**  | The application’s scalable potential depends on the Flask application's capacity to handle increased traffic when deployed with gunicorn or similar. |

---

## 🚀 Pre-installation Setup

Before installing the application:

1. **Environment Variables:**

   - Fill in the necessary information at `.env.example` and Rename this file to `.env` after .

   - Use existing keys for tests or provide your own Keys for Producton. However, you must provide Gmail SMTP information.
   <p align="center"><img src=https://github.com/beephole/FlaskAuthFrame/assets/118709832/adc4ac8d-dd7b-448e-81b8-5873563d2ae6)alt="Here how password looks like !" width="350"/></p>

2. **Gmail SMTP Setup**:

   - You must generate a Gmail app password for your account:
     - Go to your Google Account.
     - Select Security.
     - Under "Signing in to Google," select App Passwords. You may need to sign in again.
     - Under "App Passwords", select the app dropdown and choose "Mail", and the device you want the app password to apply to and then select Generate.
     - Follow the instructions to enter the App Password. The App Password is the 16-character code in the yellow bar on your device.
     - For a detailed walkthrough, watch this [Tutorial](https://www.youtube.com/watch?v=J4CtP1MBtOE). Img how pass looks like , below ⬇️

   <p align="center"><img src="https://github.com/beephole/FlaskAuthFrame/assets/118709832/1b63f1d4-64e1-4f52-83e5-52d2f2f2307d" alt="Here how password looks like !" width="200"/></p>

### 🔧 Installation

1. Clone the FlaskAuthFrame.git repository:

```
git clone https://github.com/beephole/FlaskAuthFrame.git
```

2. Change to the project directory:

```
cd FlaskAuthFrame
```

3. Create a virtual environment:

```
python -m venv env
```

4. Activate the virtual environment:

   - On Windows, run:

   ```
   .\env\Scripts\activate
   ```

   - On Unix or MacOS, run:

   ```
   source env/bin/activate
   ```

5. Install the dependencies:

```
pip install -r requirements.txt
```

6. Init Database:

```
python init.py
```

### 🤖 Running FlaskAuthFrame.git

To run the project, use the following command:

```
python app.py
```

Server will run at http://127.0.0.1:5000


https://github.com/beephole/FlaskAuthFrame/assets/118709832/bb34d375-7b47-4c90-ba59-9fe7430ab5d0

> For first time registering users Try it with 2 or 3 diff emails ,  gmail verificaiton email "

> note that you have to confim the links in gmail in browser if running locally , on phone you need to open a tunnel with ngrok for testing
## 📂 Repository Structure

```sh
└── FlaskAuthFrame.git/
    ├── .env.example
    ├── app.py
    ├── init.py
    ├── LICENSE
    ├── models.py
    ├── requirements.txt
    ├── static/
    │   ├── assets/
    │   ├── favicon.ico
    │   └── img/
    └── templates/
        ├── change_password.html
        ├── emailverification.html
        ├── error.html
        ├── index.html
        ├── login.html
        ├── register.html
        ├── registration_successful.html
        ├── reset_password.html
        ├── reset_password_email.html
        └── reset_token.html
```

---

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [app.py](https://github.com/beephole/FlaskAuthFrame.git/blob/main/app.py)                                                       | This Flask application allows user registration, login, and authentication for a web application. It includes email confirmation, password hashing for security, and password reset capabilities. It also provides CSRF protection and CORS policies. The app uses Flask-SQLAlchemy for database interactions, Flask-Mail for email services, and Flask-Login for handling user sessions. Login is required for certain routes. The code also handles errors and flashes messages for user feedback. |
| [models.py](https://github.com/beephole/FlaskAuthFrame.git/blob/main/models.py)                                                 | This code represents the database model structure in an application, using Flask-SQLAlchemy. It defines three primary models: Role, User, and UserRoles. The `Role` model has fields for ID, name, and description. The `User` model has fields for user-related data like name, username, email, password, login data, and associated roles. Lastly, `UserRoles` model captures the many-to-many relationships between users and roles.                                                             |
| [requirements.txt](https://github.com/beephole/FlaskAuthFrame.git/blob/main/requirements.txt)                                   | The code installs dependencies for a Flask web application. It features Flask for creating the application, Flask-WTF for forms, Werkzeug for utilities and services, Flask-Cors for handling Cross-Origin Resource Sharing, Flask-Security for authentication and authorization, pytz for timezone calculations, SQLAlchemy for SQL toolkit and ORM, and email-validator for email validation. It also uses python-dotenv to manage environment variables.                                          |
| [change_password.html](https://github.com/beephole/FlaskAuthFrame.git/blob/main/templates\change_password.html)                 | This is a templated HTML file for a web application's "Change Password" page. It includes Bootstrap and Font Awesome for styling and icons. It uses Jinja2 for statement and variable handling within HTML. Users can input their old and new passwords. If any error messages exist, they are flashed on screen. The page also features a dark mode toggle, a back button, and a floating image button.                                                                                             |
| [emailverification.html](https://github.com/beephole/FlaskAuthFrame.git/blob/main/templates\emailverification.html)             | This HTML file is an email template used for email verification. It generates a styled email which contains a welcome message, a confirmation token link, and a footer. The email features an adjustable'Verify' button that recipients can click to confirm their email addresses during signup. It also offers a manual link for copy-pasting in the browser if the button fails. Custom session data is used to personalize the email by addressing recipients by their provided names.           |
| [error.html](https://github.com/beephole/FlaskAuthFrame.git/blob/main/templates\error.html)                                     | The code generates an error page displayed when a user attempts to access an expired link. Key features include an SVG image, a message advising users to check for accidental input errors, a link redirecting them to the login page, and a looping JavaScript function for an alternating animation on the SVG images. Styling is used to format the appearance of page elements and animations.                                                                                                  |
| [index.html](https://github.com/beephole/FlaskAuthFrame.git/blob/main/templates\index.html)                                     | The code is a Jinja2 templated HTML for a login page. It's styled with CSS and uses Bootstrap for responsive design. The functionalities include the display of flashed messages, switching to dark mode, handling user login session, redirecting for logout and password change, and showing a user's Github and Twitter profiles. Additionally, it shows a donation modal on button hover. The alert and modal have visibility controlled via JavaScript.                                         |
| [login.html](https://github.com/beephole/FlaskAuthFrame.git/blob/main/templates\login.html)                                     | This code is for a webpage with a login form. Main functions include a form to take email and password, options to register a new account and reset password, and a switch for light/dark modes. It also shows alerts for any messages, and hides them after 5 seconds. The form posts data to the'login' url. Styling is dynamic with CSS transitions.                                                                                                                                              |
| [register.html](https://github.com/beephole/FlaskAuthFrame.git/blob/main/templates\register.html)                               | This HTML file sets up the registration page for a website. Users can fill out the form to register and create a new account. The form includes fields for first name, last name, email, password, and terms acceptance. The code also handles flash messages, an arrow-back option, a dark-mode toggle, and setup for a floating animation. Links for already-existing users to log in are included too. CSS and JS files are linked for styling and interactivity.                                 |
| [registration_successful.html](https://github.com/beephole/FlaskAuthFrame.git/blob/main/templates\registration_successful.html) | The code constructs a HTML template to notify users of successful registration. It imports aesthetic CSS styles from multiple external sources, implements button scaling animations, and displays a congratulations header. It also informs users that a verification email has been sent with further instructions and provides links to major email providers.                                                                                                                                    |
| [reset_password.html](https://github.com/beephole/FlaskAuthFrame.git/blob/main/templates\reset_password.html)                   | The HTML code specifies a web page template for a password reset form, including stylization and animations. Essential elements include flashing messages for user feedback, an email input field, and a submit button for requesting password reset instructions. It also embeds interactive'Go back' and'Dark mode' buttons, and links for registration and homepage navigation. Additionally, it temporarily shows alert messages and features a floating image frame.                            |
| [reset_password_email.html](https://github.com/beephole/FlaskAuthFrame.git/blob/main/templates\reset_password_email.html)       | This is an HTML template for a password reset email. It is styled with a minimalistic, centered layout. The email greets the recipient, provides a reset link (dynamically inserted with the'reset_url' variable), and assures that no changes will be made without the user's action. Lastly, it appreciates the user's attention.                                                                                                                                                                  |
| [reset_token.html](https://github.com/beephole/FlaskAuthFrame.git/blob/main/templates\reset_token.html)                         | The HTML file represents a web page built for resetting a user's password. It provides form fields to enter a new password and confirm it. It uses Bootstrap and FontAwesome for styling and includes custom CSS for elements like alerts and button animations. The page operates in both light and dark modes. User messages, like errors, are flashed and automatically hidden after 5 seconds.                                                                                                   |

</details>

---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:

1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).

```
git checkout -b new-feature-branch
```

4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.

```
git commit -m 'Implemented new feature.'
```

6. Push your changes to your forked repository on GitHub using the following command

```
git push origin new-feature-branch
```

7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
   The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `ℹ️  MIT` License. See the [LICENSE-MIT](LICENSE) file for additional info.

---

# Hi, I'm Beephole! 👋

### 🔗 Links

[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/b33ph0l3)

---
