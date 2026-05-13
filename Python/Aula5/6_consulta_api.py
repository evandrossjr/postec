
import requests
import json

def countries(country):



    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
        
    else:
        print("Erro ao obter a cotação.")
        return None
    
 
country = input("Digite o nome do país (em inglês): ")
country_data = countries(country)

if country_data:

    
        info = country_data[0]

        print(f"Informações sobre {info['name']['common']}:")
        print(f"Capital: {info['capital'][0]}")
        print(f"População: {info['population']}")

        with open("dadosapi.json", 'w') as arquivo:
            json.dump(info, arquivo, indent=4)
        
        print("Dados salvos em dadosapi.json com sucesso!")
        
else:
    print("Não foi possível obter as informações do país.")




