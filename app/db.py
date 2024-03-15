
from sqlalchemy import String, create_engine, text, Connection, MetaData, Table, Column, Integer
from sqlalchemy.orm import Session
import os
    
class Db_start:
    def __init__(self, args):
        
        db_path = 'sqlite:///database.db'

        # print(args)
        #"sqlite+pysqlite:///memory:"
        metadata = MetaData()
        
        engine = create_engine(db_path, echo=True)

        with engine.connect() as connection:
            
            result = connection.execute(text("select 'hello, world'"))
            # print(result.all())
            # print(result.scalar())
            st = self.cr_u_table()
            metadata.create_all(engine)
	

    def cr_u_table(self):
        metadata = MetaData()
        user_table = Table(
            "users",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("fullname", String)
            
        )
        
    def mainfile(self, file:str, dir:str):
        
        dir_file = os.path.join(os.path.dirname(__file__), dir)
        f = os.path.join(dir_file, file)
        return f