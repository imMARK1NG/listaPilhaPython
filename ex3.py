pilha = []

def push(item):
    pilha.append(item)

def pop():
    pilha.pop()

push(4)
push(7)
push(8)
push(9)
push(10)


maior = pilha[0]
menor = pilha[0]


for elementos in pilha:
    if elementos > maior:
        maior = elementos
    if elementos < menor:
        elementos = menor

print(f"\nelemetos na pilha {pilha}\n")

print(f"o maior numero na pilha é {maior}")
print(f"o menor numero na pilha é {menor}")

