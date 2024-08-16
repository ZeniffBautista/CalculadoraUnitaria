pipeline {
    agent any  // Ejecutar en cualquier agente disponible

    stages {
        stage('Probar Aplicación') {
            steps {
                script {
                    // Aquí puedes incluir comandos para probar tu aplicación
                    // Por ejemplo, si es una aplicación Python:
                    sh 'python3 app.py'
                }
            }
        }
        stage('Correr Pruebas') {
            steps {
                script {
                    // Ejecutar las pruebas unitarias
                    sh 'python3 -m unittest discover -s tests'
                }
            }
        }
        stage('Limpiar AWS') {
            steps {
                script {
                    // Comandos para limpiar recursos en AWS
                    // Por ejemplo, usando AWS CLI para eliminar instancias o volúmenes
                    sh 'aws ec2 terminate-instances --instance-ids <instance-id>'
                }
            }
        }
    }
    post {
        always {
            // Limpieza general si es necesario
            cleanWs()  // Limpia el espacio de trabajo después de la construcción
        }
    }
}






