
pilha1 = [1, 3, 5, 8]
pilha2 = [2, 4, 6, 74]


pilha3 = []


while pilha1 or pilha2:
    
    if not pilha1:
        pilha3.append(pilha2.pop())
    elif not pilha2:
        pilha3.append(pilha1.pop())
    else:
        if pilha1[-1] > pilha2[-1]:
            pilha3.append(pilha1.pop())
        else:
            pilha3.append(pilha2.pop())

print("Pilha 3:", pilha3)
