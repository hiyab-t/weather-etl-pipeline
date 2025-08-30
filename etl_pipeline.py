import pandas as pd
from main import data
import psycopg2 as psycopg
from sql_utils import config
import logging

logging.basicConfig(filename='pipeline.log', level=logging.ERROR)


# extract data from the JSON response

temperature_data = data['hourly']['temperature_2m']
timestamps = data['hourly']['time']

# create a DataFrame

df = pd.DataFrame({'timestamp': timestamps, 'temperature': temperature_data})

# convert timestamp to datetime format

df['timestamp'] = pd.to_datetime(df['timestamp'])
print(df.head())

# load stage

# connect to postgresql
try:
    with psycopg.connect(config) as conn:
    
        cur = conn.cursor()
    
        # insert DataFrame into postgresql
    
        for _, row in df.iterrows():
            cur.execute(
                "INSERT INTO weather_data (timestamp, temperature) VALUES (%s, %s)",
                (row['timestamp'], row['temperature'])
            )
    
        # commit changes 
    
        conn.commit()
        logging.INFO("Data inserted into PostgreSQL successfully!")

except Exception as err:
        logging.error(f"Unexpected {err=}, {type(err)=}", exc_info=True)

