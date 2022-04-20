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
                sh 'python3 manage.py test'
            }
        }
        stage('Deploy') { 
            steps {
                sh 'ssh ssh nutrixadmin@20.212.130.228 "sour env/bin/activate; \
                cd nutrix-backend \
                git pull origin master; \
                pip install -r requirements.txt --no-warn-script-location; \
                python manage.py migrate; \
                deactivate; \
                sudo systemctl restart nginx; \
                sudo systemctl restart gunicon " '
            }
        }
    }
}