import tkinter
window = tkinter.Tk()
window.minsize(width=300, height=200)
window.title('km to miles converter')
label1 = tkinter.Label(text="Enter km:")
label1.grid(row=1, column=2)

km_entry = tkinter.Entry()
km_entry.grid(row=1, column=3)

# label2 = tkinter.Label(text="to")
# label2.grid(row=2, column=3)

label3 = tkinter.Label(text="miles")
label3.grid(row=3, column=2)

def cal():
    val = km_entry.get()
    result = round(float(val) / 1.609, 2)
    label4 = tkinter.Label(text=f"{result}")
    label4.grid(row=3, column=3)

button = tkinter.Button(text="Convert", command=cal)
button.grid(row=2, column=3)



window.mainloop()