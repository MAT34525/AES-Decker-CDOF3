from Block import Block

class Key :

    def __init__(self, key : bytearray):
        """
        Create a key object from a sequence of bytes
        'key' - Key sequence of bytes, should be 16, 24 or 32 bytes
        """

        if len(key) not in [16, 24, 32]:

            raise ValueError("The key size is invalid and should be 16, 24 or 32 bytes")

        self.key = key

        self.Nk = len(self.key) // 4 # Number of bytes regrouped in words of 4 bytes

        self.Nr = 6 + self.Nk # Number of rounds for the cipher algorithm

        self.Nb = 4

    # Static methods =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    def SubWord(word : list) -> list:
        """
        Replace all values in the word using a S-Box
        'word' - Integer array representing the word to be substituted
        return : Integer array containing the substituted word
        """

        SBOX = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'], 
                ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'], 
                ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'], 
                ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'], 
                ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'], 
                ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'], 
                ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'], 
                ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'], 
                ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'], 
                ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'], 
                ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'], 
                ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'], 
                ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'], 
                ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'], 
                ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'], 
                ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]

        newWord = []

        for byteIndex in range(len(word)):

            # Get the substitution value using the S - Box

            val = word[byteIndex]

            valx = val >> 4             # Get the 4 MSB as x axis for the lookup table 
            valy = val ^ (valx << 4)    # Get the 4 LSB as y axis for the lookup table 

            newWord.append(int(SBOX[valx][valy], 16))

        return newWord

    def RotWord(array : list) -> list:
        """
        Apply a signle rotation to the left on an array 
        'array' - Integer array to be rotated
        return : Integer array after the rotation
        """

        shiftedArray = []
        m = len(array)

        for item in range(m):

            # Displace the last elements to the begining of the array
            if item < m - 1:

                shiftedArray.append(array[item + 1])

            # Displace the first element to the end of array
            else :

                shiftedArray.append(array[(item + 1)%m ])

        return shiftedArray

    def Rcon(pow: int) -> list:
        """
        Compute the rcon value from a specific power : {02}^(pow - 1) {00} {00} {00}
        'pow' - Integer for the power raise
        return : Integer array containign the rcon value
        """

        initVal = 2
        val = initVal

        # Specific case where the power is 0
        if pow == 0 :
            val = 1
        
        else :

            # Compute {02}^(pow - 1)
            for _ in range(pow - 1):

                val *= initVal

        # Cast result in field GF(2**8)
        modVal = Block.ModuloBytes(val)

        return [ modVal , 0, 0, 0]

    def XORarrays(array1 : list, array2 : list) -> list:
        """
        Term to term XORing of elements in two arrays
        'array1' - First integer array
        'array2' - Second integer array
        return : The resulting array after the XOR of 'array1' and 'array2'         
        """

        if len(array1) - len(array2) != 0 :

            raise ValueError(f"The two arrays must be the same length : {len(array1)} != {len(array2)}")

        arrayXOR = []

        # Term to term XOR
        for i in range(len(array1)):

            arrayXOR.append(array1[i] ^ array2[i])

        return arrayXOR
    
    # Instance methods =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def KeyExpansion(self):
        """
        Key expansion algorithm, generates an array of words (4 bytes) to XOR columns of a block over multiple iterations
        return : An array of multiple 4 bytes words 
        """
        
        i = 0   
        words = []

        # Get the initial words for the key expansions
        while i < self.Nk :
        
            words.append([self.key[4*i], self.key[4*i+1], self.key[4*i+2], self.key[4*i+3]])
            i += 1

        i = self.Nk
        rconCount = 0
        
        # Compute the following words from the initial words 
        while i < self.Nb * (self.Nr+1) :

            temp = words[i-1]
            
            # At the begining of each word, compute a word by using a rotation, substitution and a XOR with previous values
            if i %  self.Nk == 0:

                temp = Key.XORarrays(Key.SubWord(Key.RotWord(temp)), Key.Rcon(rconCount))
                rconCount += 1

            # Add an other step for 256 bit key with an simple substitution at the middle of the word
            elif self.Nk > 6 and i % self.Nk == 4:
            
                temp = Key.SubWord(temp)     
            
            # Add the new word after XORing it with previous words values
            words.append(Key.XORarrays(words[i-self.Nk], temp))
            i += 1

        return words