def remove_element(L, x):
    if x in L:
        L.remove(x)
    return L


L = [1, 2, 3, 4, 5, 6]
x = 4
nova_lista = remove_element(L, x)
print(nova_lista)


pilha = []


pilha.append(2)  
pilha.append(3)  
pilha.append(5)  
pilha.pop()   
pilha.pop()   
pilha.append(1)  

print(pilha)

from collections import deque


fila = deque()


fila.append(2)   
fila.append(3)  
fila.popleft()   
fila.append(5)   
fila.popleft()   
fila.append(1)   

print(list(fila))
