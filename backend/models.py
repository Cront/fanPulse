from config import db
from config import bcrypt


class UserAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    taps = db.relationship("Tap", backref="user", lazy=True)

    def set_password(self, raw_pw):
        self.password = bcrypt.generate_password_hash(raw_pw).decode("utf-8")

    def check_password(self, raw_pw):
        return bcrypt.check_password_hash(self.password, raw_pw)

    def to_json(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "team": self.team,
            "email": self.email,
            "bubbles": self.num_of_taps,
        }

class Taps(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.String(80), db.ForeignKey("user_account.id"), unique=False, nullable=False
    )
    team_id = db.Column(db.String(80), unique=False, nullable=False)
    timestamp = db.Column(
        db.DateTime, default=db.func.now(), unique=False, nullable=False
    )

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "team_id": self.team_id,
            "timestamp": self.timestamp,
        }
