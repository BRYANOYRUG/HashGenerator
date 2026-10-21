import bcrypt
from termcolor import colored
import pyfiglet
from colorama import init
import os
import time
init()
while True:
    banner = pyfiglet.figlet_format("HASH GENERATOR")
    banner = colored(banner, "green")
    print(banner)
    print(colored("KernelHost11 technology", "red"))
    print(colored("by BMRL", "blue"))
    senha = input("Texto: ")
    rounds_str =  input("Rounds(Padrão é 12): ")
    erro = False
    if rounds_str.isdigit():
        try:
            rounds = int(rounds_str)
        except Exception as e:
            print(f"Erro {e}")
    else:
        print("Rounds não é um numero.")
    # Gera o salt aleatório (padrão de custo é 12)
    try:
        if senha.upper() == "EXIT" or rounds_str.upper() == "EXIT":
            os.close(fd=0)
        salt = bcrypt.gensalt(rounds=rounds)

        # Gera o hash (a senha precisa estar em bytes)
        novo_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)

        print(f"Seu HASH: {novo_hash.decode('utf-8')}")

    except Exception as e:
        print(f"Erro {e}")
        erro = True
    if erro is False:
        gerar_hash_yn = input("Deseja gerar outro hash? (S/N)")
        if gerar_hash_yn.upper() == "S":
            os.system("cls")
        else:
            print("Fechando...")
            time.sleep(3)
            break
    else:
        print("Tente novamente...")
    