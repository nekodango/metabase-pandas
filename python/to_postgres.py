import pandas as pd
import datetime
from sqlalchemy import create_engine


connection_config = {
    'user': 'metabase',
    'password': 'metabase',
    'host': 'localhost',
    'port': '5432',
    'database': 'metabase'
}

engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{database}'.format(**connection_config))

df = pd.read_csv('data.csv')

df.to_sql('iris', con=engine, if_exists='replace', index=False)
