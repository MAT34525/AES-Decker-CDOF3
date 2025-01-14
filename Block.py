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
    
INVSBOX = [['52', '09', '6a', 'd5', '30', '36', 'a5', '38', 'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb'], 
            ['7c', 'e3', '39', '82', '9b', '2f', 'ff', '87', '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb'], 
            ['54', '7b', '94', '32', 'a6', 'c2', '23', '3d', 'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e'], 
            ['08', '2e', 'a1', '66', '28', 'd9', '24', 'b2', '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25'], 
            ['72', 'f8', 'f6', '64', '86', '68', '98', '16', 'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92'], 
            ['6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da', '5e', '15', '46', '57', 'a7', '8d', '9d', '84'], 
            ['90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a', 'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06'], 
            ['d0', '2c', '1e', '8f', 'ca', '3f', '0f', '02', 'c1', 'af', 'bd', '03', '01', '13', '8a', '6b'], 
            ['3a', '91', '11', '41', '4f', '67', 'dc', 'ea', '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73'], 
            ['96', 'ac', '74', '22', 'e7', 'ad', '35', '85', 'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e'], 
            ['47', 'f1', '1a', '71', '1d', '29', 'c5', '89', '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b'], 
            ['fc', '56', '3e', '4b', 'c6', 'd2', '79', '20', '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4'], 
            ['1f', 'dd', 'a8', '33', '88', '07', 'c7', '31', 'b1', '12', '10', '59', '27', '80', 'ec', '5f'], 
            ['60', '51', '7f', 'a9', '19', 'b5', '4a', '0d', '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef'], 
            ['a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0', 'c8', 'eb', 'bb', '3c', '83', '53', '99', '61'], 
            ['17', '2b', '04', '7e', 'ba', '77', 'd6', '26', 'e1', '69', '14', '63', '55', '21', '0c', '7d']]

