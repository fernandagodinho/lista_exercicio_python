class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [' ' for _ in range(9)]  # Inicializa o tabuleiro vazio
        self.jogador_atual = 'X'  # O primeiro jogador é o 'X'

    def imprimir_tabuleiro(self):
        for i in range(0, 9, 3):
            print(f'{self.tabuleiro[i]} | {self.tabuleiro[i+1]} | {self.tabuleiro[i+2]}')
            if i < 6:
                print('---------')

    def trocar_jogador(self):
        self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'

    def vencedor(self):
        linhas_vencedoras = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for linha in linhas_vencedoras:
            if self.tabuleiro[linha[0]] == self.tabuleiro[linha[1]] == self.tabuleiro[linha[2]] != ' ':
                return self.tabuleiro[linha[0]]
        if ' ' not in self.tabuleiro:
            return 'Empate'
        return False

    def jogar(self):
        while not self.vencedor():
            self.imprimir_tabuleiro()
            jogada_valida = False
            while not jogada_valida:
                jogada = input(f'Jogador {self.jogador_atual}, escolha uma posição de 1 a 9: ')
                if jogada.isdigit() and int(jogada) in range(1, 10) and self.tabuleiro[int(jogada)-1] == ' ':
                    self.tabuleiro[int(jogada)-1] = self.jogador_atual
                    jogada_valida = True
                else:
                    print('Jogada inválida. Tente novamente.')
            self.trocar_jogador()
        self.imprimir_tabuleiro()
        if self.vencedor() == 'Empate':
            print('O jogo terminou em empate.')
        else:
            self.trocar_jogador()
            print(f'O jogador {self.jogador_atual} venceu!')

if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.jogar()
