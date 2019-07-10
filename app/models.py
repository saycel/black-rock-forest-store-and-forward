from datetime import datetime

from app.database import Base
from sqlalchemy import Column, String, DateTime, BigInteger


class Sensor(Base):
    __tablename__ = "sensor"
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    device_id = Column(String, primary_key=True)
    mac_addr = Column(String)
    type = Column(String)
    location = Column(String)
    description = Column(String)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, device_id, mac_addr, type, location, description=''):
        self.device_id = device_id
        self.mac_addr = mac_addr
        self.type = type
        self.location = location
        self.description = description

    @property
    def serialize(self):
        return dict(device_id=self.device_id,
                    mac_addr=self.mac_addr,
                    type=self.type,
                    location=self.location,
                    description=self.description,
                    created_at=self.created_at)

    def __repr__(self):
        return f'<Sensor id:{self.device_id}, type:{self.net_key}>'


class SensorData(Base):
    __tablename__ = 'sensordata'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    app_key = Column(String)
    net_key = Column(String)
    device_id = Column(String)
    channel = Column(String)
    value = Column(BigInteger)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, app_key, net_key, device_id, channel, value):
        self.app_key = app_key
        self.net_key = net_key
        self.device_id = device_id
        self.channels = channel
        self.value = value


    def __repr__(self):
        return f'<SensorData id:{self.id}, device_id:{self.device_id}, net_key:{self.net_key}>'

    def decode(self, payload):
        pass

    @property
    def serialize(self):
        return dict(device_id=self.device_id,
                    app_key=self.app_key,
                    net_key=self.net_key,
                    channel=self.channel,
                    value=self.value,
                    created_at=self.created_at)


class SensorDebug(Base):
    __tablename__ = "debug"
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    device_id = Column(String)
    code = Column(String)
    message = Column(String)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, device_id, code, message):
        self.device_id = device_id
        self.code = code
        self.message = message

    def __repr__(self):
        return f'<SensorDebug id:{self.id}, device_id:{self.device_id}, code:{self.code}, message:{self.message}, created_at:{self.created_at}>'

    @property
    def serialize(self):
        return dict(device_id=self.device_id,
                    code=self.code,
                    message=self.message,
                    created_at=self.created_at)


class DebugCode(Base):
    __tablename__ = "debugcode"
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    code = Column(String)
    description=Column(String)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, code, description):
        self.code = code
        self.description = description

    @property
    def serialize(self):
        return dict(code=self.code,
                    description=self.description,
                    created_at=self.created_at)

    def __repr__(self):
        return f'<SensorDebug id:{id}, code:{self.code}, description:{self.description}>'
