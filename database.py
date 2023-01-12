from models import products, tubes, sheets, nuts, bolts, flanges
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class MaterialListDB():
    def __init__(self, path="sqlite:///material_list.db") -> None:
        self.engine = create_engine(path, echo=True, future=True)

    
    def add_product(self, name: str, part_of:products):
        with Session(self.engine) as session:
            product = products(name=name, part_of=part_of)
            session.add(product)
            session.commit()
        return product

if __name__ == '__main__':
    db = MaterialListDB()
    db.add_product('Люк', None)