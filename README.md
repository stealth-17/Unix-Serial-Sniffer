This python script can be used to create a virtual device on your unix machine,
and this virtual device can be used to monitor the activities of serial communication
between any two devices

Format,

#python serial_sniffer.py <device file> <baudrate>

where device file can be like /dev/ttyUSB0,/dev/ttyUSB1,/dev/ttyACM0 etc

Above command will create a virtual device on your machine.
Output of above command will be,

"Configured to virtual device <some_name>"

Now all you have to do is communicate your data with the virtual device created as
if it is the real device.

Your communication data will be stored in file writelog.txt and readlog.txt

This script is useful when you want to communicate your device with a proprietary software.

Note: This script is not a clean professional code. So please let me know if there any suggestions

Note: This script is tested with Xbee device and Digi software to findout all AT commands
