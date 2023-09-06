import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('09377f64f415380f9e3fdb62ecb9b2db773081eb12bde62222d723134b16c7a6')

ALLOWED_HOSTS = [os.environ['notetaking-dnd-server.postgres.database.azure.com']] if 'notetaking-dnd-server.postgres.database.azure.com' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['notetaking-dnd-server.postgres.database.azure.com']] if 'notetaking-dnd-server.postgres.database.azure.com' in os.environ else []

# Configure Postgres database based on connection string of the libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
conn_str = os.environ['dbname=notetaking-dnd-database host=notetaking-dnd-server.postgres.database.azure.com port=5432 sslmode=require user=eidwvjivnb password=R4IBA6760624O8L7$']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=conn_str_params['eidwvjivnb'],
    dbpass=conn_str_params['R4IBA6760624O8L7$'],
    dbhost=conn_str_params['notetaking-dnd-server.postgres.database.azure.com'],
    dbname=conn_str_params['notetaking-dnd-database']
)