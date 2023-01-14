from models import Products, Tubes, Sheets, Nuts, Bolts, Flanges
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class MaterialListDB():
    def __init__(self, path="sqlite:///material_list.db") -> None:
        self.__engine = create_engine(path, echo=True, future=True)

    
    def add_product(self, name: str, part_of: int):
        with Session(self.__engine) as session:
            product = Products(name=name, part_of=part_of)
            session.add(product)
            session.commit()
        return product
    
    def add_sheet(self, product_id, width, length, diameter, thickness, material, amount ):
        with Session(self.__engine) as session:
            sheet = Sheets(product_id=product_id,
                           width=width, length=length,
                           diameter=diameter, thickness=thickness,
                           material=material, amount=amount)
            session.add(sheet)
            session.commit()
        return sheet

    def add_tube(self, product_id, length, diameter, thickness, material, amount ):
        with Session(self.__engine) as session:
            tube = Sheets(product_id=product_id,
                           length=length,
                           diameter=diameter, thickness=thickness,
                           material=material, amount=amount)
            session.add(tube)
            session.commit()
        return tube
    
    def add_nut(self, product_id, diameter, material, amount ):
        with Session(self.__engine) as session:
            nut = Nuts(product_id=product_id,
                        diameter=diameter,
                        material=material, amount=amount)
            session.add(nut)
            session.commit()
        return nut
    
    def add_bolt(self, product_id, diameter, length, material, amount ):
        with Session(self.__engine) as session:
            bolt = Bolts(product_id=product_id,
                        diameter=diameter, length=length,
                        material=material, amount=amount)
            session.add(bolt)
            session.commit()
        return bolt

    def add_flange(self, product_id, diameter, pressure, inner_diameter, material, amount ):
        with Session(self.__engine) as session:
            flange = Flanges(product_id=product_id,
                        diameter=diameter, pressure=pressure,
                        inner_diameter=inner_diameter,
                        material=material, amount=amount)
            session.add(flange)
            session.commit()
        return flange

if __name__ == '__main__':
    db = MaterialListDB()
    db.add_product('Люк', None)