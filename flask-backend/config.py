import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 
        'postgresql+psycopg2://postgres:postgres@database-1.c3cykq8yqcm2.us-east-2.rds.amazonaws.com:5432/database-1'
    )    
    SQLALCHEMY_TRACK_MODIFICATIONS = False