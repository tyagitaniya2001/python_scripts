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
                bat "python pip install snowflake-connector-python"
                bat "python python_script.py"
                }
            }

        
    }
}