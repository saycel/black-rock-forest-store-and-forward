from app.database import db_session
from app.models import SensorData


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
        db_session.bulk_save_objects(records)
        db_session.commit()
