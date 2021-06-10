pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                //sh 'bash jenkins/test.sh'
                sh 'echo test'
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
                //ansible-playbook -i inventory.yaml playbook.yaml
                sh 'echo config'
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