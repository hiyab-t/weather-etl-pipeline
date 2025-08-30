CREATE DATABASE api_data;

CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    temperature FLOAT
);