# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:27:42 2017

@author: Diogo Monteiro
"""

#import numpy
import time

cards =[]
lset = 0

cards.append(['bb1', 123456789, 303, 3000, 10, 2020, 10, 3000])
cards.append(['itau1', 741852963, 555, 5000, 10, 2022, 6, 5000])
cards.append(['bra1', 852456963, 911, 1000, 7, 2019, 3, 1000])
wallet_max = sum(row[3] for row in cards)

def insert ():
     name = input('Insira o nome do cartão: ')
     number = input('Insira o número do cartão: ')
     safe = input('Insira o código de segurança do cartão: ')
     limit = input('Insira o limite de crédito: ')
     duedate = input('Insira a data de vencimento (dia do mês): ')
     expdate = input('Insira a data de validade (MM/YYYY): ')
     expmonth = expdate.split('/')[0]
     expyear = expdate.split('/')[1]
     steplist = [name, number, safe, limit, duedate, expdate, expmonth, expyear, limit]
     return cards.append(steplist)
     global wallet_max
     wallet_max = sum(row[3] for row in cards)
 
    
def show_all():
    print('\n')
    print ('Nome \t| Número \t| Código de Segurança \t| Limite \t\t| dia de vencimento \t| Data de validade')
    for c in range(0, len(cards)): 
        print('\n')
        print('%s \t| %d \t| %d \t\t\t| R$ %d,00 \t\t| %d \t\t\t| %02d/%d' %(cards[c][0],  cards[c][1], cards[c][2], cards[c][3], 
                                                               cards[c][4], cards[c][6], cards[c][5])) 
        
def delete():
    print('\n')
    print ('Nome \t| Número')
    for c in range(0, len(cards)): 
        print('%s \t| %d ' %(cards[c][0],  cards[c][1]))
    n = int(input('Por favor insira o número do cartão que deseja remover da carteira: '))
    for c in range(0, len(cards)):
        if n == cards[c][1]:
            i = c
            break
        else:
            i = -1
    if i >= 0:          
        del cards[i]
        print('Cartão cancelado.')
    else:
        print('Este númedo de cartão não consta na carteira.')
  
    
def set_limit():
    global lset
    while 1 == 1:
        lset = int(input('Escolha o limite do cartão (o limite máximo é R$ %d,00 ): ' %wallet_max ))
        if lset > wallet_max :
            print('\n')
            print('O limite estabelecido não pode ser superior ao limite máximo')      
        else:
            print('\n')
            print('O limite máximo estabelecido é: R$ %d,00' %lset) 
            break

def show_lset():  
    print('Limite escolhido: R$ %d,00 ' %lset )
    
def show_lmax():
    global wallet_max
    wallet_max = sum(row[3] for row in cards)
    print(' Limite máximo: R$ %d,00' %wallet_max )
    

dia =  (time.strftime("%d"))  

def credit():
    for c in range(0, len(cards)): 
        if dia == cards[c][6]:
            cards[c][7] = cards[c][3]
        else:
            pass
    credit = lset - (sum(row[3] for row in cards) - sum(row[7] for row in cards))
    print ('Credito disponível: %d' %credit)
    
def buy():
    buy_cards = []
    range_days = []
    small_limit = []
    buy_day =  int(time.strftime("%d")) 
    valor_compra = int(input('Valor da compra: '))
    for c in range(0, len(cards)):
        if valor_compra <= cards[c][3]:
            buy_cards.append(cards[c])
        else:
            pass
    for c in range(0, len(buy_cards)):  
       if buy_cards[c][4] - buy_day < 0:
              range_days.append(30 - (buy_cards[c][4] - buy_day))
       else:
              range_days.append(buy_cards[c][4] - buy_day)
    max_value = max(range_days)
    max_index = [i for i, j in enumerate(range_days) if j == max_value]
    if len(max_index) == 1:
        chosen_one = buy_cards[max_index[0]]
    else:
        for c in range(0, len(max_index)):  
            small_limit.append(buy_cards[max_index[c]])
        min_value = max(small_limit)
        min_index = [i for i, j in enumerate(small_limit) if j == min_value]
        chosen_one = small_limit[min_index[0]]
        # testar com dois cartôes com mesma data e mesmo limite, depois abater a compra do limite do cartão escolhido
    print(chosen_one)    
    print(buy_cards)
    print (range_days)