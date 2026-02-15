# Epic Title: Role-Based Access Control

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserRole(db.Model):
    __tablename__ = 'user_roles'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)
    
    def save(self):
        # Epic Title: Role-Based Access Control
        db.session.add(self)
        db.session.commit()