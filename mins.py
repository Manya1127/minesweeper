from tkinter import *
import configure
import new
import unit
from unit import Cell

root = Tk()
root.configure(bg="black")
root.geometry(f'{configure.width}x{configure.height}')
root.title("Minesweeper game")  

root.resizable(False, False)

top_frame = Frame(root,
                  bg="grey",
                  width=configure.width,
                  height=new.height_prct(25))  # assuming you meant 'height_prct' instead of 'height_perct'
top_frame.place(x=0, y=0)

game_title = Label(top_frame,
                   bg="#5D6D7E",
                   fg="white",
                   text="Minesweeper Game",
                   font=('', 48))
game_title.place(x=new.width_prct(30), y=0)

centre_frame = Frame(root,
                     bg="black",
                     width=new.width_prct(75),
                     height=new.height_prct(75))
centre_frame.place(x=new.width_prct(30), y=new.height_prct(30))



for x in range(configure.gird_size):
    for y in range(configure.gird_size):
        c = Cell(x,y)
        c.create_btn_object(centre_frame)
        c.cell_btn_object.grid(column = x, row = y)

Cell.create_object_cell_count_labe;(top_frame)
Cell.cell_count_label_object.place(
    x= new.width_prct(42),
    y =new.height_prct(15)
)

Cell.randomize_mines()

root.mainloop()
