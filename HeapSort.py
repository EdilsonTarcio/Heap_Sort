import random

def organizar(lista, n, m): 
    maior = m       # Nó maior maxheap que ficará na raiz
    esquerdo = 2 * m + 1     # índice mais a esquerda = 2*i + 1 
    direito = 2 * m + 2     # ndice mais a direita = 2*i + 2 
  
    # Verifica se o indice mais a esquerda da raiz existe and > root 
    if esquerdo < n and lista[m] < lista[esquerdo]: 
        maior = esquerdo 
  
    # Verifica se o indice mais a direita da raiz existe and > root 
    if direito < n and lista[maior] < lista[direito]: 
        maior = direito 
  
    # Atualiza a raiz se necessario 
    if maior != m: 
        lista[m],lista[maior] = lista[maior],lista[m]  
  
        organizar(lista, n, maior) 
  
  
# definição de classificação da Heap Sort
def HeapSort(lista): 
    n = len(lista) 
  
    for m in range(n // 2 - 1, -1, -1): 
        organizar(lista, n, m) 
  
    # extraindo elementos 
    for m in range(n-1, 0, -1): 
        lista[m], lista[0] = lista[0], lista[m]   
        organizar(lista, m, 0) 
  
ran=20 # Índice para quantidade de números gerados
lista = random.sample(range(100),  ran) # gerando valore aleatórios entre 0 e 100 unicos
HeapSort(lista) 
n = len(lista) 
print ("Valores organizados pelo Heap Sort") 
for m in range(n): 
    print ("%d" %lista[m])