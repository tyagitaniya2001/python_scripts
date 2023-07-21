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
                bat "pip3 install -r requirements.txt"
                bat "python3 python_script.py"
                }
            }

        
    }
}