perguntas = [
    "O que é inteligência artificial?",
    "Quais são os tipos de inteligência artificial?",
    "Quais são as aplicações da inteligência artificial?",
    "Quais são os desafios da inteligência artificial?",
    "Quais são as vantagens e desvantagens da inteligência artificial?"
]


respostas = [
    "Inteligência artificial é a simulação de processos de inteligência humana por máquinas, especialmente sistemas computacionais.",
    "Os tipos de inteligência artificial incluem: IA fraca (ou estreita), IA forte (ou geral) e IA superinteligente.",
    "As aplicações da inteligência artificial incluem: assistentes virtuais, reconhecimento de voz, visão computacional, automação de processos, entre outros.",
    "Os desafios da inteligência artificial incluem: ética, privacidade, segurança, viés algorítmico, entre outros.",
    "As vantagens da inteligência artificial incluem: automação de tarefas, aumento da eficiência, análise de grandes volumes de dados, entre outros. As desvantagens incluem: perda de empregos, dependência tecnológica, questões éticas, entre outros."
]



def dicionarioIA():
    return dict(zip(perguntas, respostas))




def escolherPergunta():

    print("Perguntas disponíveis:")
    for i, pergunta in enumerate(perguntas, 1):
        print(f"{i}. {pergunta}")
    escolha = int(input("Digite o número da pergunta que deseja fazer: "))
    if 1 <= escolha <= len(perguntas):
        return perguntas[escolha - 1]   
    else:
        print("Escolha inválida.")
        return None
    
def responderPergunta(pergunta):
    dicionario = dicionarioIA()
    resposta = dicionario.get(pergunta, "Desculpe, não tenho uma resposta para essa pergunta.")
    return resposta


pergunta_escolhida = escolherPergunta()
if pergunta_escolhida:
    resposta = responderPergunta(pergunta_escolhida)
    print(f"Resposta: {resposta}")


