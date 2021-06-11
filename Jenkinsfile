pipeline {
    agent any
    environment {
        DOCKER_USERNAME = credentials('DOCKER_USERNAME')
        DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
    }
    stages {
        stage('Install Requirements') {
            steps {
                sh 'bash jenkins/install-requirements.sh'
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
                //create swarm infastructure
                sh 'echo deploy'
            }
        }
    }
}