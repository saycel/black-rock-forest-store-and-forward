from _datetime import datetime, timedelta
from functools import wraps

from dateutil.parser import parse as date_parse
import jwt
from flask import current_app, request, g

from backend.database import db_session
from backend.models import User
from backend.repositories import UserRepository


def check(_request):

    if not _request.headers.get("Authorization"):
        return {"message": "Make sure you have Token  in the headers."}, 400
    try:
        token = jwt.decode(
            _request.headers.get("Authorization").encode(),
            current_app.config["SECRET_KEY"],
            algorithms=["HS256"],
        )
    except Exception as e:
        current_app.logger.debug(str(e))
        return {"message": "invalid token"}, 400

    g.current_user = db_session.query(User).filter(User.email == token["email"]).first()

    if not g.current_user:
        return {"message": "user not found"}, 404

    if not isinstance(token, dict):
        return {"message": "invalid token"}, 400

    token_date = date_parse(token["valid_until"])

    if token_date < datetime.now():
        return {"message": "deprecated token"}, 400


def generate(email, password):
    user = UserRepository().get_by(email, as_dict=False)

    if not isinstance(user, User):
        return user

    if not user.valid_password(password):
        return {"message": "invalid password"}, 403

    valid_until = str(datetime.now() + timedelta(days=180))
    user.auth_token = {"email": email, "valid_until": valid_until}

    db_session.add(user)
    db_session.commit()

    return {"token": user.auth_token.decode()}


def auth_needed(f):
    """Decorator function. Check token."""

    @wraps(f)
    def wrap(*args, **kwargs):
        message = check(request)
        if message:
            return message
        return f(*args, **kwargs)

    return wrap
