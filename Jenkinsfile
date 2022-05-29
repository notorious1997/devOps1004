properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/notorious1997/devOps1004.git"
    }
    stage("show files"){
        sh "ls -l"
    }
}
