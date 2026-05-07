usuarios = [{"admin": "123456"},
          {"evandro": "654321"},
            {"user": "senha"}]


def acesso():
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    for usuario in usuarios:
        if login in usuario and senha == usuario[login]:
            print("Acesso Permitido!")
            return

    print(usuario)
    print("Acesso Negado!")



acesso()