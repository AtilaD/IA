class VetorOrdenado:
    def __int__(self):
        self.vetor = []

    def inserir(self, elemento):
        posicao = 0
        while posicao <len(self.vetor) and self.vetor[posicao] < elemento:
            posicao += 1
        self.vetor.insert(posicao, elemento)

    def buscar(self, elemento):
        esquerda = 0
        direita = len(self.vetor) - 1
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            if self.vetor[meio] == elemento:
                return meio
            elif self.vetor[meio] < elemento:
                esquerda = meio + 1
            else:
                direita = meio - 1
        return -1
VetorOrdenado()

print(VetorOrdenado)
