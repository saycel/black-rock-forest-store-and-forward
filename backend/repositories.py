from backend.database import db_session
from backend.models import SensorData, User


class SensorRepository(object):

    def get_sensor_data(self, user_id, page_size=20, page=1):
        offset = page_size * page-1
        data = db_session.query(SensorData).filter(SensorData.user_id == user_id)
        return data.count(), data.limit(page_size).offset(offset).all()

    def insert_one(self, record):
        try:
            db_session.add(record)
            db_session.commit()
        except Exception:
            db_session.rollback()
            raise

    def insert_many(self, records):
        try:
            db_session.bulk_save_objects(records)
            db_session.commit()
        except Exception:
            db_session.rollback()
            raise

    def insert_many_from_csv(self, records):
        try:
            db_session.bulk_insert_mappings(SensorData, records)
            db_session.commit()
        except Exception:
            db_session.rollback()
            raise


class UserRepository(object):
    def insert(self, email, password):
        user = User.query.filter(User.email == email)
        if user.count():
            return {"message": "email or passowrd incorrect"}, 400
        try:
            user = User()
            user.password = password.encode()
            user.email = email
            db_session.add(user)
            db_session.commit()
        except ValueError as e:
            db_session.rollback()
            return {"message": f"{str(e)}"}, 400

        return {"message": f"user with email {email} successfully created"}, 200

    def get_by(self, email, as_dict=True):
        user = User.query.filter(User.email == email)
        if not user.count():
            return {"message": "email or passowrd incorrect"}, 400

        return user.first().to_dict() if as_dict else user.first()
