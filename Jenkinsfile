@Library('docker') _

pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                script {
                    def gitUrl = 'https://github.com/DolevGel/WorldOfGames.git'
                    def gitCreds = credentials('Dolev') // Replace 'Dolev' with the actual credentials ID

                    checkout([$class: 'GitSCM',
                              branches: [[name: '*/master']],
                              userRemoteConfigs: [[credentialsId: gitCreds.id, url: gitUrl]]])
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build("my-image:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'Dolev', url: 'https://index.docker.io/v1/') {
                        def dockerImage = docker.build("my-image:${env.BUILD_NUMBER}")
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Add steps to run tests here
            }
        }
    }

    post {
        always {
            script {
                // Clean up or other post-build actions
            }
        }
    }
}
