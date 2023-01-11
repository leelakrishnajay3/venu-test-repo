#!groovy
void  Fetch_code_from_repo(){
      checkout([
        $class: 'GitSCM', branches: [[name: '*/$branchname']],extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'code']],userRemoteConfigs: [[url: '$GITURL',credentialsId:'Github']]
      ])
}
pipeline {
    agent any
    environment {
     manifestfile="$WORKSPACE/CHR12345.csv"
     gitcheckout_path="$WORKSPACE/$CUNumber"   
     COPY_PATH="$WORKSPACE"
     artifacts_path="$WORKSPACE"
    }
    parameters {
    string description: 'please enter the git url', name: 'GITURL'
    choice choices: ['release', 'hotfix'], description: 'please enter the branchname', name: 'branchname'
    string description: 'please enter buidID', name: 'buildID'
    string description: 'please enter the CU number', name: 'CUNumber'
             }
    stages {
        stage('Check BUildID exist') {
        steps{
             echo "${buildID}"
               }
        stage('Fetch_code_from_repo') {
        steps{
              Download_Repositories()
              dir("${WORKSPACE}/code"){
              bat 
                      }
                   }
               }
        stage ("Validate inputs "){
            steps {
                   bat 'C:\\Users\\VVelagani\\AppData\\Local\\Programs\\Python\\Python311\\python.exe validatedmanifestfile.py '
                  }
               }
        stage ("Request for new Build ID"){
            steps {
                  echo "${CUNumber}"
                 }
               }
        stage ("create buildID.zip"){
             steps {
                 echo "$artifacts_path"
                   }
               } 
        stage ("Replace/copy zip in artifactory storage "){
            steps {
                 echo "$gitcheckout_path"
                 }
               }
        stage ("Update builID with storage location"){
            steps {
                  echo "$manifestfile"
                 }
               }       
        }    
}