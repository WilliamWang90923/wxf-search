from functools import wraps


def singleton(cls):

    _instance = {}

    @wraps(cls)
    def instance(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return instance