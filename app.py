from flask import Flask

from flask_security import SQLAlchemyUserDatastore, Security
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin
#from flask_admin.contrib.fileadmin import FileAdmin

from flask_bootstrap import Bootstrap

from os import path as ospa

#приложение
app = Flask(__name__)
app.config.from_object(Configuration)

#bootstrap
Bootstrap(app)

#база
db=SQLAlchemy(app)

#миграции
migrate=Migrate(app, db)
manager=Manager(app)
manager.add_command('db', MigrateCommand) #Создаем команду db для мигаций

#ADMIN
from admin import AdminView, HomeAdminView
from models import *

admin=Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Home')) #url-перенаправляем на наш сайт если юзер не админ
admin.add_view(AdminView(Role, db.session))
admin.add_view(AdminView(User, db.session))
#при необходимости показываем файлы
# path = ospa . join ( ospa . dirname ( __file__ ), 'static' )
# admin . add_view ( FileAdmin ( path , '/static/' , name = 'Static Files' ))

#установка секюрити
user_datastore=SQLAlchemyUserDatastore(db, User, Role) #объект хранит юзеров и роли
security=Security(app, user_datastore)

#регистрируем блюпринты
from statis.statistic import statistic
app.register_blueprint(statistic, url_prefix='/statistic')

