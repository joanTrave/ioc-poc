from inversion_of_control.dependencies import service
from core.i_repository import IRepository


@service()
class PostgreRepository(IRepository):
    def custom_method(self):
        print("Postgre respoistory")
