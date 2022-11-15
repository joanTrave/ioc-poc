from typing import NoReturn

from inversion_of_control.dependencies import autowired
from core.i_repository import IRepository


class UseCase:
    @autowired
    def __init__(self, repository: IRepository):
        self.repository = repository

    def my_use_case(self) -> NoReturn:
        self.repository.custom_method()
