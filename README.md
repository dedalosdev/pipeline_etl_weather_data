# pipeline_etl_weather_data
This is a open-source data engineering project to beginners, a Python backend and PostgreSQL database. Designed for data engineering learning.


# database settings
psql postgres
postgres=# create role postgres with login password 'yourpassword';
postgres=# alter role postgres with login password 'yourpassword';
ALTER ROLE
postgres=# alter role postgres superuser createdb createrole;
ALTER ROLE
postgres=# create database weather_data owner postgres;
CREATE DATABASE
postgres=# \l
postgres=# \q


# instalation instructions
git clone https://github.com/dedalosdev/pipeline_etl_weather_data.git

cd pipeline_etl_weather_data
cp .env.example .env
Edit the database credentials
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt


## License

pipeline_etl_weather_data is an open-source project licensed under the Apache License.

You are free to use, copy, modify, distribute, sublicense, and
commercialize this project for personal, educational, or commercial
purposes, subject to the terms of the Apache License.

See the [LICENSE](./LICENSE) file for the complete license text.