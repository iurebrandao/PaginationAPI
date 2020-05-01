import os

project_dir = os.path.dirname(os.path.abspath(__file__))


class BaseConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(project_dir, "wine.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAGE_SIZE = 10



class ProductionConfig:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(project_dir, "wine.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAGE_SIZE = 10
