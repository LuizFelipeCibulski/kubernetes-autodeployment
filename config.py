import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://kubernetes:senhaforteaqui@10.15.1.120:5432/kubernetes_deploy'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
