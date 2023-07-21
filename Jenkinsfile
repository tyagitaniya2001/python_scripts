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
                bat 'pip install --upgrade setuptools'
                bat "pip3 install -r requirements.txt"
                bat 'pip install --upgrade snowflake-connector-python'
                bat 'pip freeze -r requirements.txt'
                bat "python3 test.py"
                bat "python3 python_script.py"
                
                }
            }

        
    }
}