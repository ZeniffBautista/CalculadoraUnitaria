# Usa una imagen base de Python
FROM python:3.12

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos e instala las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente
COPY . /app/

# Comando por defecto para ejecutar las pruebas
CMD ["python", "-m", "unittest", "discover"]


