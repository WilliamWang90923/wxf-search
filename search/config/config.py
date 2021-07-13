import os


class Config:
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    MONGODB = dict(
        MONGO_HOST=os.getenv('MONGO_HOST', "192.168.5.134"),
        MONGO_PORT=int(os.getenv('MONGO_PORT', 27017)),
        MONGO_USERNAME=os.getenv('MONGO_USERNAME', "root"),
        MONGO_PASSWORD=os.getenv('MONGO_PASSWORD', "root"),
        DATABASE='wxfnews',
    )
