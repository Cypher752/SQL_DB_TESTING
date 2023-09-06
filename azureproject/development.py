import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['eidwvjivnb'],
    dbpass=os.environ['R4IBA6760624O8L7$'],
    dbhost=os.environ['notetaking-dnd-server.postgres.database.azure.com'],
    dbname=os.environ['notetaking-dnd-database']
)

TIME_ZONE = 'UTC'

STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_URL = 'static/'

