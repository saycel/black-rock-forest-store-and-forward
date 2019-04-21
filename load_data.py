import os

from sqlalchemyseeder.resolving_seeder import ResolvingSeeder

from app.database import db_session

sd = ResolvingSeeder(db_session)
dirname = os.path.dirname(__file__)

new_entity = sd.load_entities_from_json_file( os.path.join(dirname, "seed_data.json"))

db_session.commit()
