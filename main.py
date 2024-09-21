# Importar as bibliotecas necessárias para a execução de algumas funções
import random

# Definir uma função que transforma o arquivo "cartelas.txt" em uma lista
def gerador_de_cartela (linhas):  
  a = [[]] * len (linhas)
  for i in range (len (linhas)):
    a[i] = linhas [i] .rstrip () .split (",")
  return a

# Definir uma função que gera quatro cartelas para serem mostradas na partida
def quatro_cartelas (lista_cartelas):
  a = [[]] * 4
  b = random.sample (range (len (lista_cartelas)), 4)
  for i in range (len (a)):
      a[i] = lista_cartelas [b [i]]
  return a

# Definir uma função que troca as cartelas que o jogador é "dono"
def troca (lista_cartelas, n):
  return lista_cartelas [n]

# Definir uma função que sorteia um número entre 1 e 50
def sortear_numero ():
  return random .sample (range (1,50), 49)

# Definir uma função que mostra as cartelas na partida
def mostrar_cartelas (cartela, special=False):
  for i in range (len (cartela)):
    if special == True:
      print (f"*******{cartela [i]}*******", end=" ")
    else:
      print (f"{cartela [i]}", end=" ")



# Definir as contantes de texto a serem printadas durante o jogo
cabecalho = """
# PROJETO: Bingo Lite
# Alunos:
Bruno Gustavo Rocha TIA: 32215029
Murilo Ramos do Nascimento TIA: 32271166
"""

perdeu = """
Que pena :( não foi dessa vez!
"""

# Printar o cabeçalho do jogo, com identificações
print (f"{cabecalho}\n\n\n")

print ("#######    B  I  N  G  O    #######")
print ("\n\n")

# Definir o valor boolean para repetição de sequência de jogos
repetindo_jogos = True

# Definir as constantes que serão executadas durante o jogo
while repetindo_jogos:
  cartelas = open ("cartelas.txt", "r")
  vencedores = open ("vencedores.txt", "a")
  repetindo_partida = True
  linha = cartelas .readlines ()
  lista_cartelas = gerador_de_cartela (linha)
  cartelas_jogo = quatro_cartelas (lista_cartelas)
  resposta = ""
  receba = sortear_numero ()
  atual = 0
  iter_sort = 0
  verdadeiros = []
  vencedora = -1
  boolean_cartelas = [ [False] * 5, [False] * 5, [False] * 5, [False] * 5, [False] * 5 ]

  # Começar o jogo
  print ("# BOA SORTE JOGADOR(A) :) (Vai precisar rsrsrs) \n\n")

  # Sortear um número, imprimir na tela e perguntar se o jogador quer mudar de cartela
  while repetindo_partida:
    print (f"####### NUMERO SORTEADO: {receba[iter_sort]} #######\n")
    if resposta != "":
      try:
        resposta = int (resposta)
        if resposta > len (cartelas_jogo):
          raise ValueError

      # Caso o usuário digite um número errado (que não seja de nenhuma cartela), fazer a verificação e pedir de novo
      except ValueError:
        resposta = input ("O valor digitado é invalido, digite outro valor.")
        continue

      atual = resposta - 1

    # Atualizar as cartelas de modo a saber se alguma venceu (enquanto nenhuma vencer) e imprimir na tela
    # Fazer a distinção de qual cartela é do jogador
    for i in range (4):
      if i == atual:
        print (f"Cartela {i + 1} >> ", end = " ")

      # Fazer a distinção de quais são as demais cartelas
      else:
        print (f"Cartela {i + 1} -- ", end = " ")

      # Armazenar em um array os números sorteados já marcados nas cartelas
      for j in range (len (cartelas_jogo [i])):
        if int (cartelas_jogo [i] [j]) == receba [iter_sort]:
          verdadeiros .append (cartelas_jogo [i] [j])
          boolean_cartelas [i] [j] = True

      # Percorrer toda a cartela e verificar se o número sorteado está em alguma das cartelas
      for n in range (len (cartelas_jogo [i])):
        desigual = ""
        for m in range (len (verdadeiros)):

          # Marcar os números sorteados em suas respectivas posições em todas as cartelas ativas no jogo
          if cartelas_jogo [i] [n] == verdadeiros [m] and cartelas_jogo [i] [n] != desigual:
            print (f"*{cartelas_jogo [i] [n]}*", end = " ")
            desigual = cartelas_jogo [i] [n]

        # Se o número que percorreu não foi sorteado (ainda), imprimir na tela o número normal
        if cartelas_jogo [i] [n] != desigual:
          print (f"{cartelas_jogo [i] [n]}", end = " ")

      print ("\n")

      # Se todos os números de uma cartela forem marcados, declarar a cartela como "vencedora"
      if all (boolean_cartelas [i]):
          vencedora = i

    iter_sort += 1

    # Se o usuário vencer o jogo, coletar os dados para colocar na lista de vencedores
    if vencedora != -1:
      print (f"####### CARTELA VENCEDORA: {vencedora+1} #######\n")
      mostrar_cartelas (cartelas_jogo [vencedora])
      print ("\n")
      if vencedora == atual:
        print ("Parabens! Você Ganhou!")
        nome = input ("Digite seu nome: ")
        data = input ("Digite o dia de hoje (DD/MM/AAAA): ")
        hora = input ("Digite a hora de agora (HH:MM): ")
        vencedores .write (f"{nome}, ganhou às {hora} do dia {data}\n")

      # Se o usuário perder, imprimir uma frase de efeito
      else:
        print (f"{perdeu}\n")

      # Repetir o jogo enquanto o jogador quiser jogar, 1 para continuar e 0 para sair
      while True:
        try:
          continuar = int (input ("Quer jogar de novo? (Sim: 1, Não: 0): "))
          if continuar == 2:
            print("******* Parabens, você desbloqueou Bingo2: Definitive Edition *******")
          break

        # Se digitar um número inválido, fazer a correção
        except:
          print ("Por favor, digite um valor válido (1 ou 0): ")

      # Terminar a partida, mas não os jogos
      if continuar == 1:
        repetindo_partida = False

      # Terminar a partida e os jogos
      else:
        repetindo_partida = False
        repetindo_jogos = False

    # Caso o jogador deseje mudar de cartela
    else:
      resposta = input ("Digite o número da cartela que deseja prosseguir o jogo: ")
      print ("\n\n")

  # Fechar os arquivos txt
  cartelas .close ()
  vencedores .close ()

repetindo_jogos = False
