import getpass

def print_banner():
    banner = f"""
    hey {getpass.getuser()}

                                                v1.0
     
                               _ _               _   
                              | (_)             | |  
   ___  _ __   ___ _ __     __| |_ _ __ ___  ___| |_ 
  / _ \| '_ \ / _ \ '_ \   / _` | | '__/ _ \/ __| __|
 | (_) | |_) |  __/ | | | | (_| | | | |  __/ (__| |_ 
  \___/| .__/ \___|_| |_|  \__,_|_|_|  \___|\___|\__|
       | |                                           
       |_|                    😎😎 Praveen Kumar 😎😎             
 

    $toolname.py [options]

    usage: toolname.py [options]

    Options:
    -h, --help         help menu
    -u, --url          URL to scan
    -i, --input        <filename> read input from txt
    -o, --output       <filename> write output to file
    -b, --blog         read about the bug
"""
    print(banner)

