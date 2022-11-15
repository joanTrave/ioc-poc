from inversion_of_control.dependencies import service
from core.i_repository import IRepository


@service("MONGO")
class MongoRepository(IRepository):
    def custom_method(self):
        print("Mongo repository")
