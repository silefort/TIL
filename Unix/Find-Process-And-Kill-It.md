# Find a process by name and automatically kill it 

    $ PID=$(ps -ef | grep processName | grep -v grep | awk '{print $2'}); kill -9 $PID
