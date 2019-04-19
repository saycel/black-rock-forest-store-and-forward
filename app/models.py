from app.database import Base
from sqlalchemy import Column, Integer, JSON, String


class SensorData(Base):
    __tablename__ = 'sensordata'
    id = Column(Integer, autoincrement='auto', primary_key=True)
    app_key = Column(String)
    net_key = Column(String)
    device_id = Column(String)
    channels = Column(JSON())

    def __init__(self, app_key, net_key, device_id, channels):
        self.app_key = app_key
        self.net_key = net_key
        self.device_id = device_id
        self.channels = channels

    def __repr__(self):
        return f'<Sensor device_id:{self.device_id}, net_key:{self.net_key}>'

    def decode(self, payload):
        pass

    @property
    def serialize(self):
        return dict(device_id=self.device_id,
                    app_key=self.app_key,
                    net_key=self.net_key,
                    channels=self.channels
                    )
