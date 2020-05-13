class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:TheriON9@localhost/twp3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    #                                                   flask security
    SECRET_KEY = 'Nafunya'
    SECURITY_PASSWORD_SALT = "dhdhwthrdth5w34th7iehw5ysg%yyWy4%Ya"
    SECURITY_PASSWORD_HASH = 'bcrypt'

