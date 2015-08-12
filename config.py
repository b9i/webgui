import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ganz komplizierter Schluessel'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    
    @staticmethod
    def init_app(app):
        print("start...")
        pass

class DevelopmentConfig(Config):
    DEBUG=True

class TestingConfig(Config):
    DEBUG=True

class ProductionConfig(Config):
    DEBUG=True

webgui_settings = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
        }

# default variables
default_variables = {
  'uptime' : 0,                       # this contains uptime
  'first_view_mod'   : 'CustomAll',     # set default view by module's first view
  'first_view_name'  : 'view_customall',
  'refresh' : 1,                      # default refresh value [s]
}

# html menu
# will append item from each module automatically based on hook menu
menu_items        = {} # key, name
menu_items_module = {} # this hold key to module connection

#used for storing enabled modules 
modules = {}

#module configuration
webgui_modules = {}

webgui_modules['BmsLionSQL'] = {
    'db_filename':'todo.db',
    'db_scheme'  :'db_scheme.sql'
}

#webgui_modules['BmsLion'] = {
#    '/dev/ttyACM0','/dev/ttyACM1',
#    '/dev/ttyUSB0',
#    '/dev/tty.usbmodem01',
#    #'/home/kortas/minicom.cap']
#}
webgui_modules['SendMail'] = {
    "SMTPserver":'smtp.seznam.cz', 
    'sender':'petrkortanek@seznam.cz',
    'destination':'petrkortanek@seznam.cz',
    "username":'petrkortanek',
    'password':'x'
}

webgui_modules['SDSmikro_doma'] = {
    'name' : 'SDS doma',
    'address':'192.168.33.43',
    'password': 'xxx'
}

webgui_modules['SDSmikro_policko'] = {
    'name' : 'SDS policko',
    'address':'192.168.33.101',
    'password': 'xxx'
}

webgui_modules['Midnite'] = {
    'name' : 'Midnite',
    'address':'192.168.33.6',
}

webgui_modules['Camera'] = {
    'name' : 'BazenCam',
    'address':'http://192.168.33.8/live/snapshot',
    'username': 'admin',
    'password': 'admin'
}

webgui_modules['CustomAll'] = {
    'name' : 'VŠE',
}
