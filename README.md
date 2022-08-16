# host-scanner
Enumerates hosts on a network. ARP-Based.
Linux or Windows.

----------

ARGUMENTS

----------

-a or --address= 
Input the IP Address you want to check the presence on network.
If you use it with a CIDR Notation, like 192.168.0.1/24, then all the network will be scanned.


-s or --singlerun= 
If you use -s, the software will run once. 
If you don't use -s, the software will scan for new hosts in real time.


------------------
FEATURES
------------------

1- Real-time Scan
2- One-time Scan
3- MacVendor Lookup
4- Error if a non IPv4 is inputed.
5 ( FUTURE IMPROVEMENT) - Fancy Output in Terminal


----------------------
REQUIREMENTS
-----------------
pip install mac_vendor_lookup 

