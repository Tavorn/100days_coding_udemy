from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

is_equal_label = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10, pady=10)

kilometer_result_label = Label(text=0, font=("Arial", 24, "bold"))
kilometer_result_label.grid(column=1, row=1)
kilometer_result_label.config(padx=10, pady=10)

kilometer_label = Label(text="Km", font=("Arial", 24, "bold"))
kilometer_label.grid(column=2, row=1)
kilometer_label.config(padx=10, pady=10)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)
calculate_button.config(pady=10, padx=10)


window.mainloop()
