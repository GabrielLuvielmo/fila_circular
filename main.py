from dataclasses import dataclass
import random

# Função para o dado do jogo
def dado():
    return random.randint(1, 6) + random.randint(1, 6)

# Classe Carta com atributos aleatórios
@dataclass
class Carta:
    atk: int
    defe: int
    vel: int

    def __init__(self):
        self.atk = random.randint(1, 14)
        self.defe = random.randint(3, 10)
        self.vel = random.randint(2, 8)

    def pontos(self):
        return self.atk + self.defe + self.vel

    def __str__(self):
        return f"Carta(ATK: {self.atk}, DEF: {self.defe}, VEL: {self.vel})"


# Classe Pilha
class Pilha:
    def __init__(self):
        self.baralho = []

    def push(self, carta):
        self.baralho.append(carta)

    def pop(self):
        return self.baralho.pop() if self.baralho else None

    def peek(self):
        return self.baralho[-1] if self.baralho else None

    def size(self):
        return len(self.baralho)


# Classe FilaCircular corrigida
class FilaCircular:
    def __init__(self, tamanho=10):
        self.size = tamanho
        self.deck = [None] * tamanho
        self.front = -1
        self.rear = -1
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def enqueue(self, carta):
        if self.is_full():
            print("Fila cheia!")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.deck[self.rear] = carta
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            return None
        carta = self.deck[self.front]
        self.deck[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return carta

    def atual_size(self):
        return self.count


# Criando pilhas de cartas
pilhaJogador = Pilha()
pilhaOponente = Pilha()

# Criando 10 cartas para cada jogador
for _ in range(10):
    pilhaJogador.push(Carta())
    pilhaOponente.push(Carta())

# Criando as filas de deck (5 cartas ativas)
filaDeckJog = FilaCircular()
filaDeckOp = FilaCircular()

while pilhaJogador.size() > 5:
    filaDeckJog.enqueue(pilhaJogador.pop())

while pilhaOponente.size() > 5:
    filaDeckOp.enqueue(pilhaOponente.pop())

print(f"Deck Jogador: {filaDeckJog.atual_size()}")
print(f"Deck Oponente: {filaDeckOp.atual_size()}")

# Função de batalha entre cartas
def batalha(jogador: Carta, oponente: Carta):
    print("\n--- Batalha ---")
    print("Jogador:", jogador)
    print("Oponente:", oponente)
    
    pontos_jog = jogador.pontos()
    pontos_op = oponente.pontos()

    print(f"Pontos Jogador: {pontos_jog}")
    print(f"Pontos Oponente: {pontos_op}")

    if pontos_jog > pontos_op:
        print("Resultado: Jogador Venceu!")
        return "jogador"
    elif pontos_op > pontos_jog:
        print("Resultado: Oponente Venceu!")
        return "oponente"
    else:
        print("Resultado: Empate!")
        return "empate"

# Simulando batalhas até as filas esvaziarem
vitorias_jog = 0
vitorias_op = 0
empates = 0

while not filaDeckJog.is_empty() and not filaDeckOp.is_empty():
    carta_jog = filaDeckJog.dequeue()
    carta_op = filaDeckOp.dequeue()
    resultado = batalha(carta_jog, carta_op)

    if resultado == "jogador":
        vitorias_jog += 1
    elif resultado == "oponente":
        vitorias_op += 1
    else:
        empates += 1

# Resultado final
print("\n=== Resultado Final ===")
print(f"Vitórias Jogador: {vitorias_jog}")
print(f"Vitórias Oponente: {vitorias_op}")
print(f"Empates: {empates}")

if vitorias_jog > vitorias_op:
    print("🏆 Jogador venceu o jogo!")
elif vitorias_op > vitorias_jog:
    print("🏆 Oponente venceu o jogo!")
else:
    print("🤝 O jogo terminou empatado!")
