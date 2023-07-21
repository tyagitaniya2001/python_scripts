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
                bat "python --version"
                bat 'pip install --upgrade setuptools'
                bat "pip install -r requirements.txt"
                bat 'pip install --upgrade snowflake-connector-python'
                bat 'pip freeze -r requirements.txt'
                bat 'pip install snowflake-ingest'
                bat "python test.py"
                bat "python python_script.py"
                
                }
            }

        
    }
}