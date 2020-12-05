# Pushing remote branches

To push a local branch (refactor) to the remote repo (origin) then use:

    git push -u origin refactor

The 'u' stands for 'upstream', another way of referring to remote

# Rebasing

A rebase base changes where the last base commit for your branch is.

If your branch_B has some changes, and the master has some changes, then a 3 way merge will happen as they have the same base commit (common ancestor). To tell git to use the latest version of master as the base for branch_B, and then be able to use a fast-forward merge, then use

    git checkout branch_b
    git rebase master

This will 'rewind' to the common ancestor, then playback all the changes on master onto branch_b. If there are any merge conflicts they can be resolved while keeping a 'linear history'.
Then, just merge in

    git checkout master
    git merge branch_b

Remember to delete the remote and local branch that was just merged

    git push --delete origin branch_b
    git branch -d branch_b

Then finally, push it all back into origin

    git push

### Continuing a rebase

If a merge is required after calling

    git rebase origin/master

Then you go into the files and treat it like a normal merge. When done though, run

    git add <conflicted_file>
    git rebase --continue

# Collaboration best practices

- Always synchronise branches before you start work
- Avoid having large changes which affect many things within a single commit
- Use feature branches
- Regularly merge changes made on the master branch back onto the feature branch
- Don't rebase changes that have already been pushed to remote repos