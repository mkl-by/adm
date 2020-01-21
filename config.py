
import os.path

class Configuration():

    #настройки фласк
    DEBUG = True
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    print('Путь: ', BASEDIR)
    SECRET_KEY = 'ldskfjlsdkfjl'
    #настройки базы данных
    SQLALCHEMY_DATABASE_URI = 'sqlite:///basa'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #flask-security
    SECURITY_PASSWORD_SALT = 'slfjdlskdjf'
    SECURITY_PASSWORD_HASH='sha512_crypt' #алгоритм хэширования
    #bootstrap
    BOOTSTRAP_SERVE_LOCAL=True #Работаем с локальным бутстрапом