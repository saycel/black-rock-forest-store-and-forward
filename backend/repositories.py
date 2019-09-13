from backend.database import db_session
from backend.models import SensorData, User


class SensorRepository:
    def get_latest_sensor_data(self):
        data = (
            db_session
            .query(SensorData)
            .filter(SensorData.is_collected == "0")
            .all()
        )
        return data

    def get_all_sensor_data(self):
        data = (
            db_session
            .query(SensorData)
            .all()
        )
        return data

    def insert_one(self, record):
        db_session.add(record)
        db_session.commit()

    def insert_many(self, records):
        db_session.bulk_insert_mappings(SensorData, records)
        db_session.commit()


class UserRepository:

    def insert(self, email, password):
        user = User.query.filter(User.email == email)
        if user.count():
            return {'message': f'given email {email} already in use'}, 400
        try:
            user = User()
            user.password = password.encode()
            user.email = email
            db_session.add(user)
            db_session.commit()
        except ValueError as e:
            return {'message': f'{str(e)}'}, 400

        return {'message': f'user with email {email} successfully created'}, 200

    def get_by(self, email, as_dict=True):
        user = User.query.filter(User.email == email)
        if not user.count():
            return {'message': f'given email {email} is not related to any user'}, 400

        return user.first().to_dict() if as_dict else user.first()
