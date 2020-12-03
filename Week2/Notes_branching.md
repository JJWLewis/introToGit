# Branching and Merging

##  Branch basics

See what branches are on the tree

    git branch

Make a new branch 

    git branch branch_name

Switch to the new branch

    git checkout branch_name

To do the above in one step: make a branch and switch to it:

    git checkout -b branch_name

## Delete a branch

To delete a branch (which has no unmerged changes) then use 

    git branch -d branch_name

# Merging

## Merging from branch to master

Checkout the master branch, then type

    git merge merge_branch_name

