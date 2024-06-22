import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://kubernetes:senhaforteaqui@127.0.0.1:5432/kubernetes_deploy'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
