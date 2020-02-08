# Retrieve a Wifi password from the command line

## MacOS

    $ security find-generic-password -wa SSID_OF_THE_WIFI

## Linux

    $ /system-connections/SSID_OF_THE_WIFI | grep psk=
