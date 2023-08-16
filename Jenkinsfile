pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    def dockerImage = docker.build("python:3.9")
                    // Tag the image with the build number
                    dockerImage.tag("${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    withDockerRegistry(credentialsId: 'dockerhub-credentials', url: '') {
                        def dockerImage = docker.image("python:3.9")
                        dockerImage.push("${env.BUILD_NUMBER}")
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    try {
                        // Run your tests here
                        sh 'python e2e.py'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                // Stop and remove the Docker container
                def containerId = env.CONTAINER_ID ?: ""
                if (containerId) {
                    sh "docker stop ${containerId}"
                    sh "docker rm ${containerId}"
                }
            }
        }
    }
}
