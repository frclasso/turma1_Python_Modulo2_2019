
from tkinter import *

window = Tk()
window.title('Shapes')

# canvas => tela de desenho
canvas = Canvas(window, width=500, height=500)
canvas.pack()

# desenhar linha
line1 = canvas.create_line(25, 25, 250, 150, fill='blue')
line2 = canvas.create_line(25, 250, 250, 150, fill='blue')

# desenhar retangulo
rect = canvas.create_rectangle(500, 25, 175, 75, fill='green')

# deletar
#canvas.delete(line1)

# deletar tudo
canvas.delete(ALL)




window.mainloop()