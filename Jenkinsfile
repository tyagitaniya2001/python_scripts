pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }
    
    stages {

        stage('Test run') {
            steps {
                echo "Production Deployment with Schemachange"
                }
            }

        stage('run script') {
            steps{
                bat 'pip install virtualenv'
                bat 'python -m virtualenv myenv'
                bat 'call myenv/bin/activate'
                bat "pip3 install -r requirements.txt"
                bat "python3 python_script.py"
                }
            }

        
    }
}