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
                bat 'python -m venv myenv'
                bat 'call myenv/bin/activate'
                bat "pip3 install -r requirements.txt"
                bat "python3 python_script.py"
                }
            }

        
    }
}