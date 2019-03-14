from app.database import Base
from sqlalchemy import Column, Integer, String


class SensorData(Base):
    __tablename__ = 'SensorData'
    id = Column(Integer, autoincrement='auto', primary_key=True)
    sensor_id = Column(Integer)
    value = Column(Integer)
    unit = Column(String(3))

    def __init__(self, sensor_id, value, unit):
        self.sensor_id = sensor_id
        self.value = value
        self.unit = unit

    def __repr__(self):
        return f'<Sensor {self.sensor_id}>'
