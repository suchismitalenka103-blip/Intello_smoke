pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Users\\suchismita.lenka\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
        REPORT_NAME = "report_${BRANCH_NAME}.html"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/suchismitalenka103-blip/Seleniumpython.git', 
                    branch: "${BRANCH_NAME}",
                    credentialsId: 'github-https-selenium'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "\"${PYTHON_PATH}\" -m pip install --upgrade pip"
                bat "\"${PYTHON_PATH}\" -m pip install -r requirements.txt"
            }
        }

        stage('Run All Tests') {
            steps {
                // Run all test files in current directory and subdirectories
                bat "\"${PYTHON_PATH}\" -m pytest --html=${REPORT_NAME} --self-contained-html"
            }
        }
    }

    post {
        always {
            // Archive the branch-specific report
            archiveArtifacts artifacts: "${REPORT_NAME}", allowEmptyArchive: true
        }
    }
}