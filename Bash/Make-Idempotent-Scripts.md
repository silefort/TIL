# Make Idempotent Bash Scripts

## Creating an empty file

    $ touch example.txt

## Creating a directory

    $ mkdir -p mydir

## Creating a symbolic link

    $ ln -sf source target

## Removing a file

    $ rm -f example.txt

## Modifying a file

```
    if ! grep -qF "/mnt/dev" /etc/fstab; then
    echo "/dev/sda1 /mnt/dev ext4 defaults 0 0" | sudo tee -a /etc/fstab
    fi
```
