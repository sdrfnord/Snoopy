#!/bin/bash
# glenn@sensepost.com 
# Snoopy // 2012
# By using this code you agree to abide by the supplied LICENSE.txt


echo "+-----------------------------------------------------------------------+
+ SensePost Information Security					+
+ Snoopy Drone Installer						+
+ http://www.sensepost.com/labs / research@sensepost.com                +
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
+ This script has been tested on a BackTrack5 installation. I'll try	+
+ install the following packages anway:					+
+ -dnsmasq, tshark, openvpn, rsync, netcat, macchanger, psmisc, iptables+
+  aircrack-ng                                                          +
+-----------------------------------------------------------------------+
"

#Set current path in config
sd=$(cd $(dirname "$0"); pwd)

apt-get install -y dnsmasq tshark openvpn rsync netcat macchanger aircrack-ng psmisc traceroute iptables

/etc/init.d/ssh start

cat > /usr/bin/snoopy << EOL
#!/bin/bash
$sd/snoopy.sh
EOL
chmod +x /usr/bin/snoopy

echo "+-----------------------------------------------------------------------------+"
echo "+ Done. Run 'snoopy' now.  					 	    +"
echo "+-----------------------------------------------------------------------------+"


