from flask_security import UserMixin, RoleMixin
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime,Text
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)


class Role(db.Model, RoleMixin):
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    fs_uniquifier = Column(
        String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False
    )


    name = Column(String(255))
    surname = Column(String(255))
    username = Column(String(255), unique=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    active = Column(Boolean())  # Renamed attribute from 'is_active' to 'active'
    confirmed_at = Column(DateTime())
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(255))
    current_login_ip = Column(String(255))
    login_count = Column(Integer())
    roles = relationship("Role", secondary="user_roles")
    


    @property
    def is_active(self):
        return self.active if self.active is not None else True

    def __init__(self, *args, active=None, **kwargs):
        super().__init__(*args, **kwargs)
        if active is not None:
            self.active = active  # Updated to use 'active' instead of 'is_active'


class UserRoles(db.Model):
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("user.id", ondelete="CASCADE"))
    role_id = Column(Integer(), ForeignKey("role.id", ondelete="CASCADE"))

