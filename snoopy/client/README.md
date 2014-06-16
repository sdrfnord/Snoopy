# Snoopy client script

This is the Snoopy client side script. It handles launching of the two main components:

1. The Rogue Access Point
2. The probe sniffer

# 1. Snoopy rogue access point component

The rogue AP does the following:

1. Brings up a VPN connection to our Snoopy server
2. Loads injection drivers
3. Brings up a [promiscuous] rogue access point
4. Starts a DHCP server

Notes:

a. DHCP is handled locally, but the DNS is set to the Snoopy server.
   This allows us to do 'bad things' with DNS at a central point.
b. The DHCP lease file is uploaded, and inserted into the Snoopy server.
c. OpenVPN can operate in tunnel mode (layer3) or bridged mode (layer2).
   Bridged mode could be used to put all drones on the same subnet, we'd
   then be able to capture layer2 traffic on the Snoopy server.
   However, in tests, this proved to be too much data over 3G.

TODO: -Get dhcp_relay working on the N900 such that we can run a
the DHCP daemon service on the Snoopy server.
      -Add more security to the rsync process.
      -Add watchdog to ensure everything is running properly

# Snoopy Probe Sniffer component

The probe sniffer component does the following:

1. Enables monitor mode on the interface
2. Captures probe requets, and log them to file
3. Rsync uploads this data every N seconds, where it is popuated into our database

