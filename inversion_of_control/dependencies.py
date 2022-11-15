import os
from typing import Type, TypeVar, Callable, Dict, Set
import inspect

from dotenv import load_dotenv


T = TypeVar("T")
DEFAULT: str = "DEFAULT"

load_dotenv()
services_dict: Dict[str, Dict[Type[T], Type[T]]] = {}
services: Set[Type[T]] = set()


def get_context() -> str:
    return os.environ.get("CONTEXT", DEFAULT)


def autowired(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        func_annotation: Dict[str, Type[T]] = inspect.getfullargspec(func).annotations
        for key_param, key_type in func_annotation.items():
            if key_type in services:
                kwargs[key_param] = services_dict[get_context()][key_type]()
        func(*args, **kwargs)
    return wrapper


def service(context_name: str = DEFAULT) -> Callable[[Type[T]], Type[T]]:
    """
    Appends decorated class to service dictionary and total mapped service set.

    :param context_name:
    """

    def decorator(cls: Type[T]) -> Type[T]:
        if not services_dict.get(context_name):
            services_dict[context_name] = {}
        class_base: Type[T] = cls.__bases__[0]  # Interface
        # Check if service already is mapped for context
        if services_dict.get(context_name).get(class_base):
            raise ValueError(f"Service {class_base} already mapped for context {context_name}")
        services_dict[context_name][class_base] = cls
        services.add(class_base)
        return cls

    return decorator
