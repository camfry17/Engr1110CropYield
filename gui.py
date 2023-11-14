import tkinter as tk
import os
#import cropYieldProject
grid_x_padding = 0
grid_y_padding = 0
root = tk.Tk()

root.geometry("600x600")
root.title("ENGR 1110")

#string to maybe have a button to search a specific country/ crop's graph

input_string = tk.StringVar()
def set_text(text):
    e.delete(0, len(text) + 1)
    e.insert(0,text)
    return

def find_data(text):
    pass

def run():
    #os.system('cropYieldProject.py')
    pass

e = tk.Entry(root,width=10)
e.grid(row=2, column=0, padx= grid_x_padding, pady= grid_y_padding)

enter_button = tk.Button(root,text="Find data", command=lambda: run())
enter_button.config(width=7, height=1)
enter_button.grid(row=2,column=1, padx= grid_x_padding, pady= grid_y_padding)

b1 = tk.Button(root,text="Somthing",command=lambda:set_text("ARG"))
b1.grid(row=3, column= 1, padx= grid_x_padding, pady= grid_y_padding)

b2 = tk.Button(root,text="Somthing",command=lambda:set_text("plant"))
b2.grid(row=3,column=0, padx= grid_x_padding, pady= grid_y_padding)

label = tk.Label(root, text = "Welcome to our program! \nHere you will be able tofind the crop yield \ndata for a specific country that you search for.")
label.grid(row=0,column=0, columnspan=3, rowspan=2, padx= grid_x_padding, pady= grid_y_padding)

#manipulate colums to make everything go together well

root.mainloop()