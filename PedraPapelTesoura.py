import random

usuario = 0
computador = 0

options = ["r", "t", "p"]

while True:
    user_choice = input(
        "Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair. ").lower()

    if user_choice == 'q':
        break

    computer_choice = random.randint(0, 2)
    # 0 : R, 1 : T, 2 : P
    computer_options = options[computer_choice]

    print("O computador escolheu " + computer_options)

    if user_choice == computer_options:
        print("Empate")

    elif user_choice == "r" and computer_options == "t":
        print("Você ganhou!")
        usuario = usuario + 1

    elif user_choice == "p" and computer_options == "r":
        print("Você ganhou!")
        usuario = usuario + 1

    elif user_choice == "t" and computer_options == "p":
        print("Você ganhou!")
        usuario = usuario + 1
    else:
        print("Você perdeu")
        computador = computador + 1

print("Sua pontuação: " + str(usuario))
print("Pontuação do Computador: " + str(computador))

if computador > usuario:
    print("Derrota!!")
elif computador == usuario:
    print("Empate")
else:
    print("Vitória!!!!")

print("Até mais!!")
