def atendimento():
    print("Atendimento ao cliente!")

    while True:
        message = input("Digite sua mensagem: ")

        match message.lower():
            case "oi" | "olá" | "ola":
                print("Olá! Como posso ajudar?")
            case "tchau" | "adeus":
                print("Até mais! Tenha um ótimo dia!")
                break
            case "obrigado" | "obrigada":
                print("De nada! Estamos aqui para ajudar.")
            case _:
                print("Desculpe, não entendi sua mensagem. Por favor, tente novamente.")


atendimento()