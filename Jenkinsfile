pipeline {
    agent {
        docker {
            image 'python:3.12'
            args '-u root:root'  // Usa el usuario root para evitar problemas de permisos
        }
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Instalar Dependencias') {
            steps {
                script {
                    // Instalar dependencias
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                script {
                    // Ejecutar pruebas unitarias
                    sh 'python -m unittest discover'
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}


