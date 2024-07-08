import random
import string
from colorama import init, Fore, Style

init()

header = f"""{Fore.BLUE}


 ####      #     ###   ### ###  #  ###   ####   ####   #####    ###
  #  #    ##    #  #  #  #  #   #   #   #    #   #  #   #   #  #  #
  #  #    ##    #     #     #  ##  #   #     #   #  #   #   #  #
 ####    #  #    #     #    #  ##  #   #     #  ####   #    #   #
 #       ####     #     #    ##  ##    #     #  #  #   #    #    #
 #      #   #  #  #  #  #    ##  ##    #    #   #  #   #   #  #  #
###    ##  ### ###   ###     #   #      ####   ### ## #####   ###


{Style.RESET_ALL}
"""
print(header)

def generate_password(min_length = 8, max_length = 50):
    length = random.randint(min_length, max_length)
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def save_passwords_to_file(filename, num_passwords):
    with open(filename, 'w') as file:
        for _ in range(num_passwords):
            password = generate_password()
            file.write(password + '\n')

num_passwords = int(input("Quantas senhas você quer gerar? "))
filename = input("Qual o nome do arquivo para salvar as senhas? ")

save_passwords_to_file(filename, num_passwords)
print(f"{num_passwords} senhas foram geradas e salvas em '{filename}'.")