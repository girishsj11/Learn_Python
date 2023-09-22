#RandomPassword_generator.py

def password_generator():
    password = str()
    characters = [chr(i) for i in range(65,65+26)] #Capital alphabets
    characters.extend([chr(i) for i in range(97,97+26)]) #small letter alphabets
    characters.extend([str(i) for i in range(0,10)]) #numbers from 0 to 9
    characters.extend(['!','@','#','$','%','^','&','*']) # special characters/symbols
    print(characters)

    for i in range(16):
        password += random.choice(characters)

    print("Your password is - ",password)
    


if __name__ == "__main__":
    password_generator()
