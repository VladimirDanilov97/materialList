from sqlalchemy import Table, MetaData, Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker

metadata = MetaData()

engine = create_engine(f"sqlite:///material_list.db")

products = Table('products', metadata,
                Column('product_id', Integer, primary_key=True),
                Column('product_name', String, ),
                )

sheet = Table('sheets', metadata,
               Column('sheet_id', Integer, primary_key=True),
               Column('width', Integer),
               Column('length', Integer),
               Column('thickness', Integer),
               Column('material', String),
               Column('amount', Integer),
               )

tube = Table('tubes', metadata,
               Column('sheet_id', Integer, primary_key=True),
               Column('diameter', Integer),
               Column('thickness', Integer),
               Column('length', Integer),
               Column('material', String),
               Column('amount', Integer),
               )

nuckle = Table('nuckles', metadata,    
               Column('nuckle_id', Integer, primary_key=True),
               Column('diameter', Integer), 
               Column('material', String),
               )

bolt = Table('bolts', metadata,    
               Column('bolt_id', Integer, primary_key=True),
               Column('diameter', Integer), 
               Column('length', Integer), 
               Column('material', String),
               )

flange = Table('flange', metadata,    
               Column('flange_id', Integer, primary_key=True),
               Column('diameter', Integer), 
               Column('pressure', Integer),
               Column('inner diameter', Integer),
               Column('pressure', Integer),
               Column('material', String),
               )


if __name__ == '__main__':
    metadata.drop_all(engine)
    metadata.create_all(engine)
    stmt = products.insert().values(product_name='foo')
    with engine.connect() as conn:
        conn.execute(stmt)
       
   
