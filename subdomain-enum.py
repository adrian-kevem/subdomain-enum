import dns.resolver
import sys

try:
    dominio = sys.argv[1]
    wordlist = sys.argv[2]
except:
    print("Argumentos inválidos!")
    sys.exit()

resolver = dns.resolver.Resolver()
try:
    with open(wordlist, "r") as file:
        subdominios = file.read().splitlines()
except:
    print("Arquivo não encontrado!")
    sys.exit()

for subdominio in subdominios:
    try:
        alvo = f"{subdominio}.{dominio}"
        resultados = resolver.resolve(f"{alvo}", "A")
        for resultado in resultados:
            print(f"Subdomínio '{alvo}': {resultado}")
    except:
        print(f"Subdomíno '{alvo}' não existente!")