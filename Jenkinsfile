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
                bat "python3 -m pip uninstall snowflake-connector-python"
                bat "python3 -m pip install snowflake-connector-python"
                bat "python3 python_script.py"
                }
            }

        
    }
}