keyword_dictionary = {
    "LAN": "Local Area Network - covers a small geographical area",
    "WAN": "Wide Area Network - covers a large geographical area",
    "BANDWIDTH": "Amount of data that can be transmitted in a given time",
    "NIC": "Allows devices to wirelessly connect built into the motherboard",
    "SWITCH": "Recieves and transmits data between different devices using MAC address",
    "TRANSMISSION MEDIA": "Wired or wireless connection allow transmission between devices",
    "WAP": "Allow devices to connect to a network wirelessly, similar to a switch",
    "ROUTER": "Transmits data between different networks using 'packets'",
    "TWISTED PAIR": "Twisted sopper wires together in 4's to reduce internal interferance",
    "COAXIAL": "A single copper wire surronded by plastic insultaion and metallic mesh to shield from external interferance",
    "FIBRE OPTIC": "Transmits data using light, can be sent over very large distances, little interferance, good performance but costly",
    "BLUETOOTH": "Direct connection between 2 devices, low bandwidth, range of 10m",
    "WIFI": "Can connect many devices together to a LAN at once, high bandwidth, range of 40-100m",
    "WIRED NETWORKS": "Faster and more reliable than wireless",
    "WIRELESS NETWORKS": "Slower and lss reliable that wired",
    "COMPRESSION": "Used to reduce the size of files benefiting storage space and read times",
    "DEFRAGMENTAION": "To group all fragments of the same files together and the free space together to increase read and write times",
    "ENCRYPTION": "Encrypts data to stop third parties from accessing it, needs a key to decrypt it",
    "USER MANAGEMENT": "Restricts access to system using user accounts and passwords",
    "FILE MANAGEMENT" : "Manages where files are located - Moves,deletes,creates folders for files",
    "MEMORY MANAGEMENT" : "moves application data to main memory when is use",
    "PERIPHERAL MANAGEMENT" : "Manages the devices that connect via the ports",
    "SECONDARY STORAGE" : "Non-volaite memory where data is stored when not in use",
    "MAIN MEMORY" : "Volaite memory where data is stored when in use",
    "HDD" : "Hard disk drive - high capcity but easily damaged by impacts",
    "SSD" : "Solid state drive - high capcity, quick read/write speed and shock resistant",
    "OPTICAL DISC" : "Low capacity and easily scratched",
    "MAGNETIC TAPE" : "Very high capacity but damaged very easily by imapcts, heat, magnets",
    "MEMORY CARD" : "Low capacity but shock resitant",
    "INTERNAL STORAGE" : "Storage within the computer",
    "EXTERNAL STORAGE" : "Storage outside the computer",
    "UTILITY SOFTWARE" : "Software that aids in runnig the computer",
    "USER INTERFACE" : "Provides a way to communicate with the computer -GUI/CLI",
    "VON NEUMAN ARCHITECTURE" : "CU, ALU, registers and instructions and data stored in the same memory",
    "CPU" : "Brain of the computer",
    "ALU" : "Preforms all mathematical and logical operations",
    "PC" : "Increments and points to the next instruction to be executed",
    "MAR" : "Holds the address of the next instruction to be executed",
    "MDR" : "Holds the data of the next instruction to be executed",
    "ACCUMALATOR" : "Holds the result of the mathematical and logic operations preformed by the ALU",
    "FETCH-EXECUTE CYCLE" : "The process of which instructions are executed and the computer runs",
    "RAM" : "Random Access Memory - Volatile memory that stores application data in use",
    "ROM" : "Read Only Memory - stores the BIOS and bootloader",
    "GUI" : "Graphical user interface - Uses WIMPs to provide a way for the user to communicate with the computer",
    "CLI" : "Command line interface - Uses text and commands to provide a way for the user to communicate with the computer",
    "VOLATILE" : "Loses data when device is turned off",
    "NON-VOLATILE" : "Retains data when device is turned off"
}
while True:
    keyword_input = str(input("Put in Keyword: "))
    for x, y in keyword_dictionary.items():
        if keyword_input.upper() == x:
            print(x,":", y)
        elif keyword_input.upper() != x:
            print("STUPID!?!?!?")
            break
    if keyword_input.lower() == 'no':
        break
    