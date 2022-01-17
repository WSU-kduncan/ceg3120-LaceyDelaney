Status: Shows status of the local repository. The status includes...
- number of local commits that have not been synced with remote (GitHub)
- list of files in local folder than are NOT being tracked by git 
-list of files in local folder that have changes that need to be committed. 
Command: git status 

Clone: This command is used to copy a repository to a system that you are using.  
Command: git clone <URL>

add: is used to add any new or modified files to an index. 
Command: git add <filename> 

rm: remove a file 
Command: rm <filename> 

commit: is used to save changes that are made in your repository. 
Command: git commit -m "Some meaningful comments" 

push: syncs commits with remote (GitHub)
Command: git push 
fetch: The git fetch command downloads commits, files, and refs from a remote repository into your local repo. 
Command: git fecth <remote> || git fetch <remote> <branch> 

merge: lets you take independent lines of development created by git branch and integrate them into a single branch.
Command: git merge 

pull: is used to fetch and download content from a remote repository and immediatley update the local to match. 
Command: git pull <remote> 

branch: list all branches 
Command: git branch 

checkout: lets you navigate between the branches created by git branch. 
Command: git checkout <branch name>

.GIT FOLDER 
hooks- this folder contains script files. Git hooks are the scripts that are executed before or after events like commit, push, etc.

objects: This folder represents an obkect database of Git.

config: This is the local configuration file. 

refs: This folder stores information about tags and branches. 

HEAD: This file stores reference to the current branch. It points to the master branch by default. 

index: This is a binary file and stores staging information. 

.GITIGNORE FILE 

- File that holds list of files / directories you want ignored
- git status will no longer show these as files to be added. 
- is used to exclude libraries files that need to be built per system, keep excess and secrets off Github. 

GITHUB

pull requests: Forum like interface on GitHub where you can request changes to be merged. 
Command: git pull
- fetch (content from remote) and merge it into your local repo copy.

ssh authentication to repositories steps
1. ssh-keygen -t ed25519 -C "your_email@example.com"
2. .ssh
3. .ssh/authorized keys : List of PUBLIC keys 
4. .ssh/known_hosts : first connection requres identity signature
5. .ssh/config way to manage keys & create "aliases" 
6. Need to copy key into github settings. 


