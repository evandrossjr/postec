respostas = [
    "Isso é interessante! Me conte mais.",
    "Eu entendo. Pode explicar melhor?",
    "Parece que você tem uma opinião forte sobre isso.",
    "Eu nunca tinha pensado nisso dessa maneira antes.",
    "Isso me faz pensar em algo diferente. O que mais você acha?",
    "Eu gostaria de saber mais sobre isso. Pode compartilhar mais detalhes?",
    "Parece que isso é importante para você. Por quê?",
    "Eu estou aqui para ouvir. Continue falando.",
    "Isso é algo que muitas pessoas pensam. O que te levou a essa conclusão?",
    "Eu acho que isso é um ponto válido. Você pode expandir um pouco mais?"
]

def chat_ia():
    print("Sobre o que você gostaria de conversar?")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Chat encerrado. Até a próxima!")
            break
        resposta = respostas[hash(user_input) % len(respostas)]
        print(f"IA: {resposta}")
    

chat_ia()