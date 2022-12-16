# O programa projetado tem o intuito de trazer uma imersão ao jogador em um jogo que os possíveis finais dependem das escolhas do usuário.

# função input utilizada para que o usuário informe ao programa algum dado

# No primeiro bloco,o usuário digta seu nome e o programa armazena a informação na variável nome. Em sequência a função print mostra ao usuário a indrodução da história.

from time import sleep

# função sleep utizada como temporizador para iniciar a próxima frase

# bloco 1
nome = input('Digite seu nome: ')
sleep(1)

# função from import utilizada para importar a função desejada
print('Era uma vez', nome,
      'ele(a) acordou muito empolgado(a), pois depois de sua aula iria comprar uma guitarra que viu em promoção em uma loja.')
sleep(7)

# função print utilizada para mostrar ao usuário uma mensagem
print(nome, 'está atrasado(a) para a escola e está preocupado(a) pois tem uma prova para fazer nesse dia.')
sleep(6)

# randint utilizado para sortear um número inteiro
from random import randint

# No segundo bloco, utilizamos listas para formar uma matriz 2x2, nesta matriz são armazenados os possíveis caminhos que o usuário deve escolher para chegar até a escola. Em seguida com a função randint o caminho correto é sorteado e armazenado na variável N.

# bloco 2
M = []

# range utilizado para limitar o valor dentro de um intervalo
for i in range(2):

    M = M + [[]]

    for j in range(2):
        N = randint(1, 4)

        M[i] = M[i] + [N]

p = int(input('Escolha um caminho de 1 a 4 para descobir se ele(a) conseguiu chegar a tempo para fazer a prova: '))

# if é uma condição que se for verdadeira o programa seguirá esse caminho

# No bloco 3,o programa verifica se a resposta está correta com o comando if, se o usuário acertar o caminho, em seguida ele resolvera uma equação de segundo grau.

# bloco 3
if p == M[0][1] or p == M[1][0] or p == M[1][1]:

    # int converte o dado para um número inteiro
    print(nome, "conseguiu chegar a tempo para fazer a prova.")
    sleep(2)

    print(nome,
          "está na última questão da prova e está preocupado(a) com o horário pois a loja de guitarras fecha às 18 horas e já são 17:45.")

    sleep(7)

    print("Ele(a) depende de acertar a resposta na primeira tentativa para conseguir pegar a loja aberta.")

    sleep(6)

    import math

    # com a utilização dos colchetes formamos uma lista
    coe = [(1, -3, -10), (1, -5, 6), (2, 12, 18)]

    # * ultizado para importar todas as funções de random
    from random import *

    # função choice escolhe um n° dentro da sequêcia
    p = choice(coe)

    a = p[0]

    b = p[1]

    c = p[2]

    x = (b ** 2) + ((-4) * a * c)

    print('Resolva a equação de segundo grau com os respectivos coeficientes: ')

    print('a:', a)

    print('b:', b)

    print('c:', c)

    x1 = (-b + (x ** (1 / 2))) / (2 * a)

    x2 = (-b - (x ** (1 / 2))) / (2 * a)

    sleep(5)

    # float, o dado informado é convertido para um número de ponto flutuante
    R1 = float(input('Digite a resposta da primeira raíz: '))

    R2 = float(input('Digite a resposta da segunnda raíz: '))

    # No bloco 4, ocorre uma verificação das raízes digitadas pelo usuário com o gabarito.

    # bloco 4
    if R1 == x1 and R2 == x2:

        print(nome, 'consegue resolver a questão e pode sair da sala de aula.')

        sleep(3)

        print(nome,
              "está indo para a loja com um cartão em cada bolso. Um dos cartões está com o limite estourado e outro com crédito.")

        sleep(6)
        # No bloco cinco os bolsos são armazenados em uma lista e com randint um dos bolsos é sorteado, em seguida se a resposta do usuário for igual a do programa a história se encaminha para a compra da guitarra, caso a resposta esteja errada o usuário não poderá comprar a guitarra.

        # bloco 5
        from random import randint

        B = ['bolso direito', 'bolso esquerdo']

        # str,comando utilizado para transformar um dado em uma  sequência de caracteres
        e = str(input(
            "Um ladrão avista ele(a) e irá assaltá-lo(la). Escolha se o ladrão irá furtar o 'bolso direito' ou o 'bolso esquerdo': "))

        F = randint(0, 1)

        o = (B[F])

        # O comando lower é utilizado para transformar todas a sequência de caracteres em letras minúsculas
        if o == e.lower():

            print('O ladrão levou o cartão com o limite estourado.', nome, 'conseguirá comprar a guitarra.')

        # else é utilizado se nenhuma condição for seguida
        else:

            print('O ladrão levou o cartão com crédito.', nome,
                  'terá que voltar para casa e não conseguirá comprar a guitarra.')
    # No bloco 6, os prints contam a história e mostram as alternativas da questão ao usuário. Com o comando str os dados são transformados para caracteres.

    # bloco 6
    else:

        print(nome, 'erra a questão e não conseguirá pegar a loja aberta.')

        sleep(3)

        print('Ele(a) e mais uma pessoa terão que ficar na sala de aula para fazer a prova de recuperação.')

        sleep(5)

        print(nome,
              'olha para seu lado na sala de aula e descobre que quem ficou de recuperação junto com ele(a) é a pessoa em que é apaixonado(a).')

        sleep(6)

        print(
            'A prova de recuperação tem só uma questão. Assinale a alternativa que completa a frase: a equação do 2° grau 2x³-5x=3')
        sleep(6)
        print('(a) admite duas raízes inteiras.')
        sleep(1)

        print('(b) admite uma raiz natural.')
        sleep(1)

        print('(c) não admite raízes reais.')
        sleep(1)

        print('(d) admite duas raizes naturais.')
        sleep(1)

        print('(e) admite duas raízes negativas.')

        ala = str('a')

        alb = str('b')

        alc = str('c')

        ald = str('d')

        ale = str('e')
        sleep(1)

        res = input('Qual alternativa você escolhe? ')

        if res == alb:

            print(nome, 'passou na prova de recuperação.')
            sleep(2)

            print('Logo após a prova,', nome,
                  'e a pessoa de quem gostava ficaram conversando e rolou química. Depois de meses começaram a namorar.')

        else:

            print(nome, 'acabou reprovando.')
            sleep(2)

            print('A pessoa de quem era apaixonado(a) acabou passando de ano, logo', nome,
                  'perdeu a chance de se aproximar de quem gostava.')





