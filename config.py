import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'dd2XG7wZQjrvjy4qm3iIl5j1xBieutG27ta+Vtpbgeg9RSBRur1CFg5Zq6m0X5XViNZl/ccXN+Nz+ASt+RocpA=='

    BLOB_ACCOUNT = 'udacitycmsstorage'
    BLOB_STORAGE_KEY = 'sp=r&st=2022-07-06T13:47:50Z&se=2022-07-06T21:47:50Z&sv=2021-06-08&sr=c&sig=6pkzV760kv7l15jQ3d7py5GvjazU0SYqbgEWHvPkfqs%3D'
    BLOB_CONTAINER = 'images'

    SQL_SERVER = 'udacity-cms-server.database.windows.net'
    SQL_DATABASE = 'udacity-cms-db'
    SQL_USER_NAME = 'udacity-cms-admin'
    SQL_PASSWORD = 'Catherine123$$$'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "if68Q~F~yz3xO9CgA~.excs_eJ9vNY9HCg2Ayddg"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "673e2d07-65ae-41d9-97d3-c4ba65945efa"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session