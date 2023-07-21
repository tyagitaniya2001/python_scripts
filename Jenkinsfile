pipeline {
    agent any
    stages {

        stage('Test run') {
            steps {
                echo "Production Deployment with Schemachange"
                }
            }

        stage('run script') {
            steps{
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'
                sh "pip3 install -r requirements.txt"
                sh "python3 python_script.py"
                }
            }

        
    }
}