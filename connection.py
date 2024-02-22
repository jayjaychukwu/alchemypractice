import sqlalchemy as db

engine = db.create_engine("sqlite:///european_database.sqlite")

conn = engine.connect()

metadata = db.MetaData()

division = db.Table(
    "divisions",
    metadata,
    autoload=True,
    autoload_with=engine,
)


if __name__ == "__main__":
    print(repr(metadata.tables["divisions"]))
    print(division.columns.keys())
