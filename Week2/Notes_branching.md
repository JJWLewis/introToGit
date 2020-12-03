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

## Merge conflicts

If you have overlapping commits, you'll get a merge conflict.

    git merge to_merge
    Auto-merging Week2/file_to_merge
    CONFLICT (content): Merge conflict in Week2/file_to_merge
    Automatic merge failed; fix conflicts and then commit the result.

Once you've resolved the conflict, save the file and add it again to mark the conflict as resolved

    All conflicts fixed but you are still merging.
    (use "git commit" to conclude merge)

## Fancier logs

It's easiest to see the commits in a graph. git cli can do this

    git log --graph --oneline

# Cheat sheet

| Command	| Explanation & Link |
| ---       | --- |
| git branch|	Used to manage branches |
| git branch <name> |	Creates the branch|
| git branch -d <name>|	Deletes the branch|
| git branch -D <name>|	Forcibly deletes the branch|
| git checkout <branch> |	Switches to a branch.|
| git checkout -b <branch>|	Creates a new branch and switches to it.|
| git merge <branch> |	Merge joins branches together. |
| git merge --abort|	If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action |
| git log --graph --oneline	|This shows a summarized view of the commit history for a repo.|