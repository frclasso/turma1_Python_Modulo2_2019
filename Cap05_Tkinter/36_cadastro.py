from tkinter import  *

janela = Tk()

janela.geometry("400x400+100+100")
janela.title("Cadastro de usuarios")


dados = []

def inclui():
    salvadados()

def salvadados():
    nome = ed1.get()
    sobrenome =ed2.get()
    email = ed3.get()

    lb2['text'] = nome+','+sobrenome+','+email

    dados_recebidos = [nome+','+sobrenome+','+email+'\n']
    dados.append(dados_recebidos)
    exporta_dados()

def clear_label():
    lb2['text'] = 'Voce apagou os dados'
    clear_text()

def clear_text():
    return ed1.delete(0, 'end'), ed2.delete(0, 'end'),ed3.delete(0, 'end')

def exporta_dados():
    with open('dados.csv','a') as f:
        for data in dados:
            f.writelines(data)

def close_window():
    janela.destroy()


lb1 = Label(janela, text="Nome")
lb1.place(x=100, y=80)
ed1 =Entry(janela)
ed1.place(x=100, y=100)

lb2 = Label(janela, text="Sobrenome")
lb2.place(x=100, y=130)
ed2 =Entry(janela)
ed2.place(x=100, y=150)

lb3 = Label(janela, text="email")
lb3.place(x=100, y=180)
ed3=Entry(janela)
ed3.place(x=100, y=200)

bt = Button(janela, width=20, text='Salvar', command=inclui)
bt.place(x=100, y=230)

bt2 = Button(janela, width=20, text='Limpar', command=clear_label)
bt2.place(x=100, y=260)

bt3 = Button(janela, width=20, text='Sair', command=close_window)
bt3.place(x=100, y=300)

lb2 = Label(janela, text='Dados do cliente')
lb2.place(x=140, y=330)

janela.mainloop()