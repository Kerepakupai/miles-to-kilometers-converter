from tkinter import *


def convert():
    km = round(float(input_text.get()) * 1.609344)
    result_label.config(text=km)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.title("Miles to Km Converter")
    window.minsize(width=300, height=150)
    window.config(pady=20, padx=20)

    input_text = Entry(width=8)
    input_text.config(font=("Arial", 12))
    input_text.grid(column=1, row=0)

    miles_label = Label(text="Miles", font=("Arial", 12))
    miles_label.grid(column=2, row=0)

    is_equal_to_label = Label(text="is equal to", font=("Arial", 12))
    is_equal_to_label.grid(column=0, row=1)

    result_label = Label(text="0", font=("Arial", 12))
    result_label.grid(column=1, row=1)

    km_label = Label(text="Km", font=("Arial", 12))
    km_label.grid(column=2, row=1)

    calculate_button = Button(text="Calculate", command=convert)
    calculate_button.grid(column=1, row=2)

    window.mainloop()
