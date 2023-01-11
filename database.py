from models import products, tubes, sheets, nuts, bolts, flanges
from sqlalchemy import create_engine


class MaterialListDB():
    def __init__(self, path="sqlite:///material_list.db") -> None:
        self.engine = create_engine(path, echo=True, future=True)