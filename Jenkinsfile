pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                sh '''
                    curl https://cli-assets.heroku.com/install.sh | sh;
                    heroku
                '''
            }
        }
    }
}