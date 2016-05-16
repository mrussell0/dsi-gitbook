# Terminal Cheatsheet

### Navigation
- ```pwd``` print working directory (where am I?)
- ```ls``` list files in current directory (what is here?)
- ```cd``` go to home directory.
- ```cd ..``` goes up a level in the directory hierarchy.
- ```cd ../..``` go up two directories
- ```cd folder``` go into that folder

### Making/Removing Files and Folders
- ```mkdir folder``` create a folder
- ```rmdir folder``` deletes an empty directory.
- ```rm -rf folder``` deletes folder and all files in that folder
- ```rm file-name``` deletes a file
- ```touch file-name``` creates a file

### Moving and Copying
- ```mv file-name new-file-name``` rename a file
- ```mv file-name folder-name/file-name``` put a file into a subfolder
- ```cp file-name new-file-name``` copy a file
- ```cp -R folder new-folder``` copy a folder

### Traversing the Filesystem using `..`
- You can traverse the filesystem using `..` to move to a parent folder.
- If I’m in `~/Documents`, I can move to `~/Downloads` using the following command: `cd ../Downloads`.
- Use tab-completion to feel your way around the terminal when using that.
- The `/` helps denote that you mean you’re moving into a parent folder.


### Editing
- ```atom .``` in the folder that has the files you wish to edit

### Get Out of There
- ```exit``` exit the terminal
