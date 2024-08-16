pipeline {
    agent {
        docker {
            image 'python:3.12'
            args '-v /var/lib/jenkins/workspace/DemoTest:/workspace'
        }
    }

    stages {
        stage('Clonar Repositorio') {
            steps {
                git url: 'https://github.com/bcaal87/pruebasunitarias.git', branch: 'main'
            }
        }

        stage('Instalar Dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar Pruebas matematicas') {
            steps {
                sh 'python app.py'
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
