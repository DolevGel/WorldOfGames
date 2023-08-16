pipeline {
    agent any

    environment {
        DOCKER_IMAGE_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build("my-python-app:${DOCKER_IMAGE_TAG}", "-f Dockerfile .")
                    env.DOCKER_IMAGE = dockerImage.imageName()
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-credentials') {
                        dockerImage.push("${DOCKER_IMAGE_TAG}")
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh "kubectl apply -f path/to/your/deployment.yaml"
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    try {
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
                sh "docker stop ${DOCKER_IMAGE_TAG} && docker rm ${DOCKER_IMAGE_TAG}"
            }
        }
        success {
            script {
                echo "Build and deployment succeeded!"
            }
        }
        failure {
            script {
                echo "Build and deployment failed!"
            }
        }
    }
}
