
keyword_dictionary = {
    "LAN": "Local Area Network",
    "WAN": "Wide Area Network",
    "NIC": "Network Interface Card",
    "WAP": "Wireless Access Point",
    "Internet": "The biggest network in the world",
    "TCP": "Transmission Control Protocol",
    "IP": "Internet Protocol",
    "HTTP": "Hypertext Transfer Protocol",
    "HTTPS": "Hypertext Transfer Protocol Secure",
    "FTP": "File Transfer Protocol",
    "DNS": "Domain Name System",
    "VPN": "Virtual Private Network",
    "MAC": "Media Access Control",
    "NAT": "Network Address Translation",
    "DHCP": "Dynamic Host Configuration Protocol",
    "SMTP": "Simple Mail Transfer Protocol",
    "POP": "Post Office Protocol",
    "IMAP": "Internet Message Access Protocol",
    "SSL": "Secure Sockets Layer",
}
keyword_input = str(input("Put in Keyword: "))
for x, y in keyword_dictionary.items():
    if keyword_input == x:
        print(x,":", y)

