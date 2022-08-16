# **HOST SCANNER**
Enumerates and logs hosts on a network. ARP-Based.
Linux or Windows.



----------
**ARGUMENTS**
----------

1- *-a or --address=*
Input the IP Address you want to check the presence on network.

If you use it with a CIDR Notation, like 192.168.0.1/24, then all the network will be scanned.


2- *-s or --singlerun=*
If you use -s, the software will run once. 

If you don't use -s, the software will scan for new hosts in real time.



3- *-l or --log=*
If you use -l, input a filename to be created with the output logs

If you don't use -l, no logs are created


------------------
**FEATURES**
------------------

1- Real-time Scan

2- One-time Scan

3- MacVendor Lookup

4- Can create logs with the output

5- Error if a non IPv4 is inputted.

--------------------------
**LEGACY_HOSTSCAN.PY**
---------------------------
1- The real-time scan of this version doesn't update IPs that leave the network, it only updates new hosts.
(Also the output isnt as clean because this version doesnt use a function to clear terminal)

Useful if you don't want to miss the IPs/MACs that leave the network.


------------------
IMPROVEMENTS
------------------

1- Fancier Output 



----------------------
REQUIREMENTS
-----------------
pip install mac_vendor_lookup 

