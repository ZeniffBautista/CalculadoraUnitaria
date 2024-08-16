pipeline {
    agent any

    stages {
        stage('Verificar Instalación') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'pip install --user pipx'
                sh 'pipx --version'
            }
        }

        stage('Crear Entorno Virtual') {
            steps {
                sh '''
                    pipx install virtualenv
                    pipx runpip virtualenv install --upgrade pip
                '''
            }
        }

        stage('Clonar Repositorio') {
            steps {
                git url: 'https://github.com/bcaal87/pruebasunitarias.git', branch: 'main'
            }
        }

        stage('Instalar Dependencias') {
            steps {
                sh '''
                    pipx runpip virtualenv install -r requirements.txt
                '''
            }
        }

        stage('Ejecutar Pruebas matematicas') {
            steps {
                sh '''
                    pipx run virtualenv python app.py
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




