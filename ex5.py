pilha = []

for _ in range(15):
    numero = int(input("Digite os elementos:"))
    pilha.append(numero)
    
    if numero % 2 == 0:
        pass
    else:
        removido = pilha.pop()
        print(f"numero impar {removido} removido da pilha.")

print(f"valores na pilha {pilha}")

print("\nEsvaziando a pilha...")
while pilha:
    print(f"{pilha.pop()} removido da pilha.")