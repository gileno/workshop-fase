import time
import tkinter
'''Código baseado em uma palestra Ministrada por Luciano Ramalho.'''
app = tkinter.Tk()
app.title("Meu primeiro relógio")

hora = tkinter.StringVar()
hora.set('00:00:00')
rel = tkinter.Label(app, font='Helvetica 120', textvariable=hora)
rel.pack()


def tic_tac():
    '''Atualiza a hora com hora atual do sistema'''
    hora_atual = time.strftime('%H:%M:%S')
    if hora_atual != hora.get():
        hora.set(hora_atual)
    rel.after(100, tic_tac)

tic_tac()
app.mainloop()
