pipeline {
  agent any

  stages {
    stage ('Build') {
      steps {
        sh "echo Welcome! Add your profile to Our Database"
     }
   }
    stage('Run Employee Profile Script'){
      steps{
        sh "eprofile.py"
      } 
    }
    stage ('test') {
      steps {
        sh "echo Jenkinsfile did not work!"
      }
    
    }
  }
}
