pipeline {
    agent {
        docker { image 'python:3.12' }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Instalar Dependencias') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
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





