import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
    #0(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Capacidade maxima atingida")
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

            x = self.ultima_posicao
            while x >= posicao:
                self.valores[x + 1] = self.valores[x]
                x -= 1
            self.valores[posicao] = valor
            self.ultima_posicao += 1
vetor = VetorOrdenado(10)
vetor.imprime() #ate aqui o vetor esta vazio
vetor.insere(6)
vetor.imprime()

