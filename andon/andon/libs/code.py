from enum import IntEnum


class Code(IntEnum):
    ERROR = 0
    SUCCESS = 1
    FAILED = 2
    ACCESS_EXPIRED = 3
    REFRESH_EXPIRED = 4


def success_dict(msg: str, data: dict) -> dict:
    return {"code": Code.SUCCESS, "msg": msg, "data": data}