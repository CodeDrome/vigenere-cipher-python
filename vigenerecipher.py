import re


class VigenereCipher(object):

    """
    This class provides methods for enciphering and
    deciphering text using the Vigenere cipher.
    """

    def __init__(self):

        self.tabularecta = self.__create_tabula_recta()
        

    def __create_tabula_recta(self):

        tabularecta = []

        for r in range(0, 26):

            offset = 0
            row = []

            for column in range(0, 26):
                row.append(chr(r + 65 + offset))
                offset += 1
                if offset > (25 - r):
                    offset = offset - 26

            tabularecta.append(row)

        return tabularecta


    def encipher(self, plaintext, keyword):

        """
        The plaintext argument can be any string, but
        only the letters a-z and A-Z will be included
        in the encrypted text.
        """

        plaintext = self.__process_plaintext(plaintext)
        keywordrepeated = self.__get_keyword_repeated(keyword, len(plaintext))
        ciphertext = []

        for index, letter in enumerate(plaintext):

            plaintextindex = ord(letter.upper()) - 65
            keywordindex = ord(keywordrepeated[index]) - 65

            #--------------------#
            # Using tabula recta #
            #--------------------#
            encipheredletter = self.tabularecta[keywordindex][plaintextindex]

            #---------------#
            # Using algebra #
            #---------------#
            # encipheredletter = chr(((plaintextindex + keywordindex) % 26) + 65)

            ciphertext.append(encipheredletter)

        return "".join(ciphertext)


    def decipher(self, ciphertext, keyword):

        """
        Decrypts the ciphetext using the keyword.
        Only the letters a-z and A-Z in the
        original text will be present in the
        decrypted text.
        """

        keywordrepeated = self.__get_keyword_repeated(keyword, len(ciphertext))
        decipheredtext = []

        for index, letter in enumerate(ciphertext):

            keywordindex = ord(keywordrepeated[index]) - 65

            #--------------------#
            # Using tabula recta #
            #--------------------#
            decipheredletter = chr(self.tabularecta[keywordindex].index(letter) + 65)

            #---------------#
            # Using algebra #
            #---------------#
            # decipheredletter = chr((((ord(letter) - 65) - keywordindex) % 26) + 65)

            decipheredtext.append(decipheredletter)

        return "".join(decipheredtext)


    def __process_plaintext(self, plaintext):

        plaintext = plaintext.upper()
        plaintext = re.sub("[^A-Z]", "", plaintext)

        return plaintext


    def __get_keyword_repeated(self, keyword, length):

        keyword = keyword.upper()
        keywordrepeated = []
        keywordlength = len(keyword)
        keywordindex = 0

        for i in range(0, length):
            keywordrepeated.append(keyword[keywordindex])
            keywordindex += 1
            if keywordindex > keywordlength - 1:
                keywordindex = 0

        return "".join(keywordrepeated)
