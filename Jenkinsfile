pipeline {
    agent any

    stages {
        stage('Verificar Instalación') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
            }
        }

        stage('Clonar Repositorio') {
            steps {
                git url: 'https://github.com/bcaal87/pruebasunitarias.git', branch: 'main'
            }
        }

        stage('Compilar/Preparar Entorno') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                sh 'python3 app.py'
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

