from config import db 
from config import bcrypt

class UserAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    num_of_taps = db.Column(db.Integer, unique=False, default=0)

    def set_password(self, raw_pw):
        self.password = bcrypt.generate_password_hash(raw_pw).decode('utf-8')

    def check_password(self, raw_pw):
        return bcrypt.check_password_hash(self.password, raw_pw)

    def to_json(self):
        return {
            "id": self.id,
            "first_name": self.first_name, 
            "last_name": self.last_name,
            "email": self.email,
            "num_of_taps": self.num_of_taps
        }