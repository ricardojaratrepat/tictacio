# Usa una imagen de Python como base
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requerimientos e instálalos
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia el resto del código del backend
COPY . .

# Exponer el puerto en el que corre FastAPI (por defecto 8000)
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
