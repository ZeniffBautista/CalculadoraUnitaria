pipeline {
    agent {
        docker {
            image 'python:3.12'
            args '-v /var/lib/jenkins/workspace:/workspace -v /root/.cache:/root/.cache'
        }
    }
    stages {
        stage('Verificar Instalación') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
            }
        }
        stage('Instalar Dependencias') {
            steps {
                sh 'pip install --user virtualenv'
            }
        }
        stage('Clonar Repositorio') {
            steps {
                // Aquí puedes agregar los pasos para clonar tu repositorio
            }
        }
        stage('Crear Entorno Virtual') {
            steps {
                sh 'python3 -m venv venv'
            }
        }
        stage('Activar Entorno Virtual e Instalar Dependencias') {
            steps {
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Ejecutar Pruebas matemáticas') {
            steps {
                sh 'source venv/bin/activate && pytest'
            }
        }
    }
    post {
        always {
            echo 'Pipeline terminado.'
        }
        failure {
            echo 'Una o más pruebas fallaron.'
        }
    }
}

