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
                sh 'ssh nutrixadmin@20.198.225.83 "cd nutrix-backend \
                source env/bin/activate; \
                git pull origin master; \
                pip install -r requirements.txt --no-warn-script-location; \
                python3 manage.py migrate; \
                sudo systemctl restart nginx; \
                sudo systemctl restart gunicorn " '
            }
        }
    }
}