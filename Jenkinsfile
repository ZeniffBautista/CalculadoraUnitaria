pipeline {
    agent {
        docker {
            image 'python:3.12'
            args '-u root' // Ejecutar como root para evitar problemas de permisos
        }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Instalar Dependencias') {
            steps {
                script {
                    sh 'pip install --upgrade pip' // Asegúrate de tener la última versión de pip
                    sh 'pip install --user --no-cache-dir -r requirements.txt'
                }
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                sh 'python -m unittest discover'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}











