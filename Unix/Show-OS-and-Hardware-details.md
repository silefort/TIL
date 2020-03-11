# Show OS and Hardware details on Linux

Some commands may not work on non linux OS ( MacOS)


## Display basic OS Information

    $ uname
    $ uname -s (kernel name)
    $ uname -r (kernel release)
    $ uname -v (kernel linux version)
    $ uname -n (hostname - Network Node Hostname)
    $ uname -m (Machine Hardware Architecture: i386, x86_64, etc.)
    $ uname -p (processor type)
    $ uname -i (hardware plateforme)
    $ uname -o (operating system informations)
    $ uname -a (display all info)

## Display Hardware Information


    $ sudo lshw (Hardware Information)
    $ sudo lshw -short (Résumé des infos)
    $ sudo lshw -html > hardwareinfo.html (créer une page HTML des résultats)

## Display CPU Information

    $ lscpu

## Display Disks Information

    $ lsblk
    $ lsblk -a (informations encore plus détaillées - loop devices)

## Display USB Devices Information

    $ lsusb
    $ lsusb -v (informations encore plus détaillées : "verbose")

## Display PCI Devices Information

    $ lspci (lspci --help pour voir toutes les options)

## Display SCSI Devices Information

    $ lsscsi (vous devrez peut-être installer : sudo apt install lsscsi)

## Display SATA Devices Information

    $ sudo hdparm [devicelocation] ==> exemple : $ sudo hdparm /dev/sda1
