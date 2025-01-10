FROM python:3.11.11-alpine3.20

# Etapa 2: Instalar dependências
# Copiar o arquivo de requisitos (se existir) para o container
# COPY requirements.txt /app/requirements.txt
# RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar o código fonte para o container
WORKDIR /app
COPY requirements.txt /app/
COPY relay.py /app/

# Etapa 3: Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 4: Expor a porta que o serviço irá escutar
#EXPOSE 1025

# Etapa 5: Comando para rodar o servidor SMTP
CMD ["python", "relay.py"]
