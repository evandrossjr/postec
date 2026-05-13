import json


def generate_question():
    
        question = input("Faça uma pergunta: ")
        return question

def generate_answer(question):
    

        if "?" in question:
            return "Essa é uma pergunta interessante!"
        elif "!" in question:
            return "Parece que você está fazendo uma exclamação!"
        else:
            return "Não entendi sua pergunta."
        
question = generate_question()
answer = generate_answer(question)


chatbot = {
     "pergunta": question,
      "resposta": answer
} 

json_chatbot = json.dumps(chatbot, indent=4, ensure_ascii=False)

print(json_chatbot)

  