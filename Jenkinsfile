pipeline {
    agent any
    environment {
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
        DATABASE_URI = credentials('DATABASE_URI')
        SECRET_KEY = credentials('SECRET_KEY')
        install = "false"
    }
    stages {
        stage('Install Requirements') {
            steps {
                script {
                    if (env.install=='true'){
                        sh 'bash jenkins/install-requirements.sh'
                    }
                }
            }
        }
        stage('Test') {
            steps {
                sh 'bash jenkins/test.sh'
            }
        }
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Push') {
            steps {
                sh 'docker-compose push'
            }
        }
        stage('Configuration Management') {
            steps {
                sh 'cd ansible && ~/.local/bin/ansible-playbook -i inventory.yaml playbook.yaml'
            }
        }
        stage('Deploy') {
            steps {
                sh 'bash jenkins/deploy.sh'
            }
        }
    }
}