from colorama import Fore

keyword_dictionary = {
    "LAN": "Local Area Network - covers a small geographical area and allows devices to communicate with each other within the same area.",
    "WAN": "Wide Area Network - covers a large geographical area and connects multiple LANs together.",
    "BANDWIDTH": "The maximum amount of data that can be transmitted in a given time.",
    "NIC": "Network Interface Card - a hardware component that allows devices to connect to a network.",
    "SWITCH": "A networking device that receives and transmits data between different devices using MAC addresses.",
    "TRANSMISSION MEDIA": "The physical medium through which data is transmitted, such as wired or wireless connections.",
    "WAP": "Wireless Access Point - a device that allows devices to connect to a wireless network.",
    "ROUTER": "A networking device that forwards data packets between different networks.",
    "TWISTED PAIR": "A type of cable that consists of pairs of twisted copper wires, used for Ethernet connections.",
    "COAXIAL": "A type of cable that consists of a single copper wire surrounded by plastic insulation and metallic mesh, used for cable TV and broadband internet connections.",
    "FIBRE OPTIC": "A type of cable that transmits data using light signals, providing high-speed and long-distance communication.",
    "BLUETOOTH": "A wireless technology that allows direct connections between two devices over short distances.",
    "WIFI": "A wireless technology that allows multiple devices to connect to a network simultaneously over a certain range.",
    "WIRED NETWORKS": "Networks that use physical cables for data transmission, offering faster and more reliable connections.",
    "WIRELESS NETWORKS": "Networks that use wireless signals for data transmission, offering convenience but with slower and less reliable connections compared to wired networks.",
    "COMPRESSION": "The process of reducing the size of files to save storage space and improve transfer speeds.",
    "DEFRAGMENTATION": "The process of organizing fragmented files on a storage device to improve read and write performance.",
    "ENCRYPTION": "The process of encoding data to protect it from unauthorized access, requiring a key to decrypt it.",
    "USER MANAGEMENT": "The practice of controlling and managing user access to a computer system through user accounts and passwords.",
    "FILE MANAGEMENT": "The process of organizing, manipulating, and controlling files on a computer system, including tasks like moving, deleting, and creating folders.",
    "MEMORY MANAGEMENT": "The process of allocating and managing computer memory resources to ensure efficient usage by applications.",
    "PERIPHERAL MANAGEMENT": "The management of devices connected to a computer system through ports, including tasks like installation, configuration, and troubleshooting.",
    "SECONDARY STORAGE": "Non-volatile memory used for long-term data storage when not in use, such as hard disk drives (HDDs) and solid-state drives (SSDs).",
    "MAIN MEMORY": "Volatile memory used for temporary storage of data and instructions that are actively being used by the computer.",
    "HDD": "Hard Disk Drive - a type of secondary storage device that uses rotating disks to store data.",
    "SSD": "Solid State Drive - a type of secondary storage device that uses flash memory to store data, offering faster read/write speeds and better durability compared to HDDs.",
    "OPTICAL DISC": "A storage medium that uses optical technology to read and write data, such as CDs and DVDs.",
    "MAGNETIC TAPE": "A storage medium that uses magnetic technology to store data, offering high capacity but slower access speeds compared to other storage devices.",
    "MEMORY CARD": "A small, portable storage device used in devices like cameras and smartphones to store data.",
    "INTERNAL STORAGE": "Storage located within the computer system, such as the hard drive or solid-state drive.",
    "EXTERNAL STORAGE": "Storage devices that are connected to the computer system externally, such as USB drives or network-attached storage (NAS) devices.",
    "UTILITY SOFTWARE": "Software programs that provide additional functionality and tools to assist in managing and maintaining a computer system.",
    "USER INTERFACE": "The means through which a user interacts with a computer system, such as a graphical user interface (GUI) or a command-line interface (CLI).",
    "VON NEUMANN ARCHITECTURE": "A computer architecture that uses a single memory to store both instructions and data, with a central processing unit (CPU) that fetches and executes instructions sequentially.",
    "CPU": "Central Processing Unit - the main component of a computer that performs most of the processing inside the computer.",
    "ALU": "Arithmetic Logic Unit - a component of the CPU that performs arithmetic and logical operations.",
    "PC": "Program Counter - a register that holds the address of the next instruction to be executed.",
    "MAR": "Memory Address Register - a register that holds the address of the next instruction or data to be fetched from or stored into memory.",
    "MDR": "Memory Data Register - a register that holds the data being fetched from or stored into memory.",
    "ACCUMULATOR": "A register that holds the result of arithmetic and logical operations performed by the ALU.",
    "FETCH-EXECUTE CYCLE": "The basic operation cycle of a computer, where instructions are fetched from memory, decoded, and executed.",
    "RAM": "Random Access Memory - volatile memory that stores data and instructions that are actively being used by the computer.",
    "ROM": "Read-Only Memory - non-volatile memory that stores permanent instructions, such as the BIOS and bootloader.",
    "GUI": "Graphical User Interface - a user interface that uses graphical elements, such as windows, icons, and menus, to interact with the computer.",
    "CLI": "Command-Line Interface - a user interface that uses text commands to interact with the computer.",
    "VOLATILE": "Data that is stored in memory and is lost when the power is turned off or the system is restarted.",
    "NON-VOLATILE": "Data that is stored in memory and is retained even when the power is turned off or the system is restarted.",
    "Internet": "A global network of interconnected computers and devices that communicate using standard protocols.",
    "TCP": "Transmission Control Protocol - a protocol that provides reliable, ordered, and error-checked delivery of data over IP networks.",
    "IP": "Internet Protocol - a protocol that defines the addressing scheme and routing of data packets on the Internet.",
    "HTTP": "Hypertext Transfer Protocol - a protocol used for transmitting hypertext documents on the World Wide Web.",
    "HTTPS": "Hypertext Transfer Protocol Secure - a secure version of HTTP that encrypts data transmitted between a web server and a client.",
    "FTP": "File Transfer Protocol - a protocol used for transferring files between a client and a server on a computer network.",
    "DNS": "Domain Name System - a system that translates domain names into IP addresses, enabling users to access websites using human-readable names.",
    "VPN": "Virtual Private Network - a secure network connection that allows users to access a private network over a public network.",
    "MAC": "Media Access Control - a unique identifier assigned to network interfaces for communication on a physical network.",
    "NAT": "Network Address Translation - a technique that allows multiple devices to share a single public IP address.",
    "DHCP": "Dynamic Host Configuration Protocol - a network protocol that automatically assigns IP addresses and other network configuration parameters to devices.",
    "SMTP": "Simple Mail Transfer Protocol - a protocol used for sending email messages between servers.",
    "POP": "Post Office Protocol - a protocol used for retrieving email messages from a mail server.",
    "IMAP": "Internet Message Access Protocol - a protocol used for retrieving and managing email messages on a mail server.",
    "SSL": "Secure Sockets Layer - a cryptographic protocol that provides secure communication over a computer network.",
}
while True:
    keyword_input = str(input(Fore.RESET + "Put in Keyword: "))
    #Lists all the elements in the dictionary
    if keyword_input.lower() == 'list':
        print("\n".join(keyword_dictionary))

    #Exits the program
    elif keyword_input.lower() == 'no':
        break

    #Checks if the keyword is in the dictionary and prints the definition if it is present.
    elif keyword_input.upper() in keyword_dictionary:
        print(Fore.RED + keyword_input.upper(), Fore.RESET,":", Fore.GREEN, keyword_dictionary[keyword_input.upper()])

    #Adds a new keyword to the dictionary if the input is add.
    elif keyword_input.lower() == 'add':
        new_keyword = str(input("Enter the new keyword: "))
        new_definition = str(input("Enter the definition of the new keyword: "))
        keyword_dictionary[new_keyword.upper()] = new_definition
        print("Keyword added to the dictionary")
    else:
        print(Fore.LIGHTCYAN_EX + "Enter a valid keyword or 'no' to exit.\nIf you wish to see the list of keywords, type 'list'.\nIf you wish to add a new keyword, type 'add'.")