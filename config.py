import urllib
import pyodbc
import os
from urllib.parse import quote_plus
from urllib import parse
from dotenv import load_dotenv
from os import path


from dotenv import load_dotenv
import os


load_dotenv()
SQLALCHEMY_DATABASE = os.getenv('SQLALCHEMY_DATABASE_URI')
SECRET_KEY = os.getenv('SECRET_KEY')
UPLOADED_PHOTOS_DEST = os.getenv('imagens')


server = os.getenv('Server')
database = os.getenv('Database')
usuario = os.getenv('UID')
password = os.getenv('PWD')
basedir = path.abspath(path.dirname(__file__))


databaseuri = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"
                                 f"SERVER={server};"
                                 f"DATABASE={database};"
                                 f"UID={usuario};"
                                 f"PWD={password}")


uploads = r'C:\Users\Guilherme\Documents\ecommercefllaskapp\appredisflask\app\uploads'

SQLALCHEMY_DATABASE_URI= ("mssql+pyodbc:///?odbc_connect=%s" % databaseuri)