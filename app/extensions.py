from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


api = Api(title='The Football App API', description='An API for The Football App')
db = SQLAlchemy(metadata=MetaData(schema='dbo'))
