# Project-Python-Algorithms

# Sobre
Foram desenvolvidos algoritmos para a solução dos problemas abaixo, levando em consideração a complexidade algoritmica:

1. No arquivo challenges/challenge_study_schedule.py:
- Função para descobrir em qual horário uma plataforma online é mais acessada por pessoas usuárias.;
- Recebe como input uma lista de tuplas (permanence_period), em que cada tupla representa o período de permanência de uma pessoa usuária no sistema com seu horário de entrada e de saída; e o horário sendo investigado (target_time);
- O retorno é o número de pessoas usuárias que estavam online no período investigado.
- Ordem de complexidade: O(n).


2. No arquivo tests/encrypt/test_encrypt.py:
Teste para a função legada encrypt.py, que faz a criptografia de mensagens segundo algumas regras de negócio.


3. No arquivo challenges/challenge_palindromes_recursive.py
- Função recursiva para verificação de palíndromos (palavras que podem ser lidas da mesma forma da esquerda para a direita e vice-versa, ex.: "ANA");
- Requer três inputs: a string a ser verificada, e os índices mínimo e máximo da palavra;
- O output é True ou False.


4. No arquivo challenges/challenge_palindromes_iterative.py:
- Função iterativa para verificação de palíndromos (palavras que podem ser lidas da mesma forma da esquerda para a direita e vice-versa, ex.: "ANA");
- Recebe como input a string a ser verificada;
- O output é True ou False.


5. No arquivo challenges/challenge_anagrams.py
- Função que compara duas palavras e verifica se são anagramas uma da outra;
- Recebe como input duas strings;
- Retorna como output uma tupla em que as duas strings tem suas letras ordenadas alfabeticamente e um booleano indicando se são anagramas ou não (True ou False);
- Ordem de complexidade: O(n log(n))


6. No arquivo challenges/challenge_find_the_duplicate.py
- Função que verifica se há números que se repetem em uma array;
- Recebe como input uma array de números;
- Retorna como output o número que se repete na array.
- Ordem de complexidade: O(n log(n))

Os demais arquivos foram desenvolvidos pelo time da Trybe.

## Tecnologias usadas
Python
