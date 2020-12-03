# Diff (the world before Git)

To use diff on the command line, just type

    diff -u file1 file2

## Generating diff files

When you need to send suggested changes to someone, it's easiest to send a diff. Once you've made the changes in a second file, create the diff by using:

    diff -u old_file new_file > change.diff

These are sometimes called patch files.

## Applying diff/patch files

To automatically apply a patch file

    patch old_file < patch_file

# Git basics

## git init

To create a repo in your current directory

    git init
This will make all the various files git needs within .git/

## git add

To add the latest modifications to tracked files to the staging area, use add

    git add file.txt

## git commit

To move a file from the git statging area into the git directory, you must commit

    git commit
This will open a new window in default editor to add a commit message. Easier to use
    git commit -m "commit message"

## removing files

If you delete a file from the repository, git add won't help. You need to remove that file from the watch

    git rm file.txt

