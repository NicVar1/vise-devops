FROM python:3.11

WORKDIR /app


# Copia los archivos necesarios
COPY requirements.txt ./
COPY app/ ./app/

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Comando para iniciar la API (ejemplo para FastAPI)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]