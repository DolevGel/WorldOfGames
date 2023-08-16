pipeline {
    agent any

    environment {
        CONTAINER_ID = ""
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build and Run Container') {
            steps {
                script {
                    // Build the Docker image using Docker Compose
                    sh "docker-compose build"

                    // Run the Docker container using Docker Compose
                    sh "docker-compose up"
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        bat 'python e2e.py'
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
                // Stop and remove the Docker container using Docker Compose
                sh "docker-compose down"
            }
        }
        success {
            script {
                docker.withRegistry('', 'dockerhub-credentials') {
                    docker.image("python:3.9").push("${env.BUILD_NUMBER}")
                }
            }
        }
    }
}
