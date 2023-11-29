import string


def caesar_cipher(word, k):
    alphabet_dict = {i: letter for i, letter in enumerate([' '] + list(string.ascii_lowercase))}  #I created a vector that has the letters of the alphabet, on the 0 position being a space
    encrypted_word = '' #we give an empty space for the final word
    for char in word:  #we go through every character of the word
        if char in alphabet_dict.values(): #we check if the character exists in the alphabet vector
            number = (list(alphabet_dict.keys())[list(alphabet_dict.values()).index(char)] + k) % 27  #we find out the new position of the new letter, mod 27 in case it is bigger than 27
            encrypted_word += alphabet_dict[number] #we add a new letter in the encrypted word, based on the new position : number
        else:
            encrypted_word += char
    return encrypted_word #returns the encrypted word


def affine_cipher(word, a, b):
    alphabet_dict = {i: letter for i, letter in enumerate([' '] + list(string.ascii_lowercase))} #I created a vector that has the letters of the alphabet, on the 0 position being a space
    encrypted_word = '' #we give an empty space for the final word
    for char in word:  #we go through every character of the word
        if char in alphabet_dict.values(): #we check if the character exists in the alphabet vector
            char_index = list(alphabet_dict.values()).index(char)
            number = (a * char_index + b) % 27 #we find out the new position of the new letter, mod 27 in case it is bigger than 27
            encrypted_word += alphabet_dict[number] #we add a new letter in the encrypted word, based on the new position : number
        else:
            encrypted_word += char
    return encrypted_word #returns the encrypted word

def belaso_cipher(word, n, k):
    alphabet_dict = {i: letter for i, letter in enumerate([' '] + list(string.ascii_lowercase))}  #I created a vector that has the letters of the alphabet, on the 0 position being a space
    encrypted_word = ''  #we give an empty space for the final word
    for i in range(0, len(word), n):  #we go through every character of the word
        chunk = word[i:i + n]   #we divide the word in chunks of n letters/characters
        for j in range(min(len(chunk), len(k))):  #we go through every chunk
            char = chunk[j]
            if char in alphabet_dict.values(): #we check if the character exists in the alphabet vector
                char_index = list(alphabet_dict.values()).index(char) #we find the letter's position
                number = (char_index + k[j]) % 27
                encrypted_word += alphabet_dict[number]  #we add a new letter to the encrypted word, based on the new position : number
            else:
                encrypted_word += char

    return encrypted_word  #returns the encrypted word

def main():
    word = input("Choose the text you want to encrypt: ")  #we choose the word we want to encrypt
    print("You chose:", word)

    choice = int(input("Choose the cipher you want your word to be encrypted into (1 to 3):\n1. Caesar cipher\n2. Affine cipher\n3. Belaso cipher\n"))
    #Alegem cu ce cipher sa cryptam
    if choice == 1:
        k = int(input("Enter the shift value for the Caesar cipher: ")) #We choose the number of times we permutate
        encrypted_word = caesar_cipher(word, k)
    elif choice == 2:
        a = int(input("Enter the first side of the k :): "))  #We choose k's components, where a letter's new position from word is a*position+b
        b = int(input("Enter the second side of the k :): "))
        encrypted_word = affine_cipher(word, a, b)
    elif choice == 3:
        n = int(input("Enter the slices size: "))
        k = [int(input(f"Enter the number for slice {i+1}: ")) for i in range(n)] #We choose k's components, to which we add to the position of each letter from the chunks of n letters from the word
        encrypted_word = belaso_cipher(word, n, k)
    else:
        print("Invalid choice. Please choose a number between 1 and 3.")  #oopsies, choose something else :)
        return

    print("Encrypted word:", encrypted_word)


if __name__ == "__main__":
    main()
