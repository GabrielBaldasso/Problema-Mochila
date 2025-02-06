import random

# Defina peso máximo da mochila e uma lista de objetos
peso_max_mochila = 5000
objetos = [
    {"id": 0, "peso": 2000, "utilidade": 6},
    {"id": 1, "peso": 100, "utilidade": 90},
    {"id": 2, "peso": 500, "utilidade": 80},
    {"id": 3, "peso": 100, "utilidade": 60},
    {"id": 4, "peso": 100, "utilidade": 100},
    {"id": 5, "peso": 3000, "utilidade": 10},
    {"id": 6, "peso": 50, "utilidade": 20},
    {"id": 7, "peso": 500, "utilidade": 75},
]

# Parâmetros do algoritmo genético
tamanho_populacao = 10000
taxa_cruzamento = 1
taxa_mutacao = 1
geracoes = 100

# Função de aptidão
def funcao_aptidao(individuo):
    peso_total = 0
    utilidade_total = 0
    for i in range(len(individuo)):
        if individuo[i] == 1:
            peso_total += objetos[i]["peso"]
            utilidade_total += objetos[i]["utilidade"]
    if peso_total > peso_max_mochila:
        return 0  # Penaliza soluções que excedem o peso máximo
    return utilidade_total

# Inicialização da população
populacao = []
for _ in range(tamanho_populacao):
    cromossomo = [random.randint(0, 1) for _ in objetos]
    populacao.append(cromossomo)

# Algoritmo genético
for geracao in range(geracoes):
    populacao.sort(key=lambda x: -funcao_aptidao(x))
    nova_populacao = []

    # Elitismo: mantém os melhores indivíduos da geração anterior
    elite_size = int(tamanho_populacao * 0.1)
    nova_populacao.extend(populacao[:elite_size])

    # Reprodução (cruzamento)
    while len(nova_populacao) < tamanho_populacao:
        pai1, pai2 = random.choices(populacao[:elite_size], k=2)
        filho1, filho2 = pai1[:], pai2[:]
        if random.random() < taxa_cruzamento:
            ponto_cruzamento = random.randint(1, len(objetos) - 1)
            filho1 = pai1[:ponto_cruzamento] + pai2[ponto_cruzamento:]
            filho2 = pai2[:ponto_cruzamento] + pai1[ponto_cruzamento:]
        nova_populacao.extend([filho1, filho2])

    # Mutação
    for individuo in nova_populacao:
        for i in range(len(objetos)):
            if random.random() < taxa_mutacao:
                individuo[i] = 1 - individuo[i]  # Inverte o bit

    populacao = nova_populacao

# Melhor solução encontrada
melhor_solucao = max(populacao, key=funcao_aptidao)
peso_final = sum(objetos[i]["peso"] for i in range(len(objetos)) if melhor_solucao[i] == 1)
utilidade_final = funcao_aptidao(melhor_solucao)

print("Melhor solução encontrada:")
print("Objetos na mochila (IDs):", [i for i in range(len(objetos)) if melhor_solucao[i] == 1])
print("Peso final da mochila:", peso_final)
print("Utilidade final da mochila:", utilidade_final)
