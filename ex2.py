pilha = []

def push(item):
    pilha.append(item)

def pop():
    pilha.pop()
      
    
push(4)
push(9)
push(8)
push(5)


pares = []

for elementos in pilha:
    if elementos % 2 == 0:
        pares.append(elementos)    

print(f"elementos na pilha {pares}")




