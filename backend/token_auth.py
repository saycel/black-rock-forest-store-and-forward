from _datetime import datetime, timedelta
from dateutil.parser import parse as date_parse
import jwt
from flask import current_app

from backend.database import db_session
from backend.models import User
from backend.repositories import UserRepository


def check(_request):

    if not _request.headers.get('Authorization'):
        return {'message': 'Make sure you have Token  in the headers.'}, 400
    try:
        token = jwt.decode(_request.headers.get('Authorization').encode(),
                             current_app.config['SECRET_KEY'],
                             algorithms=['HS256'])
    except Exception as e:
        current_app.logger.debug(str(e))
        return {'message': 'invalid token'}, 400

    if not isinstance(token, dict):
        return {'message': 'invalid token'}, 400

    token_date = date_parse (token['valid_until'])

    if token_date < datetime.now():
        return {'message': 'deprecated token'}


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
