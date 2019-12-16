import os

class BaseConfig:
    """Base configuration"""
    TESTING = False
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQL_ALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig(BaseConfig):
    """Testing Configuration"""
    TESTING = True
    SQL_ALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  

class ProductionConfig(BaseConfig):
    """Production configuration"""
    SQL_ALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')