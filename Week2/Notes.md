# Advanced git

## Skipping the staging area

    git commit -a

A shortcut to stage any changes to tracked files and commit them in one step

If a modified file has never been added, then it won't be added

## Detailed change information

git log is useful for seeing a general history, what what if you need to see the actual changes within each of those commits? Use the -p (from the patch command, from week 1) to see the extra detail

    git log -p

To look at a specific commit, you can use the commit id and git show

    git show 393ba3fccf02f791e4745273fd27a9b0acba78fb

To check how head differs from your current staged directory

    git diff --staged

## .gitignore

When you need to ignore a file, either a default of a local passwords file, create a .gitignore file within the repo

    touch ignoreme.txt
    echo ignoreme.txt > .gitignore
    git add .gitignore

# Cheat sheet

| Command |	Explanation & Link|
| ---     | ---     |
| git commit -a	    |Stages files automatically|
| git log -p	    |Produces patch text|
| git show	        |Shows various objects|
| git diff    	    |Is similar to the Linux `diff` command, and can show the differences in various commits|
| git diff --staged	|An alias to --cached, this will show all staged files compared to the named commit|
| git add -p	    |Allows a user to interactively review patches to add to the current commit|
| git mv	        |Similar to the Linux `mv` command, this moves a file|
| git rm	        |Similar to the Linux `rm` command, this deletes, or removes a file|

# Undoing things

## Revert unstaged changes

If you've made changes that you want to get rid of, just checkout over the top of your local copy

    git checkout file.txt

## Revert staged changes

