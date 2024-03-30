pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = '2025746b-4243-42ac-a1b6-2a7bf0881c99' // Jenkins credentials ID for Docker Hub login
        DOCKER_IMAGE_NAME = 'appflask' // Docker image name
        DOCKERFILE_PATH = 'Dockerfile' 
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("appflask", "-f ${env.DOCKERFILE_PATH} .")
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', env.DOCKER_HUB_CREDENTIALS) {
                        docker.image(env.DOCKER_IMAGE_NAME).push('latest')
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image build and push successful!'
            mail to: 'fatimajamshaidkhan2@gmail.com',
                 subject: "Deployment Successful: ${env.JOB_NAME} ${env.BUILD_NUMBER}",
                 body: "The deployment of build  ${env.BUILD_NUMBER} was successful :)."
        }
        failure {
            echo 'Docker image build or push failed!'
        }
    }
}
   
