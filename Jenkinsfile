pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/suchismitalenka103-blip/Seleniumpython.git', 
                    branch: 'main',
                    credentialsId: 'github-https-selenium'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Use full path to python
                bat '"C:\\Users\\suchismita.lenka\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install --upgrade pip'
                bat '"C:\\Users\\suchismita.lenka\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\suchismita.lenka\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pytest --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
    }
}
