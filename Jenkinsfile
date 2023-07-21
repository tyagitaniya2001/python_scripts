pipeline {
    agent any
    stages {

        stage('Test run') {
            steps {
                echo "Production Deployment with Schemachange"
                }
            }

        stage('Get Schemachange') {
            steps{
                bat "python3.8 -m pip install snowflake-connector-python"
                bat "python3.8 python_script.py"
                }
            }

        
    }
}