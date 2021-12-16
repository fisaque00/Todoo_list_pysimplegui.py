#importando pysimplegui
from tkinter import Event
import PySimpleGUI as sg

#criando layout
def criar_janela_inicial():
    sg.theme('Dark Blue 4')
    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas',layout=linha,key='container')],
        [sg.Button('Nova Tarefa'),sg.Button('Resetar')]
    ]

    return sg.Window('Todo List',layout=layout,finalize=True)

#criando a janela
janela = criar_janela_inicial()
#criar as regras dessa janela
while True:
    Event, values = janela.read()
    if Event == sg.WIN_CLOSED:
        break
    elif Event == 'Nova Tarefa':
        janela.extend_layout(janela['container'],[[sg.Checkbox(''),sg.
        Input('')]])
    elif Event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()