class Block :

    def __init__(self, sequence: bytearray) :
        """
        Create a new block from a 16 bytes sequence
        'sequence' - Sequence to be transformed (filled if size < 16 bytes)        
        """

        if len(sequence) > 16 :

            raise ValueError("The byte sequence used to create a block is too long (> 16)")
        
        # Complete the sequence of byte with zeros
        altSequence = [x for x in sequence]
        altSequence.extend([0 for x in range(len(sequence), 16)])

        self.Nb = 4
        stateArray = []

        # Distribute the values in a 4 * 4 2DArray
        for row in range(self.Nb) :

            stateArrayColumns = []

            for col in range(self.Nb):

                stateArrayColumns.append(altSequence[row + 4 * col])

            stateArray.append(stateArrayColumns)

        self.block = stateArray

    # Static methods =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def BlockToSequence(self) -> list :
            """
            Convert the block back to an interger array
            return : Array containing the block data            
            """

            array = []

            for col in range(self.Nb) :

                for row in range(self.Nb):

                    array.append(self.block[row][col])

            return array

    def MultiplyBytes(byte1: int, byte2 : int) -> int:
        """
        Get the resulting polinomial from a polinomial multiplication
        'byte1' - First byte
        'byte2' - Second byte
        return : Result of the multiplication as an integer
        """

        mult = 0
        binaryOfMultiplier = bin(byte2)[2:] # Convert to binary notation

        # Compute the polynomial multiplication result
        for iter, bit in enumerate(binaryOfMultiplier):

            subMult = 0

            # Let n be the power of x from byte2, at the index 'iter'   
            # We multiply byte1 by the n th term of byte2 by shifting it n times
            # We add up the polynomial expansion by XORing it to previous values

            if bit == '1':
                
                # Shift byte1 n times
                subMult = byte1 << (len(binaryOfMultiplier) - 1 - iter)

            # Add up the polynomial expansion
            mult ^= subMult

        return mult
    
    def ShiftArrayLeft(array : list, shift : int, left : bool = True) -> list:
        """
        Shift an array 'shift' times on the left (default) or right
        'array' - Array to be shifted
        'shift' - Integer specifying the amount of shift (looped if bigger than the array length)
        'left' - Boolean idicating the direction of the Shift : True (default) : left, False : right        
        """

        shiftedArray = []
        m = len(array)
        shift = shift%m # Loop the shift amount if too big

        # Rotate the elements in the array
        for item in range(m):

            # Case if shift left
            if left :

                # Displace the last elements to the begining of the array
                if item < m - shift:

                    shiftedArray.append(array[item + shift])

                # Displace the first element to the end of array 
                else :

                    shiftedArray.append(array[(item + shift)%m ])
            
            # Case if shift right
            else :

                # Displace the first elements
                if 0 < m - shift:

                    shiftedArray.append(array[item - shift])

                # Displace the last element to the beginning of array
                else :

                    shiftedArray.append(array[(item - shift)%m ])

        return shiftedArray

    def ModuloBytes(byte : int, mod : int = 283) -> int:
        """
        Compute the result of the modulus by a polynomial represented by a byte by an other one  
        'byte' - Byte representing the polynomial to get the rest
        'mod' - Byte representing the modulus (default x^8 + x^4 + x^3 + x + 1 : 283)
        return : Byte representing the rest of the operation byte mod(mod)
        """

        modres = byte               # Result initial value

        binmod = bin(mod)[2:]       # Convert the modulus to binary
        binmodres = bin(modres)[2:] # Convert the modulus result to binary

        # We will reduce th polynomial until it is shorter than the modulus
        # Therefore, we will successively substract (XOR) the shifted the modulus from the polynomal
        # To get the amount of shift required, we get the difference of both greatest powers of x in each polynomials

        while len(binmodres) >= len(binmod):

            if binmodres[0] == '1' :

                # Substract the shifted modulus from the polynomial
                modres ^= (mod << (len(binmodres) - len(binmod)))
                binmodres = bin(modres)[2:] # Get the binary equivalent

        return modres

    # Instance methods =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
   
    def SubBytes(self, sbox : list = SBOX):
        """
        Replace all values in the block using a S-Box
        'sbox' - S-Box used for the substitution
        """

        subBlock = []

        for row in range(self.Nb):

            subBlockRow = []

            for column in range(self.Nb):

                # Get the substitution value using the S - Box

                val = self.block[row][column]

                valx = val >> 4             # Get the 4 MSB as x axis for the lookup table 
                valy = val ^ (valx << 4)    # Get the 4 LSB as y axis for the lookup table 

                subBlockRow.append(int(sbox[valx][valy], 16))

            subBlock.append(subBlockRow)

        self.block = subBlock

    def InvSubBytes(self):
        """
        Revert the substitution of the block values using the revert S-Box
        """

        # Use tge same algorithm as the substitution with the revert S-Box
        self.SubBytes(INVSBOX)

    def ShiftRows(self, left = True):
        """
        Gradually shift the rows of the block to the left starting from the second row
        'left' - Direction of the shift (default left)
        """

        shiftBlock = []

        for row in range(0, self.Nb):

            shiftBlock.append(Block.ShiftArrayLeft(self.block[row], row, left))

        self.block = shiftBlock

    def InvShiftRows(self):
        """
        Gradually shift the rows of the block to the right starting from the second row 
        """

        # Shift rows to the right
        self.ShiftRows(False)

    def MixColumns(self, IV = [3, 1, 1, 2]):
        """
        Mix the columns of the block using a rotating vector
        'IV' - Vector [03, 01, 01, 02]
        """

        # We do a matrix multiplication of the rotating vector shifts and the columns values
        # Multiplications are polynomial multiplications, additions are simple XOR
        # The result of each new column cells values are cast into the filed GF(2^8) using 
        # an irreductible polynomial x^8 + x^3 + + x^1 + 1 (default)

        # c1'        Shift(IV, 2)         c1
        # c2'    =   Shift(IV, 3)    *    c2
        # c3'        Shift(IV, 4)         c3

        mixedCol = []

        for row in range(self.Nb):

            mixedColRow = []

            for col in range(self.Nb):

                # Rotate the vector depending on the row number
                shiftedIV = Block.ShiftArrayLeft(IV, row+1, False )
                mult = 0

                # Get the value of the matrix multiplication
                for multCol in range(self.Nb):

                    mult ^= Block.MultiplyBytes(shiftedIV[multCol], self.block[multCol][col])

                # Cast the multiplication values in the field GF (2^8)
                mixedColRow.append(Block.ModuloBytes(mult))

            mixedCol.append(mixedColRow)

        self.block = mixedCol

    def InvMixColumns(self, IV = [11, 13, 9, 14]):
        """
        Revert the columns mix of the block using the invert of the rotating vector 
        'IV' - Invert vector [0b, 0d, 09, 0e]
        """

        # Reverse the column mix using the revert IV
        self.MixColumns(IV)

    def AddRoundKey(self, round, keySchedule):
        """
        XOR the block columns by using the keySchedule (generated using the key expansion algorithm)
        'round' - Index of the keySchedule word to XOR the column with
        'keySchedule' - Full keySchedules words from the key expansion algorithm
        """

        blockWithKey = []

        for row in range(self.Nb):

            blockWithKeyRow = []

            for col in range(self.Nb):

                # Get the new value of the block cell by XORing the block cell and the keySchedule word
                # Then, apply a cast of the result in the field GF(2^8)
                blockWithKeyRow.append(Block.ModuloBytes(self.block[row][col] ^ keySchedule[round*self.Nb + col][row]))

            blockWithKey.append(blockWithKeyRow)

        self.block = blockWithKey

                