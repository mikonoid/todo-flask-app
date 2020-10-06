pipeline {
    environment {
    registry = "mk51/todo"
    registryCredential = 'docker_hub_login'
    prod_ip = ''
  }
    agent any
    stages {

    stage('Checkout') {
      steps {
         git (url: 'https://github.com/mikonoid/todo-flask-app')

        }
    }
    stage('Building docker Image') {
      steps{
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }

    stage('Deploy docker Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }

    stage('DeployToProduction') {
      steps {
      input 'Deploy to Production?'
          milestone(1)
          withCredentials([usernamePassword(credentialsId: 'webserver_login', usernameVariable: 'USERNAME', passwordVariable: 'USERPASS')]) {
              script {
                 sh "sshpass -p '$USERPASS' -v ssh -o StrictHostKeyChecking=no $USERNAME@$prod_ip \"docker pull mk51/todo:${env.BUILD_NUMBER}\""
                 try {
                     sh "sshpass -p '$USERPASS' -v ssh -o StrictHostKeyChecking=no $USERNAME@$prod_ip \"docker stop todo\""
                     sh "sshpass -p '$USERPASS' -v ssh -o StrictHostKeyChecking=no $USERNAME@$prod_ip \"docker rm todo\""
                 } catch (err) {
                     echo: 'caught error: $err'
                   }
                     sh "sshpass -p '$USERPASS' -v ssh -o StrictHostKeyChecking=no $USERNAME@$prod_ip \"docker run --restart always --name todo -p 80:5000 -d mk51/todo:${env.BUILD_NUMBER}\""
                 }
             }
         }
     }
  }
}
