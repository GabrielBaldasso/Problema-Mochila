# Algoritmo Genético para Resolução do Problema da Mochila

## Funcionalidades

Este código utiliza um algoritmo genético para resolver o problema clássico da mochila, onde o objetivo é escolher um subconjunto de objetos para colocar em uma mochila, de modo que a utilidade total dos objetos seja maximizada, sem exceder o peso máximo da mochila.

### Descrição do Código

O código é composto por várias partes:

1. **Definição dos Objetos e Parâmetros:**
   - O código começa definindo o peso máximo da mochila (`peso_max_mochila`) e uma lista de objetos, onde cada objeto possui um `id`, um `peso` e uma `utilidade`.
   - Também são definidos os parâmetros do algoritmo genético, como o tamanho da população, taxa de cruzamento, taxa de mutação e o número de gerações.

2. **Função de Aptidão:**
   - A função `funcao_aptidao` calcula a aptidão de um indivíduo, que é uma solução representada por um vetor de bits (cromossomo). A aptidão é dada pela soma das utilidades dos objetos incluídos na mochila, penalizando soluções cujo peso exceda o limite máximo da mochila.

3. **Inicialização da População:**
   - Uma população inicial é gerada aleatoriamente, onde cada indivíduo é um vetor de bits representando quais objetos estão incluídos na mochila.

4. **Algoritmo Genético:**
   - O algoritmo genético é executado por um número predefinido de gerações. A cada geração, os indivíduos são classificados com base em sua aptidão e, em seguida, os melhores indivíduos são selecionados para a reprodução.
   - **Elitismo:** Uma parte da população (10%) é mantida intacta para garantir que as melhores soluções sejam preservadas.
   - **Reprodução (Cruzamento):** A reprodução ocorre por cruzamento entre pares de indivíduos selecionados, criando novos indivíduos (filhos) com combinações dos genes dos pais.
   - **Mutação:** A mutação é aplicada de maneira aleatória a cada indivíduo para introduzir diversidade na população, invertendo aleatoriamente bits no cromossomo.

5. **Solução Final:**
   - Após a execução do algoritmo genético, a melhor solução encontrada é exibida, mostrando os objetos selecionados, o peso total da mochila e a utilidade total.

### Parâmetros Configuráveis

- **Peso máximo da mochila (`peso_max_mochila`)**: Define o peso máximo que a mochila pode carregar.
- **Objetos**: Uma lista de objetos, cada um com um peso e uma utilidade associados.
- **Parâmetros do algoritmo genético**:
  - `tamanho_populacao`: Número de indivíduos na população.
  - `taxa_cruzamento`: Probabilidade de cruzamento entre dois indivíduos.
  - `taxa_mutacao`: Probabilidade de mutação em cada gene de um indivíduo.
  - `geracoes`: Número de gerações que o algoritmo executa.

