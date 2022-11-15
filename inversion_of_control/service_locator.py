import glob
import importlib
import sys
from pathlib import Path
from typing import NoReturn

PYTHON_EXTENSION: str = ".py"


def get_executable_parent_path(executable_path: str) -> str:
    return str(Path(executable_path).parent.absolute())


def get_module_name_from_absolute_path(filename: str) -> str:
    return filename.split("/")[-1].split(".")[0]


def discover_services() -> NoReturn:
    """
    Discovers recursively all services that match with termination and execute them in order to save them to
    services diot.
    """
    executable_parent_path = get_executable_parent_path(sys.argv[0])
    for filename in glob.iglob(executable_parent_path + f"/**/*{PYTHON_EXTENSION}", recursive=True):
        if "\n@service" in open(filename).read():
            module_name: str = get_module_name_from_absolute_path(filename)
            spec = importlib.util.spec_from_file_location(module_name, filename)
            foo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(foo)
