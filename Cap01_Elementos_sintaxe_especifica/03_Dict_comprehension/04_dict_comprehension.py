#!/usr/binenv python3

dict = {'a':1,'b':2,'c':3,'d':4,'e':5}

dict_comp = {k:v for(k,v) in dict.items() if v > 2 if v % 2 == 0}
print(dict_comp)

# for k,v in dict.items():
# #     if v > 2:
# #         if v % 2 == 0:
# #             print(k,':',v)