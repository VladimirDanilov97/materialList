from sqlalchemy import Table, MetaData, Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
metadata = MetaData()

engine = create_engine(f"sqlite:///material_list.db")

class Product(Base):
    __tablename__ = 'products'
    id = Column('id', Integer, primary_key=True)
    name = Column('product_name', String, )
    part_of = Column('part_of', ForeignKey('products.id'), nullable=True)

    def __init__(self, id, name, part_of=id) -> None:
        self.id = id
        self.name = name,
        self.part_of = part_of
    
    def __repr__(self):
        return f'{self.name}'

# products = Table('products', metadata,
#                 Column('product_id', Integer, primary_key=True),
#                 Column('product_name', String, ),
#                 Column('part_of', ForeignKey('products.product_id')))

# sheet = Table('sheet', metadata,
#                Column('sheet_id', Integer, primary_key=True),
#                Column('width', Integer),
#                Column('length', Integer),
#                Column('thickness', Integer),
#                Column('material', String),
#                Column('amount', Integer),
#                Column('product', ForeignKey('products.product_id')))



if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    p = Product(id=1, name='manhole')
    session.add(p)

    session.commit()