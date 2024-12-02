s = "ABCDDCBA" 

if len(s) % 2 != 0:
    print("Quantidade de caracteres não é impar.")
else:

    meio = len(s) // 2
    X = s[:meio]  
    Y = s[meio:]  


    if Y == X[::-1]:
        print(X)
    if X == Y[::-1]:
        print(Y)

