

import requests

def cotacao(moeda):



    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Erro ao obter a cotação.")
        return None
    
moeda = input("Digite a moeda (ex: USD-BRL): ")
cotacao_data = cotacao(moeda)

if cotacao_data:

    chave = moeda.replace('-', '')
    if chave in cotacao_data:
        info = cotacao_data[chave]

        print(f"Cotação de {moeda}:")
        print(f"Valor: {info['bid']}")
        print(f"Data: {info['create_date']}")

else:
    print("Não foi possível obter a cotação.")


