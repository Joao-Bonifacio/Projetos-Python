def first():
    global archive
    archive = True
    #tipo de sala de sinal
    tipo = input('Operações => com Martingale(G) | com mão Fixa(F) | com Soros? (S): ')
    if (tipo == 'g' or tipo == 'G'):
        tipo = '1'
    elif (tipo == 'f' or tipo == 'F'):
        tipo = '2'
    elif (tipo == 's' or tipo == 'S'):
        tipo = '3'
    else:
        tipo = ''
    #com martingale 
    if tipo == '1':
        print("----Operações com Martingale----")
        entrada = float(input('qual o valor da entrada? '))
        payout = int(input('qual o payout? '))
        gale = int(input('O gale é quantas vezes o valor da entrada? '))
        ws = int(input('quantos wins sem gale? '))
        wg = int(input('quantos wins com gale? '))
        hit = int(input('quantos hits? '))
        payout = (payout / 100)
        ws = ws * (entrada * payout)
        wg = wg * (entrada - (entrada * 2)) + (entrada * gale * payout)
        hit = hit * (entrada - (entrada * (gale + 2)))
        calculo = ws + wg + hit
        print('-----Resultado-----')
        print('R$',round(calculo,2))
        print('-------------------')
    #sem martingale
    elif tipo == '2':
        print("----Operações sem Martingale----")
        entrada = float(input('qual o valor da entrada? '))
        payout = int(input('qual o payout? '))
        ws = int(input('quantos wins? '))
        hit = int(input('quantos loss? '))
        payout = (payout / 100)
        ws = ws * (entrada * payout)
        hit = hit * entrada
        calculo = ws - hit
        print('-----Resultado-----')
        print('R$',round(calculo,2))
        print('-------------------')
    #com soros
    elif tipo == '3':
        print("----Operações com Soros----")
        entrada = float(input('qual o valor da entrada? '))
        payout = int(input('qual o payout? '))
        soros = int(input('Quantas mãos de Soros? '))
        payout = (payout / 100)
        calculo = entrada * pow((1 + payout),soros)
        print('-----Resultado-----')
        print('R$',round(calculo,2))
        print('-------------------')
    else:
        archive = False
    global x
    global y
    y = input('Recalcular? (S/N?) ')
    if y == 's' or y == 'S':
        x = first()
    else:
        archive = False

x = first()
while archive == True:
    open