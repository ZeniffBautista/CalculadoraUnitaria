pipeline {
    agent any

    stages {
        stage('Verificar Instalación') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version || sudo apt-get install python3-pip -y'
                sh 'pip3 install virtualenv || sudo apt-get install python3-venv -y'
            }
        }

        stage('Clonar Repositorio') {
            steps {
                git url: 'https://github.com/bcaal87/pruebasunitarias.git', branch: 'main'
            }
        }

        stage('Crear Entorno Virtual') {
            steps {
                sh 'python3 -m venv venv'
            }
        }

        stage('Activar Entorno Virtual y Instalar Dependencias') {
            steps {
                sh '''
                    set -e
                    source ./venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Ejecutar Pruebas matematicas') {
            steps {
                sh '''
                    set -e
                    source ./venv/bin/activate
                    python app.py
                '''
            }
        }
    }

    post {
        success {
            echo 'Las pruebas se ejecutaron correctamente.'
        }
        failure {
            echo 'Una o más pruebas fallaron.'
        }
    }
}

