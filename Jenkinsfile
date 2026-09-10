pipeline {
    agent any

    parameters {
        choice(name: 'MOCK_TEST_SUITE', choices: ['smoke', 'regression'], description: 'Test suite to run')
    }

    environment {
        ALLURE_ENDPOINT = 'https://nimaruichi.qameta.in'
        ALLURE_PROJECT_ID = '1'
        ALLURE_RESULTS = 'allure-results'
        ALLURE_LAUNCH_NAME = 'TestForJenkins1'
        ALLURE_TOKEN = credentials('allure-token')
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh 'python3 -m pip install --user -r requirements.txt'
            }
        }

        stage('Run tests and upload to TestOps') {
            steps {
                sh '''#!/bin/sh
                    export PATH="$HOME/.local/bin:$PATH"
                    allurectl watch -- python3 -m pytest "tests/$MOCK_TEST_SUITE" --alluredir="$ALLURE_RESULTS" --clean-alluredir
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
        }
    }
}
