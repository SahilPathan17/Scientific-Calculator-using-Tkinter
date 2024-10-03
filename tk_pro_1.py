from tkinter import *
import math

def click(value):
       ex = display.get()
       ans=""

       try:

              if value == 'C':
                     ex = ex[0:len(ex)-1]
                     display.delete(0, END)
                     display.insert(0, ex)
                     return

              elif value == 'CE':
                     display.delete(0, END)

              elif value == "√":
                     ans = math.sqrt(eval(ex))

              elif value == "π":
                     ans = math.pi

              elif value == "cos0":
                     ans = math.cos(math.radians(eval(ex)))

              elif value == "tan0":
                     ans = math.tan(math.radians(eval(ex)))

              elif value == "sin0":
                     ans = math.sin(math.radians(eval(ex)))

              elif value == "2π":
                     ans = 2*math.pi

              elif value == "cosh":
                     ans = math.cosh(eval(ex))

              elif value == "tanh":
                     ans = math.tanh(eval(ex))

              elif value == "sinh":
                     ans = math.sinh(eval(ex))

              elif value == chr(8731):
                     ans = eval(ex)**(1/3)

              elif value == "x\u02b8":
                     display.insert(END, "**")
                     return

              elif value == "x\u00B3":
                     ans = eval(ex) ** 3

              elif value == "x\u00B2":
                     ans = eval(ex) ** 2

              elif value == "ln":
                     ans = math.log2(eval(ex))

              elif value == "deg":
                     ans = math.degrees(eval(ex))

              elif value == "rad":
                     ans = math.radians(eval(ex))

              elif value == "e":
                     ans = math.e

              elif value == "log10":
                     ans = math.log10(eval(ex))

              elif value == "x!":
                     ans = math.factorial(eval(ex))

              elif value == chr(247):
                     display.insert(END, "/")
                     return

              elif value == "=":
                     ans = eval(ex)

              else:
                     display.insert(END, value)
                     return

              display.delete(0, END)
              display.insert(0, ans)

       except SyntaxError:
              pass

root = Tk()
root.title("Scientific Calculator")
root.geometry("562x386")
root.config(bg="#0d1137")

display = Entry(root, bg="#0d1137", fg="#e52165", bd=20, relief=SUNKEN, width=40, font=("arial", 18, "bold"))
display.grid(row=0, column=0, columnspan=8)

but_lst = ["C", "CE", "√", "+", "π", "cos0", "tan0", "sin0",
       "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
       "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
       "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
       "0", ".", "%", "=", "log10", "(", ")", "x!"]

rowval = 1
colval = 0

for i in but_lst:
       button=Button(root, text=i, font=("arial", 14, "bold"), width=5, height=2, bd=2, relief=SUNKEN, bg="#0d1137",
                     fg="#e52165", activebackground="#e52165", command=lambda button=i: click(button))
       button.grid(row=rowval, column=colval, pady=1)
       colval+=1
       if colval>7:
              rowval+=1
              colval=0

root.mainloop()