pipeline {
    agent any

    stages {
        stage('Verificar Instalación') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'pipx --version'
            }
        }

        stage('Clonar Repositorio') {
            steps {
                git url: 'https://github.com/bcaal87/pruebasunitarias.git', branch: 'main'
            }
        }

        stage('Crear Entorno Virtual y Instalar Dependencias') {
            steps {
                sh 'pipx runpip venv install -r requirements.txt'
            }
        }

        stage('Ejecutar Pruebas matematicas') {
            steps {
                sh 'pipx run venv python app.py'
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


