pipeline {
  agent any

  stages {
    stage ('Version') {
      steps {
        sh "echo python3 --version"
     }
   }
    stage('Run Employee Profile Script'){
      steps{
        sh "python3 eprofile.py"
      } 
    }
    stage ('test') {
      steps {
        sh "echo Jenkinsfile did not work!"
      }
    
    }
  }
}
