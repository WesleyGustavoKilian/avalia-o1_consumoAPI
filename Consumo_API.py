import webbrowser
import requests  
import tkinter as tk 
from tkinter import ttk  
from tkinter import messagebox  

class ConsultaCEP:
    def __init__(self, cep):
        self.cep = cep.replace("-", "").replace(" ", "") # Remove qualquer caractere "-" ou espaço em branco do CEP e formata para manter somente os dígitos
        self.url = f"https://viacep.com.br/ws/{self.cep}/json/"  

    def validar_cep(self):
        if len(self.cep) == 8 and self.cep.isdigit():  # Verifica se o CEP possui 8 dígitos numéricos
            return True
        else:
            return False

    def consultar(self):
        if self.validar_cep():  # Verifica se o CEP é válido
            resposta = requests.get(self.url)  # Faz uma solicitação GET para a API 
            if resposta.status_code == 200:  # Verifica se a solicitação foi bem-sucedida
                dados = resposta.json()  # Converte a resposta JSON em um dicionário Python
                if "erro" not in dados:  # Verifica se não houve erro na resposta
                    return dados  # Retorna os dados do CEP
                else:
                    return "CEP inválido ou não encontrado."  
            else:
                return "Não foi possível obter dados da API."  
        else:
            return "CEP inválido. Deve conter 8 dígitos numéricos."  

def consultar_cep(event=None):  # Adiciona um parâmetro opcional para lidar com eventos de teclado (ENTER)
    cep = cep_entry.get()  # Obtém o CEP digitado pelo usuário
    consulta = ConsultaCEP(cep)  # Cria uma instância da classe ConsultaCEP
    dados = consulta.consultar()  # Chama o método consultar para obter os dados do CEP
    resultado_tree.delete(*resultado_tree.get_children())  # Limpa a TreeView antes de exibir os novos resultados
    if isinstance(dados, dict) and "erro" not in dados:  # Verifica se os dados são um dicionário válido e se não contêm erro
        values = (
            dados.get("cep", ""), 
            dados.get("logradouro", ""), 
            dados.get("bairro", ""), 
            dados.get("localidade", ""), 
            dados.get("uf", ""), 
            dados.get("ibge", ""),  
            dados.get("ddd", ""), 
        )
        resultado_tree.insert("", "end", values=values)  # Insere os valores na TreeView
        
        # Centraliza os itens em cada coluna
        for col in resultado_tree["columns"]:
            resultado_tree.heading(col, anchor=tk.CENTER)  
            resultado_tree.column(col, anchor=tk.CENTER)  
    else:
        resultado_tree.insert("", "end", values=("CEP inválido ou não encontrado.", "", "", "", "", "", "", ""))  # Exibe uma mensagem de erro na TreeView

def ver_no_maps():
    cep = cep_entry.get().strip()  # Obtém o CEP digitado pelo usuário e remove espaços em branco
    if cep:  # Verifica se o campo do CEP não está vazio
        consulta = ConsultaCEP(cep)  # Cria uma instância da classe ConsultaCEP
        dados = consulta.consultar()  # Chama o método consultar para obter os dados do CEP
        if isinstance(dados, dict) and "erro" not in dados:  # Verifica se os dados são um dicionário válido e se não contêm erro
            # Formata a URL do Google Maps com base nos dados de latitude e longitude do CEP
            url = f"https://www.google.com/maps/search/?api=1&query={dados['localidade']},{dados['uf']}"
            webbrowser.open_new_tab(url)  # Abre a URL no navegador padrão
        else:
            messagebox.showerror("Erro", "CEP inválido ou não encontrado.")
    else:
        messagebox.showinfo("Aviso", "Digite o CEP desejado.")

def nova_consulta():
    cep_entry.delete(0, 'end')  # Limpa a caixa de entrada do CEP
    resultado_tree.delete(*resultado_tree.get_children())  # Limpa a TreeView
    cep_entry.focus()  # Coloca o foco de volta na caixa de entrada do CEP

root = tk.Tk()  # Cria a janela principal
root.title("Consulta CEP")  # Define o título da janela
root.configure(bg='#f0f0f0')  # Define a cor de fundo da janela (cinza claro)

cep_label = tk.Label(root, text="Digite o CEP:", bg='#f0f0f0', fg='black')  # Cria um rótulo para solicitar o CEP
cep_label.pack(pady=10)  

cep_entry = tk.Entry(root)  # Cria uma caixa de entrada para o CEP
cep_entry.pack(pady=10) 
cep_entry.focus()  # Define o foco inicial na caixa de entrada do CEP

# Adiciona um evento de teclado para a caixa de entrada do CEP
cep_entry.bind("<Return>", consultar_cep)

# Cria um botão "Consultar" que chama a função consultar_cep quando clicado
consulta_button = tk.Button(root, text="Consultar", command=consultar_cep, bg='#4CAF50', fg='white', relief='raised')  
consulta_button.pack(pady=10)  

# Cria um botão "Ver no Maps" que chama a função ver_no_maps quando clicado
ver_no_maps_button = tk.Button(root, text="Ver no Maps", command=ver_no_maps, bg='#2196F3', fg='white', relief='raised')  
ver_no_maps_button.pack(pady=10)  

# Cria um botão "Nova Consulta" que chama a função nova_consulta quando clicado
nova_consulta_button = tk.Button(root, text="Nova Consulta", command=nova_consulta, bg='#FFEB3B', fg='black', relief='raised')  
nova_consulta_button.pack(pady=10)  

# Cria uma TreeView para exibir os resultados da consulta de CEP
resultado_tree = ttk.Treeview(root, columns=("CEP", "Logradouro", "Bairro", "Localidade", "UF", "IBGE", "DDD"), show="headings")
resultado_tree.heading("CEP", text="CEP") 
resultado_tree.heading("Logradouro", text="LOGRADOURO") 
resultado_tree.heading("Bairro", text="BAIRRO") 
resultado_tree.heading("Localidade", text="LOCALIDADE") 
resultado_tree.heading("UF", text="UF") 
resultado_tree.heading("IBGE", text="IBGE") 
resultado_tree.heading("DDD", text="DDD") 
resultado_tree.pack(pady=10)  

root.mainloop()  # Inicia o loop principal do tkinter, que mantém a janela aberta 
