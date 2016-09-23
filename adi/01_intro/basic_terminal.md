# Basic Terminal and Navigating the File System

## File system structure
- Explore navigation commands
    - `cd`, `ls`, `pwd`
    - Names are case sensitive!
- Explore file/dir create/read/write commands
    - `mkdir`, `touch`, `echo`, `cat`, `rm`, `rmdir`
- Relative vs. Absolute paths

## Permissions
Permissions on POSIX systems are split into User, Group, and Other. The file’s owner usually has the most liberal permissions to do anything they like with the file while the group and others have less permissions.

Run `ls -l` to view a listing of files with permissions in the terminal. Permissions are listed like so:

`--- --- ---`

`— — —` in 3 stanzas. The first stanza is the owner then the group, then everyone else. Permissions are Read (r), Write (w), and Execute (w). Each stanza lists which of these actions each user type can perform.

# Creating and Moving Files Using the Terminal

## Learning Objectives

- Rename files and folders
- Move and copy files/folders
- Delete files and folders
- Create files in at least 2 ways

## Create a File

- `touch` command: Creates a new empty file
- `echo` command: Outputs any string of text to the terminal, can be redirected into a new or existing file using `>` or `>>` operators

## Moving Files and Folders

- Create a file, create a folder: `touch` and `mkdir`
- Change permission to a different user: `chown`

## Deleting Data

Using the `rm`, `rm -rf`, and `rmdir` commands to...

- Delete Files
- Delete Folders
- Delete recusively (and with *force*)

__Group Exercise__

Create a folder called “Zoo” on your system. Within the zoo we’ll have cages (folders) for each animal (file). Create the following cages for these animals within the zoo folder:

- Zoo
    - Horses
        - Zebra
        - Horse
        - Giraffe
    - Big Cats
        - Puma
        - Leopard
        - Donkey

__ Individual Exercise: File System Zoo__

Some of the animals are in cages they shouldn’t be in! Move the donkey where it’ll be safe. It’s your job to create a new cage for each animal in their group if needed.