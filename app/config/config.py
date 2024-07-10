class Config:
     SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://joaquin:123456789@localhost:5433/dev_database'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://joaquin:123456789@localhost:5433/test_database'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://joaquin:123456789@localhost:5433/database'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}