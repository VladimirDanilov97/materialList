from sqlalchemy import Table, MetaData, Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
engine = create_engine(f"sqlite:///material_list.db", echo=True, future=True)

class products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name =  Column('name', String)
    part_of = ForeignKey('products.id') 
    
    sheets = relationship('sheets', backref='sheets')
    tubes = relationship('tubes', backref='tubes')

    def __repr__(self) -> str:
        return f'{self.name}'

class sheets(Base):
    __tablename__ = 'sheets'
    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'))
    width = Column('width', Integer, nullable=True)
    length = Column('length', Integer, nullable=True)
    diameter = Column('diameter', Integer, nullable=True)
    thickness = Column('thickness', Integer, nullable=True)
    material = Column('material', String)
    amount = Column('amount', Integer)

    def __repr__(self) -> str:
        if self.width:
            return f'{self.width}x{self.length}x{self.thickness}, {self.material}'
        if self.diameter:
            return f'{self.diameter}x{self.thickness}, {self.material}'

class tubes(Base):
    __tablename__ = 'tubes'
    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'))
    length = Column('length', Integer)
    diameter = Column('diameter', Integer)
    thickness = Column('thickness', Integer)
    material = Column('material', String)
    amount = Column('amount', Integer)

    def __repr__(self) -> str:
        return f'{self.diameter}x{self.thickness}x{self.length}, {self.material}'

class nuts(Base):
    __tablename__ = 'nuts'
    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'))
    diameter = Column('diameter', Integer)
    material = Column('material', String)
    amount = Column('amount', Integer)

    def __repr__(self) -> str:
        return f'{self.diameter}, {self.material}'

class bolts(Base):
    __tablename__ = 'bolts'
    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'))
    length = Column('length', Integer)
    diameter = Column('diameter', Integer)
    material = Column('material', String)
    amount = Column('amount', Integer)

    def __repr__(self) -> str:
        return f'{self.diameter}x{self.length}, {self.material}'

class flanges(Base):
    __tablename__ = 'flanges'
    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'))
    diameter = Column('diameter', Integer)
    pressure = Column('pressure', Integer)
    inner_diameter = Column('inner_diameter', Integer)
    material = Column('material', String)
    amount = Column('amount', Integer)

    def __repr__(self) -> str:
        return f'{self.diameter}x{self.pressure}x{self.inner_diameter}, {self.material}'

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
   
