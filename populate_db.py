import pandas
import os
from config import BaseConfig
from sqlalchemy import create_engine

wine_df = pandas.read_csv('data/winemag-data-130k-v2.csv')
engine = create_engine(BaseConfig.SQLALCHEMY_DATABASE_URI, echo=False)
wine_df.rename(columns={'Unnamed: 0': 'id'}, inplace=True)
wine_df.to_sql(con=engine, name='wine', if_exists='append', index=False)