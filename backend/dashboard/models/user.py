# Epic Title: Customizable Widgets

from .widget import Widget

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=True)
    mfa_enabled = Column(Boolean, default=False)

    accounts = relationship('Account', back_populates='user')
    profile = relationship('UserProfile', uselist=False, back_populates='user')
    widgets = relationship('Widget', back_populates='user')

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f"<User(username='{self.username}', is_active='{self.is_active}', mfa_enabled='{self.mfa_enabled}')>"



# File 3: Widget Controller in dashboard/controllers/widget_controller.py