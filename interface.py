"""
Módulo: Interface

Este código será responsável por extrair dados.
Objetivo:
- Criar um código capaz de extrair dados colocados pelo usário.

Com o objetivo concluído, será possível realizar a plotagem de gráfico.

"""


import customtkinter as ctk
from sympy import sympify
from tkinter import END, StringVar

def extração():
    
    #configuração da janela
    ctk.set_appearance_mode('dark')
    window = ctk.CTk()
    window.title('Sistema de extração de dados')
    window.geometry('450x520')

    def conversor(palavra : str): #atualizar depois
        if(palavra != ""):
            try:
                expr = sympify(palavra)
                valor = expr.evalf()

                if not(valor.is_real or valor.is_number):
                    raise ValueError("Valor não numérico.")
        
                return float(valor)
            except ValueError as e:
                print(f"ERROR: {e}")
    
    def validar_variaveis():
        #Esse trecho será utilizado para validar as entradas 'inputadas' pelo usuário
        """
        Esta função irá validar, com o auxílio da função 'conversor', as entradas
        digitadas pelo usuário.
        """
        try:
            Tensao1 = conversor(campo_tensao1.get())
            Te1 = conversor(campo_T1.get())
            Tensao2 = conversor(campo_tensao2.get())
            Te2 = conversor(campo_T2.get())

            if any(v is None for v in [Tensao1, Te1, Tensao2, Te2]):
                raise ValueError("Valor(es) incorreto(s)!")
            verificacao.configure(text="Variáveis aceitas!\n  Executando cálculo...", font = ("Times", 15))
            window.update_idletasks()
            window.after(2000)
            window.destroy()
            coord[:] = [Tensao1, Te1, Tensao2, Te2, False]
            
            #Algoritmo para salvar as variáveis em um arquivo
            with open("default.txt", "w") as arq: #O with garante que o arquivo será fechado
                for c in coord:
                    arq.write(str(c) + '\n') #Escrevendo no arquivo coef.txt

        except ValueError as e:
            window.update_idletasks()
            verificacao.configure(text=f"{e}", font = ("Times", 15))
            return None
    
    def validar_clear():
        """
        Essa função apaga todos os valores digitados nos campos
        """
        campo_tensao1.delete(0,END)
        campo_T1.delete(0,END)
        campo_tensao2.delete(0,END)
        campo_T2.delete(0,END)
    
    def validar_sair():
        """
        Essa função te faz sair da interface
        """

        verificacao.configure(text="Saindo...", font = ("Times", 15))
        window.update_idletasks()
        window.after(2000)
        window.destroy()
        coord[:] = [0, 0, 0, 0, True]
    
    def validar_default():
        """
        Essa função põe valores aos coeficientes de forma automática com valores default.
        """
        arq_def = open("default.txt", "r")
        if((arq_def.readable()) and (arq_def.read(1) != "")):
            print("Arquivo default.txt aberto.")

            arq_def.seek(0)
            entry_Tensao1.set(arq_def.readline().strip())
            entry_T1.set(arq_def.readline().strip())
            entry_Tensao2.set(arq_def.readline().strip())
            entry_T2.set(arq_def.readline().strip())
        else:
            verificacao.configure(text = "Não foi possível ler e extrair os valores do arquivo.", font = ("Times", 15))
        arq_def.close()

    #Criando os campos: 
    #Há 3 campos : 
    # - Label : texto
    # - Entry : entrada
    # - Button : botão

    #Label

    #Essa variável auxiliar serve para dá um pequeno espaço no topo da janela
    texto_auxiliar = ctk.CTkLabel(window, text = '') 
    texto_auxiliar.pack(pady = 2)

    texto_primario = ctk.CTkLabel(window, text = "< Termômetro digital >",
                                  font = ("Times", 20))
    texto_primario.pack(pady = 5)

    texto_secudario = ctk.CTkLabel(window, text = "Digite os valores de tensão e temperatura do diodo: ",
                                  font = ("Times", 15))
    texto_secudario.pack(pady = 5)

    texto_obs = ctk.CTkLabel(window, text = "Observação:\n Não são lidos letras.",
                             font = ("Times", 13))
    texto_obs.pack(pady = 2)


    #Texto auxiliar para demarcar testes:
    texto_auxiliar1 = ctk.CTkLabel(window, text = 'Primeiro Teste') 
    texto_auxiliar1.pack(pady = 5)

     #--------------------------Campo (Tensão1, T1)------------------------------#
    texto_titulo1 = ctk.CTkLabel(window, text = '      Tensão:                     Temperatura:  ',
                                    font = ("Helvenica", 13))
    texto_titulo1.pack(pady = 0)

    #Entry
    #Utilizando a variável linha1 para auxiliar a posição dos campos de entrada A, B e C
    linha1 = ctk.CTkFrame(window)
    linha1.pack(pady = 5)

    #Iniciando variaveis dos campos:
    entry_T1 = StringVar()
    entry_Tensao1 = StringVar()

    entry_T2 = StringVar()
    entry_Tensao2 = StringVar()

    campo_tensao1 = ctk.CTkEntry(linha1, fg_color = ("black"),
                                 textvariable = entry_Tensao1)
    campo_T1 = ctk.CTkEntry(linha1, fg_color = ("black"),
                            textvariable = entry_T1)
    
    campo_tensao1.grid(row = 0, column = 0, padx = 5, pady = 5)
    campo_T1.grid(row = 0, column = 1, padx = 5, pady = 5)

    #Texto auxiliar para demarcar testes:
    texto_auxiliar1 = ctk.CTkLabel(window, text = 'Segundo Teste') 
    texto_auxiliar1.pack(pady = 5)

     #--------------------------Campo (Tensão1, T1)------------------------------#
    texto_titulo2 = ctk.CTkLabel(window, text = '      Tensão:                     Temperatura:  ',
                                    font = ("Helvenica", 13))
    texto_titulo2.pack(pady = 0)

    #Utilizando a variável linha2 para auxiliar a posição dos campos de entrada D, E e F
    linha2 = ctk.CTkFrame(window)
    linha2.pack(pady = 5)

    campo_tensao2 = ctk.CTkEntry(linha2, fg_color = ("black"),
                                 textvariable = entry_Tensao2)
    campo_T2 = ctk.CTkEntry(linha2, fg_color = ("black"),
                            textvariable = entry_T2)
    
    campo_tensao2.grid(row = 0, column = 0, padx = 5, pady = 5)
    campo_T2.grid(row = 0, column = 1, padx = 5, pady = 5)

    #Button
    #Utilizando a variável linha3 para auxiliar a posição dos botões

    linha3 = ctk.CTkFrame(window)
    linha3.pack(pady = 5)

    #Criando o botão Executar
    botao_executar = ctk.CTkButton(linha3, text = 'Executar',
                                    command = validar_variaveis,
                                    hover_color = 'green',
                                    corner_radius = 50)

    #Criando o botão Limpar
    botao_limpar = ctk.CTkButton (linha3, text = 'Limpar campos',
                                command = validar_clear,
                                hover_color = 'darkblue',
                                corner_radius = 50)
    
    #Criando o botão Sair
    botao_sair = ctk.CTkButton (linha3, text = 'Sair',
                                command = validar_sair,
                                hover_color = 'red',
                                corner_radius = 50)
    
    #Criando o botão Default
    botao_default = ctk.CTkButton(linha3, text = "Default",
                                  command = validar_default,
                                  corner_radius = 50)

    botao_executar.grid(row = 0, column = 0, padx = 5, pady = 8)
    botao_limpar.grid(row = 0, column = 1, padx = 5, pady = 8)
    botao_default.grid(row = 0, column = 2, padx = 5, pady = 8)
    botao_sair.grid(row = 1, column = 1, padx = 5, pady = 5)

    #Feedback dos botões botão_calcular e botao_sair
    verificacao = ctk.CTkLabel(window, text = '')
    verificacao.pack(pady = 5)
    coord = []

    #inicia a aplicação
    window.mainloop()

    #Esse trecho retorna todos os coeficientes necessários
    return tuple(coord)