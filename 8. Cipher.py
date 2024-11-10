# Funkcja z inputem
# def greet(name):
#     print(f"Hello {name}")
#     print(f'How are you {name}')
# greet('Szymon')
#
# #Funkcja z kilkoma inputami
# def greet_with(name, location):
#     print(f'Hello {name}')
#     print(f'What is it like in {location}?')
# #greet_with('Szymon', 'Plewiska')
# #or
# greet_with(name = 'Szymon',location='Plewiska')
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
run = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cezar(start_text, shift_amount,cipher_direction):
    szyfr = ''
    for litera in start_text:
        if litera in alphabet:
            position = alphabet.index(litera)
            if cipher_direction == 'decode' and shift_amount >= 0:
                shift_amount *= -1
            new_position = position + shift_amount
            szyfr += alphabet[new_position]
        else:
            szyfr+=litera
    print(f'The {cipher_direction}d text is {szyfr}')

while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    cezar(start_text=text,shift_amount=shift,cipher_direction=direction)
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no',\n").lower()
    if answer == "no":
        run = False
        print('Goodbye!')

# def encrypt(plain_text,shift_amount):
#     szyfr = ''
#     for litera in plain_text:
#         position = alphabet.index(litera)
#         new_position = position + shift_amount
#         szyfr += alphabet[new_position]
#     print(f"The encoded text is {szyfr}")
#
# def decrypt(szyfr,shift_amount):
#     plain_text = ''
#     for litera in szyfr:
#         new_position = alphabet.index(litera)
#         position = new_position - shift_amount
#         plain_text += alphabet[position]
#     print(f"The decoded text is {plain_text}")
#
# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(szyfr=text, shift_amount=shift)