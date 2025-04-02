import vigenerecipher


def main():

    print("-------------------")
    print("| Vigenere Cipher |")
    print("-------------------\n")

    vc = vigenerecipher.VigenereCipher()

    keyword = "orchestra"

    plaintext = "Imagination is more important than knowledge."
    print(f'Plaintext:  {plaintext}')

    enciphered = vc.encipher(plaintext, keyword)
    print(f'Enciphered: {enciphered}')

    deciphered = vc.decipher(enciphered, keyword)
    print(f'Deciphered: {deciphered}')


if __name__ == "__main__":

    main()
