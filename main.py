import tkinter
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

input = tkinter.Entry(width=10)
input.insert(tkinter.END, '0')
input.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles", font=('Arial', 12))
miles_label.grid(row=0, column=2)

is_equal_to_label = tkinter.Label(text='is equal to', font=('Arial', 12))
is_equal_to_label.grid(row=1, column=0)

converted_metric_label = tkinter.Label(text='0', font=('Arial', 12))
converted_metric_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km", font=('Arial', 12))
km_label.grid(row=1, column=2)


def calculate():
    miles = float(input.get())
    km = miles * 1.609
    return converted_metric_label.config(text=km)


button = tkinter.Button(text='Calculate', command=calculate)
button.grid(row=2, column=1)

window.mainloop()
