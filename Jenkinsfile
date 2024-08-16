pipeline {
    agent {
        docker {
            image 'python:3.12' // Imagen base de Python 3.12
            args '-v /var/lib/jenkins/workspace:/workspace' // Monta el directorio de trabajo en el contenedor
        }
    }
    stages {
        stage('Verificar Instalación') {
            steps {
                sh 'python3 --version' // Verifica la versión de Python
                sh 'pip3 --version' // Verifica la versión de pip
            }
        }
        stage('Instalar Dependencias') {
            steps {
                sh 'pip install virtualenv' // Instala virtualenv dentro del contenedor Docker
            }
        }
        stage('Clonar Repositorio') {
            steps {
                sh 'git clone https://github.com/bcaal87/pruebasunitarias.git' // Clona el repositorio en el contenedor
            }
        }
        stage('Crear Entorno Virtual') {
            steps {
                sh 'python3 -m venv venv' // Crea un entorno virtual
            }
        }
        stage('Activar Entorno Virtual e Instalar Dependencias') {
            steps {
                sh '. venv/bin/activate && pip install -r pruebasunitarias/requirements.txt' // Activa el entorno virtual e instala dependencias
            }
        }
        stage('Ejecutar Pruebas matematicas') {
            steps {
                sh '. venv/bin/activate && python pruebasunitarias/test_math.py' // Ejecuta las pruebas matemáticas
            }
        }
    }
    post {
        always {
            echo 'Pipeline terminado.' // Mensaje al finalizar el pipeline
        }
        failure {
            echo 'Una o más pruebas fallaron.' // Mensaje en caso de falla
        }
    }
}

