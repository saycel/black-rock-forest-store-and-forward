from app.database import init_db, engine

table = engine.dialect.has_table(engine, 'SensorData')
if not table:
    print('initializing database')
    init_db()
else:
    print('db already exist,in case you want a fresh install drop db before run this script')