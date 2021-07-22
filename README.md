# SLR vs LALR

Trabalho da disciplina Compiladores 2021.1

Data de entrega 23/07/21

## Introdução 

A gramática 
```BNF
S -> L = R | R
L -> * R | id
R -> L
```
não é ambígua. É LALR mas não SLR. (Veja os slides do curso sobre parsing ascendente a partir do slide 13.)

## Objetivo

Mostre na prática que a tabela de parsing SLR é ambigua e que a LALR não é utilizando o gerador de analisador sintático PLY, 
uma implementação em Python da ferramenta Yacc. 

## Implementação

1. Implemente o analisador léxico e o sintático da gramática acima em PLY no arquivo `slrvslalr.py`.
2. Estude PLY e descubra como:
   - escolher entre SLR ou LALR como algoritmo para construção da tabela de parsing;
   - demonstrar, utilizando os arquivos gerados por PLY, que a tabela SLR possui um conflito e a LALR não. 
     Produza um pequeno relatório, em `slrvslalr.pdf`, explicando sua demonstração. 
   - Seu relatório deve:
     1. estar corretamente identificado com seu nome e data, 
     2. descrever o problema, e
     3. mostrar como este problema fica reportado pela ferramenta PLY.


