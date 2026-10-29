# Remote library imports
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt
from sqlalchemy.pool import NullPool

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))

def load_env_file(path):
    if not os.path.exists(path):
        return
    with open(path) as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, value = line.split('=', 1)
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
                value = value[1:-1]
            # An explicit environment variable wins over the file.
            os.environ.setdefault(key.strip(), value)

# neon deploy writes the pooled and direct URLs here.
load_env_file(os.path.join(ROOT_DIR, '.env.local'))
load_env_file(os.path.join(ROOT_DIR, '.env'))

def normalize_database_url(url):
    if url.startswith('postgres://'):
        return 'postgresql://' + url[len('postgres://'):]
    return url

def database_uri():
    # Migrations and seeding need the direct connection. The running app uses
    # the pooled URL, which is the right one for a serverless host like Vercel.
    if os.environ.get('NEON_USE_DIRECT') == '1' and os.environ.get('DATABASE_URL_UNPOOLED'):
        return normalize_database_url(os.environ['DATABASE_URL_UNPOOLED'])
    configured = os.environ.get('DATABASE_URL')
    if not configured:
        return 'sqlite:///app.db'
    return normalize_database_url(configured)


app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', '5389h234ujrfb@!#$RF4f5')

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri()
engine_options = {'pool_pre_ping': True}
if os.environ.get('VERCEL'):
    # PgBouncer already pools connections. Don't keep a pool inside each function.
    engine_options['poolclass'] = NullPool
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = engine_options
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

CORS(app)