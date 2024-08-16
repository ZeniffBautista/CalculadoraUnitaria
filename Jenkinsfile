pipeline {
    agent any

    parameters {
        booleanParam(name: 'RUN_PROBAR_APLICACION', defaultValue: true, description: 'Ejecutar la aplicación')
        booleanParam(name: 'RUN_CORRER_PRUEBAS', defaultValue: true, description: 'Ejecutar pruebas unitarias')
        booleanParam(name: 'RUN_LIMPIAR_AWS', defaultValue: false, description: 'Limpiar recursos en AWS')
    }

    stages {
        stage('Probar Aplicación') {
            when {
                expression { params.RUN_PROBAR_APLICACION }
            }
            steps {
                script {
                    // Comando para probar la aplicación
                    sh 'python3 app.py'
                }
            }
        }
        stage('Correr Pruebas') {
            when {
                expression { params.RUN_CORRER_PRUEBAS }
            }
            steps {
                script {
                    // Comando para ejecutar pruebas unitarias
                    sh 'python3 -m unittest discover -s tests'
                }
            }
        }
        stage('Limpiar AWS') {
            when {
                expression { params.RUN_LIMPIAR_AWS }
            }
            steps {
                script {
                    // Comando para limpiar recursos en AWS
                    sh 'aws ec2 terminate-instances --instance-ids <instance-id>'
                }
            }
        }
    }
    post {
        always {
            // Limpia el espacio de trabajo
            cleanWs()
        }
    }
}







