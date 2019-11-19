import io

try:
    import pandas as pd
except Exception:
    pass
from multiprocessing import Pool
from backend.repositories import SensorRepository


class CsvDataService:
    def _create_records_dict(
        row, user_id, app_key, net_key, device_id, units, created_at
    ):
        return [
            {
                "user_id": user_id,
                "app_key": app_key,
                "net_key": net_key,
                "device_id": device_id,
                "field_name": field_name,
                "value": value,
                "unit_string": units[field_name],
                "created_at": created_at,
            }
            for field_name, value in row.items()
            if field_name not in ["TIMESTAMP", "RECORD"]
        ]

    def insert_many_from_http(self, csv_file, user_id):
        csv_file = io.StringIO(csv_file.decode())
        data = pd.read_csv(csv_file, delimiter=",", quotechar='"')
        rows = data.to_dict("records")
        units = rows[0]
        tuples = []
        for row in rows[2:]:
            tuples += self._create_records_dict(
                row,
                user_id,
                "from_csv",
                "from_csv",
                "from_csv",
                units,
                row["TIMESTAMP"],
            )

        list_size = len(tuples)
        chunks = list_size // 4
        chunk1 = tuples[0:chunks]
        chunk2 = tuples[chunks : chunks * 2]
        chunk3 = tuples[chunks * 2 : chunks * 3]
        chunk4 = tuples[chunks * 3 : list_size]

        with Pool(5) as p:
            p.map(
                SensorRepository().insert_many_from_csv,
                [chunk1, chunk2, chunk3, chunk4],
            )
        return len(tuples)