# Com a função elif o programa verifica todas as condições digitadas, caso as mesmas se confirmem o usuário errou o caminho.

# bloco 7
elif p == M[0][0] or p != M[0][0] and p != M[0][1] and p != M[1][0] and p != M[1][1]:

    print(nome, "escolheu um caminho que havia muito trânsito e acabou se atrasando.")

    sleep(3)

    print(
        'Ele(a) não conseguiu entrar na sala de aula para fazer a prova, então saiu do colégio e foi jogar bola com os amigos em um campo nas proximidades.')

    sleep(7)

    print('Nesse campinho haviam algumas pessoas olhando o jogo, dentre elas um olheiro do Juventude.')

    sleep(5)

    print(nome, 'estava jogando muito bem e iria bater um pênalti. O olheiro ainda estava em dúvida, porém se', nome,
          'acertasse o pênalti, iria ser contradado(a).')

    sleep(7)
    # O último bloco funciona exatamente como o bloco 5, contudo o resultado final da história é diferente.

    # bloco 8
    from random import randint

    B = ['canto direito', 'canto esquerdo']

    e = str(input(
        "A goleira era pequena, logo se o goleiro escolhesse o canto certo, ele defenderia. Escolha se ele(a) bateu o pênalti no 'canto direito' ou no 'canto esquerdo': "))

    F = randint(0, 1)

    o = (B[F])

    if o == e.lower():

        print(nome, 'conseguiu marcar o gol e o olheiro decidiu contratá-lo(la).')
        sleep(4)

        print(nome,
              'foi para a sua casa com o olheiro para falar com seus pais. Ele(a) ficou tão feliz que acabou esquecendo de comprar a guitarra.')

    else:

        print(nome, 'errou o pênalti, logo o olheiro não quis contratá-lo(la).', nome, 'continuou jogando bola')
        sleep(4)

        print(nome,
              'acabou ficando sem a guitarra, sem uma boa nota na escola, acabou perdendo a partida e a chance de se tornar jogador(a) profissional.')
