
def chatbot():
    username = input("Digite seu nome: ")   
    message = input(f'{username}, "digite uma mensagem: ')  
    if message.lower() == "oi":
        resposta = "Olá!"
    elif message.lower() == "como você funciona?":
        resposta = "Utilizo programação e IA."
    else:
        resposta = "Não compreendi."

    print(f"Chatbot: {resposta}")

chatbot()