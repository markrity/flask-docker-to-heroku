pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'cimg/base:stable'
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