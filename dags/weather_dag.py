from datetime import datetime, timedelta
from airflow.decorators import dag, task
from pathlib import Path
import sys, os
from dotenv import load_dotenv

sys.path.insert(0, 'opt/airflow/src')

from src.extract_data import extract_weather_data
from src.load_data import load_weather_data
from src.transform_data import data_transformations

env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(env_path)

API_KEY = os.getenv('API_KEY')

url = f'http://api.openweathermap.org/data/2.5/weather?q=Sao Paulo,br&APPID={API_KEY}'


@dag(
    dag_id='data_weather_pipeline',
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
    },
    description='ETL Pipeline - Weather',
    schedule='0 */1 * * * ',
    start_date=datetime(2026, 2, 7),
    catchup=False,
    tags=['weather', 'etl']
)

def weather_pipeline():
    
    @task
    def extract():
        extract_weather_data(url)

    
    @task
    def transform():
        import pandas as pd
        df = data_transformations()
        df = pd.read_parquet('/opt/airflow/data/temp_data.parquet')

    @task 
    def load():
        import pandas as pd
        df = pd.read_parquet('/opt/airflow/data/temp_data.parquet')
        load_weather_data('sp_weather', df)        

    extract() >> transform() >> load()


weather_pipeline()    

