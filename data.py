class ResponseMassages:
    CREATE_COURIER_SUCCESS = {"ok": True}
    ERROR_DUPLICATE_LOGIN = {"message": "Этот логин уже используется"}
    MISSING_REQUIRED_FIELDS = {"message": "Недостаточно данных для создания учетной записи"}
    MISSING_REQUIRED_FIELDS_LOGIN = {"message":  "Недостаточно данных для входа"}
    ERROR_ACCOUNT_NOT_FOUND = {"message": "Учетная запись не найдена"}

class Flags:
    COURIER_ID = "id"

class Colors:
    ORDER_COLORS = [["GREY"], ["BLACK"], ["GREY", "BLACK"], None]

    