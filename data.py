class ResponseMassages:
    CREATE_COURIER_SUCCESS = {"ok": True}
    ERROR_DUPLICATE_LOGIN = {"message": "Этот логин уже используется"}
    MISSING_REQUIRED_FIELDS = {"message": "Недостаточно данных для создания учетной записи"}
    MISSING_REQUIRED_FIELDS_LOGIN = {"message":  "Недостаточно данных для входа"}
    ERROR_ACCOUNT_NOT_FOUND = {"message": "Учетная запись не найдена"}

class Flags:
    COURIER_ID = "id"

class Data:
    ORDER_DATA = {
                "firstName": "Naruto",
                "lastName": "Uchiha",
                "address": "Konoha, 142 apt.",
                "metroStation": 4,
                "phone": "+7 800 355 35 35",
                "rentTime": 5,
                "deliveryDate": "2026-11-10",
                "comment": "Saske, come back to Konoha"
    }

    ORDER_DATA_GREY = {**ORDER_DATA, "color": ["GREY"]}
    ORDER_DATA_BLACK = {**ORDER_DATA, "color": ["BLACK"]}
    ORDER_DATA_BOTH = {**ORDER_DATA, "color": ["GREY", "BLACK"]}
    ORDER_DATA_NO_COLOR = ORDER_DATA.copy()