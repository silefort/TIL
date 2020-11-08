# Tar Cheatsheet

## Create a tar backup

    $ tar -cvf backup.tar /home/user
    $ tar -cvfz backup.tar.gz /home/user # with gzip

## Extract content from a tar

    $ tar -xvfz backup.tar.gz /backup/directory/file.txt

## List content of a tar 

    $ tar -ztvf backup.tar.gz
