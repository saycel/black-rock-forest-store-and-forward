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

    def set_collected_to_true(self):
        all_lectures = self.get_latest_sensor_data()

        for lecture in all_lectures:
            lecture.is_collected = "1"
            db_session.add(lecture)

        db_session.commit()
