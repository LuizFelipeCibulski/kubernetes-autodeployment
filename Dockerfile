# Usar a imagem oficial do Python como base
FROM python:3.9

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos de requisitos do projeto para o diretório de trabalho
COPY requirements.txt requirements.txt

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código para o diretório de trabalho
COPY . .

# Definir a variável de ambiente para que o Flask rode no modo de produção
ENV FLASK_ENV=production

# Comando para rodar o aplicativo Flask
CMD ["flask", "run", "--host=0.0.0.0"]
