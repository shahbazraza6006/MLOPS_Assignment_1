pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials'
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('fatima:${BUILD_NUMBER}')
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS_ID) {
                        docker.image('my-app:${BUILD_NUMBER}').push('latest')
                        docker.image('my-app:${BUILD_NUMBER}').push('${BUILD_NUMBER}')
                    }
                }
            }
        }
    }  
    
    post {
        success {
            mail to: 'fatimajamshaidkhan2@gmail.com',
                 subject: "Deployment Successful: ${env.JOB_NAME} ${env.BUILD_NUMBER}",
                 body: "The deployment of build  ${env.BUILD_NUMBER} was successful :)."
        }
    }
}
