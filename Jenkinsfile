pipeline {
    agent any
    tools{
        terraform 'Terraform'
    }
    environment{
        AWS_ACCESS_KEY_ID     = credentials('aws-cred')
        AWS_SECRET_ACCESS_KEY = credentials('aws-cred1')
    }

    stages {
        stage('dev') {
            steps {
                sh '''
                terraform init
                terraform plan -out=dev.tfplan
                terraform apply dev.tfplan
                '''
            }
        }
    }
}
