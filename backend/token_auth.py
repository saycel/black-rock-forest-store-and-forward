from _datetime import datetime, timedelta

import jwt
from flask import current_app

from backend.database import db_session
from backend.models import User
from backend.repositories import UserRepository


def check(_request):

    if not _request.authorization:
        return {'message': 'Make sure you have Token  in the headers.'}, 400

    if jwt.decode(_request.authorization.encode(), current_app.config['SECRET_KEY'], algorithms=['HS256']):
        return {'message': 'Wrong Token.'}, 403


def generate(email, password):
    user = UserRepository().get_by(email, as_dict=False)

    if not isinstance(user, User):
        return user

    if not user.valid_password(password):
        return {'message': 'invalid password'}, 403

    valid_until = str(datetime.now() + timedelta(days=180))
    user.auth_token = {'email': email, 'valid_until': valid_until}

    db_session.add(user)
    db_session.commit()

    return {'token': user.auth_token.decode()}
