# macOS Boot Option Cheatsheet

## macOS Boot Options

### Start you Mac in Safe Mode

`Shift`: Since safe mode only loads essential software, you can determine whether a system process or a user-installed application is causing your problem.

### Boot into Startup Manager

`Option`: From here you can select different startup disks if any bootable partitions are available.

### Boot into Recovery Mode

`Command + R`: Recovery Mode is macOS's powerful recovery suite with a bunch of options for saving or wiping your Mac. You can use it to reinstall macOS, restore from a Time Machine backup or use Disk Utility to repair or format your hard drive.

### Start in Internet Recovery Mode

`Shift + Command + Option + R`: Skipping your system's hard drive. This allows you to reinstall the build of macOS that came with your computer from the factory. macOS might do this one on its own if your installation is so messed up that you can't boot into Recovery Mode.

### Start in single user, command-line-only mode

`Command + S`: This is useful for running diagnostic Terminal commands or `fsck`, but it can't do much beyond that.

### Boot in verbose mode

`Command + V`: This mode displays logging and diagnostic messages as your Mac boots. If your Mac is showing the Apple logo but failing to start completely, try this step to see where in the boot process the error occurs.

## Reset Commands

### Reset your Mac's NVRAM or PRAM

`Command + Option + P + R`: This small memory module stores certain settings essential to your Mac's operation, and resetting is a good first step when you're trying to resolve tricky hardware issues. Hold down the key combo immediately after pressing your Mac's power button. Then release the keys after about twenty seconds. During the reset process it might seem like your Mac is restarting before starting up normally.

### Reset the SMC on an Apple laptop

`Shift + Control + Option + Power`: The SMC, or System Management Controller, is responsible for low-level hardware functionality like fan speed, battery charging and sleep routines. To perform the reset, hold down the Shift, Control and Option keys on the _left_ side of the built-in keyboard, then press the power button at the same time. Hold the modifier keys and power button down for ten seconds, then release all the keys and start the computer normally. For Apple desktops you can reset the SMC by disconnecting the power cable and all peripherals for fifteen seconds.

## Legacy Commands

### Start up from a CD, DVD or USB thumb drive

`C`: Start from a device that contains a valid Mac operating system.

### Start up in Target Disk mode

`T`: This command makes the computer it was executed on behave like a hard drive, allowing you to pull data off of it with another Mac. If you absolutely cannot save your computer, sometimes you can save the data with Target Disk Mode. The target computer must be connected with a Firewire, Thunderbolt or USB-C cable.

### Eject a CD or DVD from the optical disc drive

`Eject, Mouse button, Trackpad button or F12`: Eject a CD or DVD from the optical disc drive

## Force the system to boot from your macOS startup disk

`X`:Force the system to boot from your macOS startup disk

## Advanced Commands

### Start up in diagnostic mode

`D`: launching Apple Diagnostics. On pre-June 2013 Macs, this command launches the analogous Apple Hardware Test.

### Start the appropriate diagnostic utility over the Internet

`Option + D`: bypassing your computer's internal storage system.

### Start from a compatible NetBoot server

`N`: if there is one available.

### Boot from the default boot image on a compatible NetBoot server

`Option + N`
