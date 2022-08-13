# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 18:46:46 2022

@author: Juliano
"""

#Calculadora de juros simples

import os

print('Informe os dados para o cálculo dos juros')

capital = float(input('Capital: '))

taxa = float(input('Taxa de juros: '))

tempo = float(input('Tempo: '))

juros = capital * taxa * tempo / 100

print('O valor dos juros é', juros)

os.system('pause')