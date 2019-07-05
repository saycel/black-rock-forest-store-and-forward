import datetime

from app.database import Base
from sqlalchemy import Column, Integer, JSON, String, Boolean, DateTime, BigInteger


class SensorData(Base):
    __tablename__ = 'sensordata'
    id = Column(BigInteger, autoincrement='auto', primary_key=True)
    app_key = Column(String)
    net_key = Column(String)
    device_id = Column(String)
    channel = Column(String)
    value = Column(BigInteger)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, app_key, net_key, device_id, channel, value):
        self.app_key = app_key
        self.net_key = net_key
        self.device_id = device_id
        self.channels = channel
        self.value =  value


    def __repr__(self):
        return f'<SensorData device_id:{self.device_id}, net_key:{self.net_key}>'

    def decode(self, payload):
        pass

    @property
    def serialize(self):
        return dict(device_id=self.device_id,
                    app_key=self.app_key,
                    net_key=self.net_key,
                    channel=self.channel,
                    value=self.value,
                    created_at=self.created_at
                    )


class SensorDebug(Base):
    __tablename__ = "debug"
    id = Column(Integer, autoincrement='auto', primary_key=True)
    device_id = Column(String)
    code = Column(Integer)
    message = Column(String)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, device_id, code, message):
        self.device_id = device_id
        self.code = code
        self.message = message

    def __repr__(self):
        return f'<SensorDebug device_id:{self.device_id}, code:{self.code}, message:{self.message}, created_at:{self.created_at}>'

    @property
    def serialize(self):
        return dict(device_id=self.device_id,
                    code=self.code,
                    message=self.message,
                    created_at=self.created_at
                    )
