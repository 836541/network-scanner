#!/usr/bin/python3

# /undead_warlock
# GPL3.0-or-foward

from mac_vendor_lookup import MacLookup
import scapy.all as scapy 
import optparse 
import re 

def arguments():               # optparse arguments 
    singlerun = "singlerun"
    address   = "address"
    log       = "log"

    parser = optparse.OptionParser() 
    parser.add_option("-a", "--address", dest= address, help= "Target's IPV4 Address. Use CIDR for full network scan.")
    parser.add_option("-s", "--singlerun", dest= singlerun, action= "store_true", default= False, help= "True: One-time Scan | False: Real-time Scan")
    parser.add_option("-l", "--log", dest= log, default= False, help= "If used, input a filename to be created with logs")
    (inputs, args) = parser.parse_args()

    if not inputs.address:
        parser.error("\n[X] PLEASE INPUT AN IPV4 ADDRESS")

    return (inputs.singlerun, inputs.address, inputs.log)



def checkAddress(ipaddress):          # validating user's input
    def printQuit(): 
        print()
        print("[X] Invalid IP Address")
        quit() 
        
        return 0
    
    def regexAddress(ipaddress, NOT_CIDR= None):
        if NOT_CIDR: 
            address_numbers = re.findall(r"(([0-9]{1,3})[\.]?)", ipaddress) 
  
        else: 
            address_numbers = re.findall(r"(([0-9]{1,3})[\.\/])", ipaddress)

        numbers = [int(value[1]) for value in address_numbers] 
        
        return numbers 

    numbers = regexAddress(ipaddress)
    if len(numbers) == 3: 
        numbers = regexAddress(ipaddress, True)

    if len(numbers) != 4:        # Checking if ipaddress has 4 octets
        printQuit() 
        
    for number in numbers:       # Checking if a octet value is higher than 255.
        if number > 255:
            printQuit() 

    return 1 


def arpRequest(Address):
    arp_request       = scapy.ARP(pdst= Address)               # ARP Request for one/multiple IPs.
    ethernet_request  = scapy.Ether(dst= "ff:ff:ff:ff:ff:ff")  # Ethernet request for Broadcast's MAC.
    arp_ether_request = ethernet_request/arp_request           # ARP Request through MAC's Broadcast Address.
    
    return arp_ether_request 


def printOutput(singlerun, arp_ether_request, log):
    print("\nIPv4\t\tMAC Address\t\thwlen\tplen\tMAC Vendor")
    print("--"*38)
    already_printed = list() 

    loop = 1 
    while loop:
        answered_request = scapy.srp(arp_ether_request, timeout= 1, verbose= False)[0]
        

        for element in answered_request:
            if [element[1].psrc, element[1].hwsrc] in already_printed: 
                continue 

            already_printed.append([element[1].psrc, element[1].hwsrc]) 

            try :
                MacVendor = MacLookup().lookup(element[1].hwsrc)
            except:
                MacVendor = "Unknown"

           
            print(f"{element[1].psrc}\t{element[1].hwsrc}\t{element[1].hwlen}\t{element[1].plen} \t{MacVendor}" )
            
            if log:
                if [element[1].psrc, element[1].hwsrc, MacVendor] not in already_logged:
                    with open(log, "a") as logfile:
                        logfile.write("%s,%s,%s \n"    %({element[1].psrc}, element[1].hwsrc, MacVendor))
                    already_logged.append([element[1].psrc, element[1].hwsrc, MacVendor])

        if singlerun: 
            loop = 0 

    return 1 


def main(): 
    singlerun, address = arguments() 
    checkAddress(address) 
    arp_ether_request = arpRequest(address)
    printOutput(singlerun, arp_ether_request, log)

main() 









