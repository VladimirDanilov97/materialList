from sqlalchemy import Table, MetaData, Column, String, Integer, ForeignKey, create_engine

metadata = MetaData()

engine = create_engine(f"sqlite:///material_list.db")

products = Table('products', metadata,
                Column('product_id', Integer, primary_key=True),
                Column('product_name', String, ),
                Column('part_of', ForeignKey('products.product_id')))

sheet = Table('sheet', metadata,
               Column('sheet_id', Integer, primary_key=True),
               Column('width', Integer),
               Column('length', Integer),
               Column('thickness', Integer),
               Column('material', String),
               Column('amount', Integer),
               Column('product', ForeignKey('products.product_id')))



if __name__ == '__main__':
    metadata.drop_all(engine)
    metadata.create_all(engine)