pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                pytest --cov
            }
        }
        stage('Build') {
            steps {
                docker-compose build
            }
        }
        stage('Push') {
            steps {
                docker-compose push
            }
        }
        stage('Configuration Management') {
            steps {
                ansible-playbook -i inventory.yaml playbook.yaml
            }
        }
        stage('Deploy') {
            steps {
                //create swarm infastructure
            }
        }
    }
}