from sqlalchemy import String, create_engine, text, Connection, MetaData, Table, Column, Integer
from sqlalchemy.orm import Session
    
class Db_start:
    def __init__(self, *args):
        db_path = 'sqlite:///database.db'

        # print(args)
        #"sqlite+pysqlite:///memory:"

        engine = create_engine(db_path, echo=True)

        with engine.connect() as connection:
            result = connection.execute(text("select 'hello, world'"))
            # print(result.all())
            print(result.scalar())
	

    def cr_u_table():
        metadata = MetaData()
        user_table = Table(
            "users",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("fullname", String)
            
        )