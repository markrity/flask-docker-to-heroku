pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'curlimages/curl:latest'
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