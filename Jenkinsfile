pipeline {
    agent any

    environment {
        // Set environment variables if any.
        // For example, specify the path to Python or virtualenv.
        // PYTHON_PATH = '/path/to/python'
    }

    stages {
        stage('Checkout') {
            steps {
                // Fetch the latest code from the repository.
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    // Create a Python virtual environment.
                    sh 'python3 -m venv venv'
                    // Activate the virtual environment.
                    sh '. venv/bin/activate'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install the required Python packages.
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/ --junitxml=report.xml'
            }
        }
    }

    post {
        always {
            // Archive the test report regardless of the build result.
            junit 'report.xml'
        }
        success {
            // Actions to perform on successful build.
            echo 'Build succeeded!'
        }
        failure {
            // Actions to perform if the build fails.
            echo 'Build failed!'
        }
    }
}
