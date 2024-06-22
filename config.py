import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://seu_usuario:sua_senha@seu_host:5432/kubernetes_deploy'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
