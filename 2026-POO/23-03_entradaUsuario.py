#programa que permite a entrada de um usuario em um sistema. LOGIN e SENHA.

def login ():
    usuario=str(input("Nome de usuário: "))
    senha=int(input("Senha: "))
    print (f"Bem vindo(a): {usuario}")
    return login

def cadastro ():
    cad_usuario=str(input("Digite um nome de usuário: "))
    cad_email=str(input("Digite seu email: "))
    cad_senha=int(input("Digite uma senha: "))
    print(f"Usuário cadastrado!")
    return cadastro
   
opc=int(input("Olá, bem vindo ao sistema, gostaria de fazer login ou não pussui cadastro? [1/2]:  "))
if opc!=1:
    cadastro()

else:
    login()
    
    
