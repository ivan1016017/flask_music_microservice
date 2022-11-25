from flask import Flask
import os 
from dotenv import load_dotenv

load_dotenv()

# variable = 'postgresql://ivan:1234@localhost/tutorial_canciones'

URI_DB = 'postgresql://{}:{}@{}/{}'.format(os.getenv('USER_DB'),
os.getenv('PASSWORD_DB'),os.getenv('PORT_DB'), os.getenv('NAME_DB'))

# URI_DB = variable

def create_app(config_name):
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = URI_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['PROPAGATE_EXCEPTIONS']=True

    return app 

