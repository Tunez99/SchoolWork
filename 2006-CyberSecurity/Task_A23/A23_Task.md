A23 Enhance the cybersecurity at your home.

In this section I want to dive deeper into the importance of network security. Using my own wifi as an example to concepts and applied methods to protect privacy. We will achieve this through analysing and monitoring of the wifi network. Through this I hope to highlight some security concepts and mitigate risk.  

The first thing you can do to improve your wifi network. 

netstat -rn | grep default

you can use this following command to find your access point then log in through http://[ipaddress]

Now, according to the IBM, 86% of routers never have their default password changed. This allows some basic attacks to brute force and gain access to the wifi. Simply changing this to a strong passphrase is a great way to improve security. 

https://www.ibm.com/think/insights/router-reality-check-86-percent-default-passwords-have-never-been-changed

We can also change our SSID, make sure not to include any personal info as it will be public to view. 

Just these 2 changes can greatly increase security. By simply changing the password to a strong 10 character password. With a mix of characters, can make it computationally infeasible to guess the password. 

While some simple fixes can help improve security, another form of access comes from the end point. Some examples can be to keep firmware up-to-date. When vulnerabilities are found, patches will roll out to help protect you. This makes it harder for threats to access your information. 

This is something i've continued to practice, however, i want to bring to light a vulnerability I found on my computer.

Over time, i have used this computer to travel and connect to various WIFIs, including some public ones and some I don't know. 

Using the command:
networksetup -listpreferredwirelessnetworks en0

I am able to list the various networks my device keeps preffered. This is a risk. I want to especially draw attention to the public WIFIs. If a threat is present on a public wifi, my device would automatically join it. Through this method, a treat could try to access information or install a virus to my device compromising my home network in the future. 

So in light of this discovery i have decided to clean up this list and remove unwanted networks. A simple bash script will suffice for this. Keep in mind this will be a quick script based on MacOS and I will not be making cross platformed as of this moment. It is recommended to use at your own discretion. 

In conclusion to this, i would like to highlight how this discovery applies has improved my security.

Access control - controlled connection to networks
Authentication - Through approving network connections
Endpoint control - Ensure my device is protected from harmful connections.
Threat Reduction - Reduce the "attack surface" so old, potentially unsafe connections arn't made. 

Through mitigation i have protected my device and current networks against potential threats.

