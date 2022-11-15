from application.use_case import UseCase
from inversion_of_control.service_locator import discover_services


def main():
    discover_services()
    UseCase().my_use_case()


if __name__ == "__main__":
    main()
