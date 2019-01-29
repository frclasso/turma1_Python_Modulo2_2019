#!/usr/bin/env python3

dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

# dobrando os valores
valor_dobrado={k:v*2 for (k,v) in dict.items()}
print(valor_dobrado)


# dobrando a chave
chave_dobrada = {k*2:v for(k,v) in dict.items()}
print(chave_dobrada)


# for k,v in dict.items():
# #     print(k, v*2)