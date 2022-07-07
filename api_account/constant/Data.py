from enum import Enum


class UserData:
    users = [
        {
            "id": 2,
            "email": "nguyen13901@gmail.com",
            "first_name": "Nguyen",
            "last_name": "Pham",
            "address": "Quang Nam",
            "phone": "0944194927",
            "age":"20"
        },
        {
            "id": 3,
            "email": "tranviet0710@gmail.com",
            "first_name": "Viet",
            "last_name": "Tran",
            "address": "Quang Nam",
            "phone": "0905116362",
            "age": "20",
        },
    ]


class RoleData(Enum):
    ADMIN = {
        "id": "0a32895b4e544490ad4368fdca4cfd0b",
        "name": "ADMIN",
    }
    USER = {
        "id": "d03c62ed42454214bc7d4a09770736dc",
        "name": "USER",
    }
