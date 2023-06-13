const {data: comments} = await github.rest.issues.listComments({
    owner: context.repo.owner,
    repo: context.repo.repo,
    issue_number: '${{steps.get_issue_number.outputs.result}}',
  })

  const botComment = comments.find(comment => comment.user.id === 41898282)                                                                       
  const commentBody = "Hello from actions/github-script! (${{ github.sha }})"                  

    if (botComment) {
      await github.rest.issues.updateComment({
        owner: context.repo.owner,
        repo: context.repo.repo,
        comment_id: botComment.id,
        body: commentBody
      })
    } else {
      await github.rest.issues.createComment({
        owner: context.repo.owner,
        repo: context.repo.repo,
        issue_number: '${{steps.get_issue_number.outputs.result}}',
        body: commentBody
      })
    }
  
