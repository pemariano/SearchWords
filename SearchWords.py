RETANG = []
with open("matriz.txt", "r") as arq:
    for linha in arq:
        linha = linha.replace("\n", "").split(" ")
        RETANG.append([int(x) for x in linha])
'''Le o arquivo e monta uma matriz com eles'''

lin = len(RETANG)    # numero de linhas da matriz 
col = len(RETANG[0]) # numero de colunas da matriz


def imprime_matriz(RETANG):
    '''Imprime a matriz de forma organizada'''
    print("Matriz {}x{}: ".format(lin, col))
    for linha in RETANG:
        for coluna in linha:  # nesse for imprime uma linha
            print("{}".format(coluna).rjust(2), end="")
        print()  # pula linha


def ProcuraPrimeiroNumero(RETANG, PADRAO, i, j):
    '''Apenas procura em ordem lexicografica o primeiro numero do padrao dentro da matriz.'''
    for p in range(i, lin):
        if p == i:
            for q in range(j, col):
                if PADRAO[0] == RETANG[p][q]:
                    return p, q
        else:
            for q in range(0, col):
                if PADRAO[0] == RETANG[p][q]:
                    return p, q
    return -1


def VerificaSeCabe(RETANG, t, r, i, j):
    '''numero de linhas/colunas - posicao em relacao a linha/coluna e +1 caso esteja no sentido da contagem de índices da matriz
       nas diagonais tem que juntar as duas condições dos eixos principais pertinentes'''
    if r == 11:
        if i + 1 >= t:
            return 1
        return 0
    if r == 22:
        if col - j >= t:
            return 1
        return 0
    if r == 33:
        if lin - i >= t:
            return 1
        return 0
    if r == 44:
        if j + 1 >= t:
            return 1
        return 0
    if r == 12:
        if i + 1 >= t and col - j >= t:
            return 1
        return 0
    if r == 32:
        if lin - i >= t and col - j >= t:
            return 1
        return 0
    if r == 34:
        if lin - i >= t and j + 1 >= t:
            return 1
        return 0
    if r == 14:
        if j + 1 >= t and i + 1 >= t:
            return 1
        return 0


def AchaPADRAO(RETANG, PADRAO, r, i, j):
    '''Esta funcao cria uma lista a partir de um ponto dado (i,j) numa direcao (r) e a compara com o padrao
       Quando a direcao e contraria ao sentido de indices da matriz o passo do range e -1'''
    if r == 11:
        linha = [RETANG[k][j] for k in range(i, i - len(PADRAO), -1)]
        return linha == PADRAO
    if r == 22:
        linha = [RETANG[i][l] for l in range(j, j + len(PADRAO))]
        return linha == PADRAO
    if r == 33:
        linha = [RETANG[k][j] for k in range(i, i + len(PADRAO))]
        return linha == PADRAO
    if r == 44:
        linha = [RETANG[i][l] for l in range(j, j - len(PADRAO), -1)]
        return linha == PADRAO
    if r == 12:
        linha = [RETANG[k][l] for l, k in zip(range(j, j + len(PADRAO)), range(i, i - len(PADRAO), -1))]
        return linha == PADRAO
    if r == 32:
        linha = [RETANG[k][l] for l, k in zip(range(j, j + len(PADRAO)), range(i, i + len(PADRAO)))]
        return linha == PADRAO
    if r == 34:
        linha = [RETANG[k][l] for l, k in zip(range(j, j - len(PADRAO), -1), range(i, i + len(PADRAO)))]
        return linha == PADRAO
    if r == 14:
        linha = [RETANG[k][l] for l, k in zip(range(j, j - len(PADRAO), -1), range(i, i - len(PADRAO), -1))]
        return linha == PADRAO


def Final(RETANG, PADRAO, t, i, j):
    '''Esta funcao e recursiva, chama as outras funcoes uma a uma, caso todas as condicoes forem vencidas ela já imprime o padrão, o inicio do mesmo e sua direcao.
       Caso não ache o padrao a funcao ja informa o usuario que o padrao nao aparece na matriz'''
    direcoes = [11, 22, 33, 44, 12, 32, 34, 14]
    direcoes2 = ["norte", "leste", "sul", "oeste", "nordeste", "sudeste", "sudoeste", "noroeste"]
    l = False
    if ProcuraPrimeiroNumero(RETANG, PADRAO, i, j) != -1:
        p, q = ProcuraPrimeiroNumero(RETANG, PADRAO, i, j)
        for r in direcoes:
            if VerificaSeCabe(RETANG, t, r, p, q) == 1:
                if AchaPADRAO(RETANG, PADRAO, r, p, q):
                    for u in range(8):
                        if direcoes[u] == r:
                            h = direcoes2[u]
                    if t == 1:
                        print("Padrao {} esta em ({},{}).".format(PADRAO, p, q))
                        print()
                    else:
                        print("Padrao {} começa em ({},{}) com direcao {}.".format(PADRAO, p, q, h))
                        print()
                    l = True
                    break
        #Achou no minimo o primeiro numero mas nao achou o padrao.
        if q != col - 1 and not l:                    #Aqui e no proximo if o programa continua a rodar no resto da matriz.
            Final(RETANG, PADRAO, t, p, q + 1)        #Recursividade.
            l = True                                  #Ao chamar a funcao 2,3 vezes e achar em uma destas o l vira True, mas so na chamada 2,3. Aqui faco o l=True para a primeira chamade de Final.
        if q == col - 1 and p != lin - 1 and not l:   #As condicoes dos ifs correspondem a onde o programa parou.
            Final(RETANG, PADRAO, t, p + 1, 0)
            l = True
    if l == False:                                    #Se o programa roda ate a ultima casa e nao acha o padrao cai aqui.
        print("Padrão {} nao ocorre.".format(PADRAO))
        print()


def main():
    print()
    print("Bem vindo, este programa recebe uma matriz via arquivo salvo como: matriz.txt que esteja na pasta do mesmo e checa se os padroes inseridos pelo usuario aparecem na matriz (sera perguntando quantos padroes deseja buscar). Caso aparecam, o programa imprime a posicao inicial do padrao e sua direcao. Se o padrao nao for encontrado o programa informa ao usuario que o padrao nao se encontra na matriz.")
    print()
    n = int(input("Digite quantos padroes deseja testar: "))
    print()
    imprime_matriz(RETANG)
    print()
    while n > 0:
        PADRAO = [int(x) for x in input("Entre com o padrao: ")]
        t = len(PADRAO)
        x = Final(RETANG, PADRAO, t, 0, 0)
        n -= 1


main()