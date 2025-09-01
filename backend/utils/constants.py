from enum import Enum

class UserRoles(str, Enum):
    # By inheriting from str the API docs will be able to know that the values must be of type string and will be able to render correctly.
    ADMIN = "admin"
    USER = "user"
