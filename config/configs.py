class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_URL = "postgresql://postgres/egroeg@127.0.0.1:5432/EmployeeManagementSystem"
    SECRET_KEY = "&G0^I#ibETsri0Y0bpUKS"

class Production(Config):
    DEBUG = False
    SECRET_KEY = "&G0^I#ibETsri0Y0bpUKS"

