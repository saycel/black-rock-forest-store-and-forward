import datetime
from unittest import TestCase
from unittest.mock import patch

from app.models import SensorData


class testSensorData(TestCase):
    def test_constructor(self):
        sensData = SensorData('12','11','10','fieldName',12,'c')

        assert '12' == sensData.app_key
        assert '11' == sensData.net_key
        assert '10' == sensData.device_id
        assert 'fieldName' == sensData.field_name
        assert 12 == sensData.value
        assert 'c' == sensData.unit_string


    def test_repr(self):
        sensData = SensorData('12', '11', '10', 'fieldName', 12, 'c')
        assert '<SensorData id:None, device_id:10, net_key:11>' == sensData.__str__()

    @patch('app.models.datetime')
    def test_serialize(self, mock_datetime):
        mock_datetime.utcnow.return_value =  datetime.datetime(2019, 8, 12, 23, 42, 20, 990864)
        sensData = SensorData('12', '11', '10', 'fieldName', 12, 'c')
        serialized = sensData.serialize

        assert isinstance(serialized, dict)
        assert '12' == serialized['app_key']
        assert '11' == serialized['net_key']
        assert '10' == serialized['device_id']
        assert 'fieldName' == serialized['field_name']
        assert 12 == serialized['value']
        assert 'c' == serialized['unit']
        assert None == serialized['created_at']
