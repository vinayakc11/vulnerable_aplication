pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/vinayakc11/vulnerable_application.git'
            }
        }

        stage('Sonar Scan') {
            steps {
                withSonarQubeEnv('SonarCloud') {
                    sh 'sonar-scanner'
                }
            }
        }
    }
}
