pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Test') { 
            steps {
                echo 'python3 manage.py test'
            }
        }
        stage('Deploy') { 
            steps {
                sh 'ssh -o StrictHostKeyCHecking=no nutrixadmin@20.198.225.83 "cd nutrix-backend \
                source env/bin/activate; \
                git status " '
            }
        }
    }
}