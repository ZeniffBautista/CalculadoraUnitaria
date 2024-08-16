FROM python:3.12

# Establece el directorio de trabajo
WORKDIR /app

# Copia el código fuente y requisitos
COPY . /app

# Instala las dependencias
RUN pip install -r requirements.txt

# Comando por defecto
CMD ["python", "-m", "unittest", "discover"]
