import argparse
import sys, subprocess

sys.path.append("src")

from AES import *

if __name__ == "__main__" :

    AES_Instance = AES()

    parser = argparse.ArgumentParser(prog="AES")

    # Modes =====================================
    subParserMode = parser.add_argument_group("MODE", "Choose one of the following modes")
    subParserModeGroup = subParserMode.add_mutually_exclusive_group(required=True) 
    
    subParserModeGroup.add_argument('-T', help='Tests the tool', action='store_true')
    subParserModeGroup.add_argument('-E', help='Encrypt data using the information provided', action='store_true')
    subParserModeGroup.add_argument('-D', help='Decrypt data using the information provided', action='store_true')

    # Keys ======================================
    subParserKey = parser.add_argument_group("KEY", "Choose one of the following commands to insert the key")
    subParserKeyGroup = subParserKey.add_mutually_exclusive_group() 

    subParserKeyGroup.add_argument('-kr', '--key-random', type=int, help="Key from size out_file a randomly generated byte array (size >= 16)", metavar="size")
    subParserKeyGroup.add_argument('-kb', '--key-bytes', type=str,  help="Key from bytes in hexadecimal format", metavar="hex")
    subParserKeyGroup.add_argument('-kt', '--key-text', type=str, help="Key from text", metavar="text")

    # Data ======================================
    subParserData = parser.add_argument_group("DATA", "Choose one of the following commands to insert the data to be encrypted / decrypted")
    subParserDataGroup = subParserData.add_mutually_exclusive_group() 

    subParserDataGroup.add_argument('-dr', '--data-random', help="Data from size out_file a randomly generated byte array", type=int, metavar= "size")
    subParserDataGroup.add_argument('-dt', '--data-text', help="Data from text", type = str, metavar="text")
    subParserDataGroup.add_argument('-df', '--data-file', help="Data from file using a path", type = str, metavar="path")

    # Output ====================================
    subParserOut = parser.add_argument_group("OUTPUT", "Choose one of the following commands to output / save the result")
    subParserOutGroup = subParserOut.add_mutually_exclusive_group() 

    subParserOutGroup.add_argument('-ob', help="Output bytes", action='store_true')
    subParserOutGroup.add_argument('-ot', help="Output text", action='store_true')
    subParserOutGroup.add_argument('-of', '--out-file', help="Output file to a path", type = str, metavar="path")

    # Get the arguments as a list
    args = sys.argv[1:]
    
    # Print help if no arguments are passed
    if len(args) == 0:
    
        parser.print_help()
        sys.exit(0)

    # Parse the arguments
    else :

        parse = parser.parse_args(args)

    # Run test mode and exit
    if parse.T:

        subprocess.run(["python", "tests/unit_tests.py"])
        sys.exit(0)

    # Select key 
    if (parse.key_bytes and parse.key_text) \
            or (parse.key_random  and parse.key_text ) \
            or (parse.key_random  and parse.key_bytes ) :
        
        print("You can't have multiple keys use : --key_random or --key_bytes or --key_text")
        sys.exit(0)

    if (not(any([parse.key_bytes, parse.key_text, parse.key_random]))):
    
        print("You should insert a key using : --key_random or --key_bytes or --key_text")
        sys.exit(0)

    # Load the key value
    if parse.key_random  :

        AES_Instance.UseRandomKey(parse.key_random)
        
    elif parse.key_bytes  :

        AES_Instance.UseBytesKey(parse.key_bytes)
    
    elif parse.key_text  :

        AES_Instance.UseTextKey(parse.key_text)

    # Select data
    if (parse.data_text  and parse.data_random ) \
        or (parse.data_text  and parse.data_file ) \
        or (parse.data_file  and parse.data_random ) :
    
        print("You can't have multiple data inputs use : --data_random or --data_text or --data_file")
        sys.exit(0)

    if (not(any([parse.data_random, parse.data_text, parse.data_file]))):
    
        print("You should have a data input using : --data_random or --data_text or --data_file")
        sys.exit(0)

    # Load the data  
    if parse.data_random  :

        AES_Instance.FromRandomByte(parse.data_random)

    elif parse.data_text  :

        AES_Instance.FromText(parse.data_text)

    elif parse.data_file  :

        AES_Instance.FromFile(parse.data_file)

    # Run the selected mode
        
    if parse.E:

        AES_Instance.Cipher()

    elif parse.D:

        AES_Instance.UnCipher()

    # Select output 
    if (parse.ob and parse.ot ) \
        or (parse.ot and parse.out_file ) \
        or (parse.out_file and parse.ob ) :
    
        print("You can't have multiple data outputs use : -ob or -ot or --out_file")
        sys.exit(0)

    if (not(any([parse.ob, parse.ot, parse.out_file]))):
    
        print("You should have a data output using : -ob or -ot or --out_file")
        sys.exit(0)

    # Run output
        
    if parse.ob :

        AES_Instance.ToBytes()

    elif parse.ot :

        AES_Instance.ToText()

    elif parse.out_file  :

        AES_Instance.ToFile(parse.out_file)