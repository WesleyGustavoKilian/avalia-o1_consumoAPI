Araras | SP 
2024


Faculdade de Tecnologia de Araras – Antônio Brambilla
Tecnologia em Desenvolvimento de Software

_________________________________________________________
Wesley Gustavo Kilian


_________________________________________________________

Prof. Orlando Saraiva do Nascimento Junior




CONSUMO APIS COM A LINGUAGEM PYTHON E A BIBLIOTECA REQUESTS.




RESUMO:

Este projeto Python oferece uma interface gráfica simples para consultar informações de CEP (Código de Endereçamento Postal) usando a API do ViaCEP. 

Interface Gráfica: Utiliza o módulo tkinter para criar uma interface amigável onde os usuários podem inserir um CEP.

Consulta de CEP: Ao inserir um CEP e clicar no botão "Consultar", o programa faz uma solicitação HTTP à API do ViaCEP para obter informações sobre o endereço correspondente.

Exibição dos Resultados: Os dados do endereço, como logradouro, bairro, localidade, UF (Unidade Federativa), IBGE e DDD, são exibidos em uma tabela na interface.

Visualização no Google Maps: Além disso, há um botão "Ver no Maps" que, quando clicado, abre o navegador padrão com a localização do CEP no Google Maps.

Feedback para o Usuário: O programa fornece feedback em caso de CEP inválido ou se não foram encontradas informações para o CEP fornecido.



 
Principais elementos e comandos utilizados no código para criar uma aplicação funcional de consulta de CEP com interface gráfica:


Importações de Módulos:

import webbrowser: Importa o módulo webbrowser para abrir URLs no navegador padrão.
import requests: Importa o módulo requests para fazer solicitações HTTP.
import tkinter as tk: Importa o módulo tkinter para criar uma interface gráfica e o renomeia como tk para facilitar a referência.
from tkinter import ttk: Importa ttk do tkinter para usar widgets temáticos.
from tkinter import messagebox: Importa messagebox do tkinter para exibir mensagens.

Classe ConsultaCEP:

_init_: Método inicializador da classe que recebe um CEP como argumento, formata o CEP e define a URL da API do ViaCEP.
validar_cep: Método para validar se o CEP possui 8 dígitos numéricos.
consultar: Método para fazer a consulta à API do ViaCEP e retornar os dados do CEP.

Funções:

consultar_cep: Função para lidar com a consulta do CEP, chamando os métodos adequados da classe ConsultaCEP e atualizando a interface gráfica com os resultados.
ver_no_maps: Função para abrir a localização do CEP no Google Maps, usando a API do ViaCEP para obter os dados de latitude e longitude.
nova_consulta: Função para limpar a entrada do CEP e a exibição dos resultados, permitindo uma nova consulta.



Interface Gráfica:

tk.Tk(): Cria a janela principal.

tk.Label(): Cria rótulos de texto na interface.

tk.Entry(): Cria caixas de entrada de texto.

tk.Button(): Cria botões com funcionalidades específicas.

ttk.Treeview(): Cria uma tabela para exibir os resultados da consulta de CEP.

root.mainloop(): Inicia o loop principal do tkinter, mantendo a janela aberta e respondendo às interações do usuário.




