pipeline {
    agent any  // Usando 'any' para que el pipeline corra en cualquier nodo disponible
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Instalar Dependencias') {
            steps {
                bat 'pip install --no-cache-dir -r requirements.txt'  // Usar 'bat' en lugar de 'sh'
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                bat 'python -m unittest discover'  // Usar 'bat' en lugar de 'sh'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
