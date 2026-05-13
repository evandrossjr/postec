
import requests

def github():



    url = "https://api.github.com/users/evandrossjr"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Erro ao obter as informações do GitHub.")
        return None
    
github_data = github()

if github_data:
    print("Informações do GitHub:")
    print(f"Nome: {github_data['name']}")
    print(f"URL: {github_data['html_url']}")
else:
    print("Não foi possível obter as informações do GitHub.")

