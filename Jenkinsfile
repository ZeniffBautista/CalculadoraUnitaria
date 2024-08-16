pipeline {
    agent {
        docker {
            image 'python:3.12'
            args '-v /var/lib/jenkins/workspace:/workspace'
        }
    }
    stages {
        stage('Preparar') {
            steps {
                // Clonar el repositorio
                checkout scm
            }
        }
        stage('Instalar Dependencias') {
            steps {
                // Instalar dependencias
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                // Ejecutar pruebas unitarias
                sh 'python -m unittest discover'
            }
        }
    }
    post {
        always {
            // Limpiar el workspace después de la ejecución
            cleanWs()
        }
    }
}


