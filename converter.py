from tkinter import *
from tkinter import ttk
import re

widget_width = 30
color = "#eee8d5"

#hex to hex
def hh(input):
    reg = re.compile('^[a-fA-F0-9\.]+$')
    if reg.match(input):
        return input
    else:
        return "Not a valid hexadecimal number"

#hex to dec
def hd(input):
    reg = re.compile('^[a-fA-F0-9\.]+$')
    if reg.match(input):
        return int(input, 16)
    else:
        return "Not a valid hexadecimal number"

#hex to bin
def hb(input):
    reg = re.compile('^[a-fA-F0-9\.]+$')
    if reg.match(input):
        return bin(int(input, 16))[2:].zfill(len(input) * 4)
    else:
        return "Not a valid hexadecimal number"

#bin to bin
def bb(input):
    reg = re.compile('^[0-1\.]+$')
    if reg.match(input):
        return input
    else:
        return "Not a valid binary number"

#bin to dec
def bd(input):
    reg = re.compile('^[0-1\.]+$')
    if reg.match(input):
        return int(input, 2)
    else:
        return "Not a valid binary number"

#bin to hex
def bh(input):
    reg = re.compile('^[0-1\.]+$')
    if reg.match(input):
        return hex(int(input, 2))[2:].upper()
    else:
        return "Not a valid hexadecimal number"

#dec to bin
def db(input):
    reg = re.compile('^[0-9\.]+$')

    if reg.match(str(input)):
        return bin(int(input))[2:]
    else:
        return "Not a valid integer"

#dec to dec
def dd(value):
    try:
        value = int(value)
        return value
    except:
        return "Not a valid integer"

#dec to hex
def dh(input):
    reg = re.compile('^[0-9\.]+$')

    if reg.match(str(input)):
        return hex(int(input))[2:].upper()
    else:
        return "Not a valid integer"

  
def calculate(event):

    function_list = {
        "bd":bd,
        "db":db,
        "dh":dh,
        "hd":hd,
        "hh":hh,
        "dd":dd,
        "hb":hb,
        "bh":bh,
        "bb":bb
    }
    
    first_letter = drop1.get()[:1].lower()
    second_letter = drop2.get()[:1].lower()
    function = function_list[first_letter+second_letter]
    answer = function(entry.get())
    length = len(str(answer))
    
    entry2["state"] = "normal"
    entry2.delete("1.0", END)
    entry2.insert("1.0", answer)
    entry2["state"] = "disabled"
    label5.configure(text=f"({length} digits)")
    
def reset():
    entry2["state"] = "normal"
    entry2.delete("1.0", END)
    entry2["state"] = "disabled"
    entry.delete(0, END)
    label5.configure(text="")
  
def on_select(event):
    selected = event.widget.get()
    label3['text'] = "Enter " + selected + " number"

def on_select2(event):
    selected = event.widget.get()
    label4['text'] =  selected + " number"

root = Tk() 
root.geometry( "590x250" ) 
root.configure(background=color)
root.title("Number converter")
root.resizable(0,0)
  
# Create Dropdown menu
label1 = ttk.Label(root, text="From", width=widget_width, anchor="w", background=color) 
label1.grid(column=0, row=0)

drop1 = ttk.Combobox(
    state="readonly",
    values=[ 
    "Binary", 
    "Hexadecimal", 
    "Decimal (Integer)"
    ],
    width=widget_width
)
drop1.grid(column=0, row=1, padx=(15,0))
drop1.current(0)
drop1.bind('<<ComboboxSelected>>', on_select)

label2 = ttk.Label( root , text = "To", width=widget_width, anchor="w", background=color) 
label2.grid(column=1, row=0)

drop2 = ttk.Combobox(
    state="readonly",
    values=[ 
    "Binary", 
    "Hexadecimal", 
    "Decimal"
    ],
    width=widget_width
) 
drop2.grid(column=1, row=1, padx=(15,0))
drop2.current(2)
drop2.bind('<<ComboboxSelected>>', on_select2)

label3 = ttk.Label(root, text = "Enter " + drop1.get() + " number", anchor="w", width=widget_width, background=color) 
label3.grid(column=0, row=2, pady=(20,0))

entry = ttk.Entry(root, width=82)
entry.bind("<Return>", calculate)
entry.grid(column=0, row=3, columnspan=2, padx=(15,0))
  
button1 = ttk.Button( root , text = "Convert" , command = lambda:calculate(""))
button1.grid(column=0, row=4, pady=(10,0)) 
button2 = ttk.Button( root , text = "Reset" , command = reset)
button2.grid(column=1, row=4, pady=(10,0)) 

label4 = ttk.Label( root , text = drop2.get() + " number", anchor="w", width=widget_width, background=color) 
label4.grid(column=0, row=5, pady=(20,0))

entry2 = Text(root, width=69, state="disabled", height=3)
entry2.grid(column=0, row=6, columnspan=2, padx=(15,0))

label5 = ttk.Label( root , text = "", anchor="e", width=widget_width, background=color) 
label5.grid(column=1, row=5, pady=(20,0))  

root.mainloop() 