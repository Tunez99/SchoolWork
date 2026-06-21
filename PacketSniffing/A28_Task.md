A28 Implement a security solution of your choice and put it on your GitHub.

Packet Sniffer in python

I build a small python script to log basic live network traffic and save it to a file. This can be updated to include security features if need be. However, i've kept it as a small project so that analysis can be done. Similar to the functionality of wire shark, it's importance in detection is paramount.

Some details about the project include:
Capture; Source and Destination, the protocol used, source and destination of ports. A total packet tally, and a time stamp.

This information is printed in real time and also saved to a file for later analysis. 

To ensure data isn't leaks without the proper security in place, I only capture the headers of the packets and not the data.

Note: i run this in a python virtual enviroment and required libs must be installed via requirements.txt