import warnings
from Block import Block
from Key import Key
from random import randbytes
from tqdm import tqdm
from threading import Thread

class AES :

    def __init__(self) :
        """
        Create a new AES object
        """
        
        self.blocks = None
        self.key = None

    # Static methods & Other =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            
    def SequenceToBlocks(sequence : bytearray) -> list:
        """
        Convert a sequence of bytes into multiple blocks
        return : Array of Block
        """
        # Divide the byte sequence in multiple blocks of 15 bytes
        nBlocks = len(sequence) // 16 if len(sequence)%16 == 0 else len(sequence) // 16 + 1

        blocks = []

        # Create new blocks from slices of 16 bytes
        for blockIndex in range(nBlocks):

            blocks.append(Block(sequence[blockIndex * 16 : (blockIndex + 1) * 16 ]))

        return blocks

    def BlocksToSequence(self) -> list:
        """
        Convert a block array to an array of bytes
        return : Sequence of bytes
        """
        sequence = []

        for block in self.blocks:

            # Get byte sequence from each block and add it to the sequence
            sequence.extend(block.BlockToSequence())

        return sequence

    def PrintSequence(sequence : bytearray):
        """
        Print an array of bytes using the hexadecimal format
        """

        print(" ".join([hex(x)[2:] if len(hex(x)) == 4 else "0" + hex(x)[2:]  for x in sequence]))

    # Instance methods =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    # <=-=-=-= Load the data =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def FromRandomByte(self, size : int):
        """
        Generate a random sequence of bytes with a specific size to be encrypted
        'size' - Size of the sequence to be encrypted
        """

        # Generate randoms bytes
        sequence = randbytes(size)

        # Create blocks from byte sequence
        self.blocks = AES.SequenceToBlocks(sequence)

        print("Randomly generated sequence :")
        AES.PrintSequence(sequence)

    def FromText(self, textSequence : str):
        """
        Convert the 'textSequence' to an array of bytes to be converted to blocks
        'textKey' - String to be converted and used as a key
        """

        # Convert characters to their byte equivalent
        byteSequence = [ord(x) for x in textSequence]

        # Convert the byte sequence to blocks
        self.blocks = AES.SequenceToBlocks(byteSequence)

        print("Byte sequence :")
        AES.PrintSequence(byteSequence)
        
    def FromFile(self, path):
        """
        Get the bytes from a file located at 'path' and convert it to blocks
        'path' - String to be used as a relative path to the file
        """

        # Open the file and get the byte arrays
        with open(path, "rb") as f:

            sequence = f.read()
            f.close()

        # Convert the sequence to blocks
        self.blocks = AES.SequenceToBlocks(sequence)
        
        print("Input file has been loaded from :")
        print(path)

    # <=-=-=-= Load the key =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    def UseRandomKey(self, size : int):
        """
        Generate a random sequence of bytes with a specific size to be used as a key
        'size' - Size of the sequence to be used as a key
        """

        if size not in [16, 24, 32]:

            raise ValueError("The key size is invalid and should be 16, 24 or 32 bytes")

        self.key = Key(randbytes(size))

        print("Randomly generated key :")
        AES.PrintSequence(self.key.key)

    def UseBytesKey(self, key : str):
        """
        Get the bytes to be used as a key
        'key' - Integer array to be used as a key
        """
        sequence = []

        for elt in key.split(" "):

            sequence.append(int(elt, base = 16))

        if len(sequence) not in [16, 24, 32]:

            raise ValueError("The key size is invalid and should be 16, 24 or 32 bytes")
        
        self.key = Key(sequence)

        print("Input key :")
        AES.PrintSequence(sequence)

    def UseTextKey(self, textKey : str):
        """
        Convert the 'textKey' to an array of bytes to be used as a key
        'textKey' - String to be converted and used as a key
        """

        byteKey = [ord(x) for x in textKey]

        if len(byteKey) < 16 :

            raise ValueError("Text used to generate a key is too short, should be >= 16")
        
        keySize = len(byteKey)
        
        # Cast the key into an array of bytes depending on it's length
        if keySize <= 24 :

            key = byteKey[:16]

        elif keySize <= 32 :

            key = byteKey[:24]

        else :

            key = byteKey[:32]

        self.key = Key(key)

        print("Input key :")
        AES.PrintSequence(self.key.key)

    # <=-=-=-= Export the data =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        
    def ToBytes(self):
        """
        Convert the blocks to bytes
        """

        # Get the sequence from blocks
        sequence = self.BlocksToSequence()

        print("Output byte sequence :")
        print(AES.PrintSequence(sequence))

    def ToText(self):
        """
        Convert the blocks to a text
        """

        # Get sequence from blocks
        sequence = self.BlocksToSequence()

        # Get the characters from their bytes equivalent
        text = "".join(chr(x) for x in sequence)

        print("Output text :")
        print(text)

    def ToFile(self, path):
        """
        Convert the blocks to a file
        'path' - String to be used as a path where the file will be created 
        """

        # Get bytes sequence from blocks
        sequence = self.BlocksToSequence()

        # Convert bytes sequence to a single byte array
        bytesSequence = bytes(list(sequence))

        # Write the bytesSequence to the file
        with open(path, "wb+") as f:

            f.write(bytesSequence)
            f.close()

        print("Output file has been created at :")
        print(path)

    # <=-=-=-= Encryption / Decryption =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def CipherBlock(self, block : Block, keySchedule : list):
        """
        Encrypt a block of 16 bytes using the AES using the key
        'block' - Block to by encrypted
        'keySchedule' - Pre-calculated key schedule
        """

        # Encrypt the block
        block.AddRoundKey(0, keySchedule)

        # Repetition depending on the key size (128 - 10 rep, 192 - 12 rep, 256 - 14 rep)
        for round in range(1, self.key.Nb):

            block.SubBytes()
            block.ShiftRows()
            block.MixColumns()
            block.AddRoundKey(round, keySchedule)

        block.SubBytes()
        block.ShiftRows()
        block.AddRoundKey(self.key.Nb, keySchedule)

        return block

    def Cipher(self):
        """
        Encrypt all blocks using the key        
        """

        nBlocks = len(self.blocks)

        keySchedule = self.key.KeyExpansion()

        encryptedBlocks = []

        # Iteration with progress bar 
        for blockIndex in tqdm(range(nBlocks), desc= "Encrypt blocks...") :

            # Encrypt a block
            encryptedBlocks.append(self.CipherBlock(self.blocks[blockIndex], keySchedule))

        self.blocks = encryptedBlocks


    def UnCipherBlock(self, block : Block, keySchedule : list):
        """
        Decrypt a block of 16 bytes using the AES using the key
        'block' - Block to be decrypted
        'keySchedule' - Pre-calculated key schedule
        """

        block.AddRoundKey(self.key.Nb, keySchedule)        

        # Reverse the encryption 
        for round in range(self.key.Nb - 1, 0, -1):

            block.InvShiftRows()
            block.InvSubBytes()
            block.AddRoundKey(round, keySchedule)
            block.InvMixColumns()
 
        block.InvShiftRows()
        block.InvSubBytes()
        block.AddRoundKey(0, keySchedule)

        return block

    def UnCipher(self):
        """
        Decrypt all blocks using the key
        """

        nBlocks = len(self.blocks)

        keySchedule = self.key.KeyExpansion()

        plainBlocks = []

        # Iteration with progress bar
        for blockIndex in tqdm(range(nBlocks), desc= "Decrypt blocks...") :

            # Decrypt a block
            plainBlocks.append(self.UnCipherBlock(self.blocks[blockIndex], keySchedule))

        self.blocks = plainBlocks
