import tkinter as tk
import pint
ureg = pint.UnitRegistry()
ureg.define('pound_force_per_square_foot = force_pound / foot **2 = psf') 


def calculate(number: str, unit1: str, unit2: str, field: tk.Label) -> None:
    """
    Cast number as float and convert it from one unit to another

    :param number: str, number to attempt to cast to float and 
                   convert from unit1 to unit2
    :param unit1: str, choice from dropdown menu of pressures
    :param unit2: str, choice from dropdown menu of pressures
    :param field: tk.Label to update with the calculated number
    :return: None
    """

    try:
        number_float = float(number.replace(',', ''))
        converter = ureg.Quantity
        initial_value = converter(number_float, unit1)
        final_value = initial_value.to(unit2)
        field.configure(text='{:,.2f}'.format(
                        final_value.magnitude), relief="sunken")
    except ValueError:
        toreturn = 'Input a number'
        field.configure(text='{}'.format(toreturn), relief="sunken")
    except pint.errors.UndefinedUnitError:
        toreturn = 'Unrecognized unit'
        field.configure(text='{}'.format(toreturn), relief="sunken")
    except pint.errors.DimensionalityError:
        toreturn = 'Check units'
        field.configure(text='{}'.format(toreturn), relief="sunken")

app = tk.Tk()
app.title('Unit Converter')

app.geometry('400x200')

tk.Label(app, text="Converter", font=("Verdana", 24)).grid(row=0, 
                                column=1, columnspan=3)

calculate_text = tk.Label(app, text="Convert ")
calculate_text.grid(row=1, column=1)

value_to_convert = tk.StringVar()
input_field = tk.Entry(app, borderwidth=2, relief="sunken", 
                       textvariable=value_to_convert, width=15)
input_field.grid(row=1, column=2)

first_units = tk.StringVar()
first_units.set('Pa')
units_one = tk.Entry(app, borderwidth=2, relief="sunken", 
                     textvariable=first_units, width=10)
units_one.grid(row=1, column=3)

into_text = tk.Label(app, text='into')
into_text.grid(row=2, column=2)

calculated_value = tk.Label(app, borderwidth=2, relief="groove", 
                            width=15)
calculated_value.grid(row=3, column=2)

second_units = tk.StringVar()
second_units.set('Pa')
units_two = tk.Entry(app, borderwidth=2, relief="sunken", 
                     textvariable=second_units, width=10)
units_two.grid(row=3, column=3)

tk.Label(app, text="").grid(row=4, column=2)

convert_button = tk.Button(app, text="Convert", command=lambda: 
                      calculate(value_to_convert.get().strip(),                                                          
                      first_units.get().strip(), 
                      second_units.get().strip(), calculated_value))
convert_button.grid(row=5, column=2)
app.mainloop()