import tkinter as tk

def convert_mpa_to_psi(number: str, field: tk.Label):
    """
    Convert MPa to PSI with the conversion factor 
    1 MPa = 145.038 PSI
    :param number: str number to cast as float and convert to psi
    :param field: The Label to update with the calculated number
    :return: None
    """
    mpa_to_psi = 145.038
    try:
        toreturn = float(number.replace(',', '')) * mpa_to_psi
        field.configure(text='{:,.2f}'.format(toreturn), 
                        relief="sunken")
    except ValueError:
        toreturn = 'NaN'
        field.configure(text='{}'.format(toreturn), relief="sunken")

app = tk.Tk()
app.title('Unit Converter')

app.geometry('600x350')
text_font = ('Times New Roman', 14)

tk.Label(app, text="Converter", font=("Times New Roman", 24)).grid(row=0, column=1, columnspan=2)

calculate_text = tk.Label(app, text="Convert ", font=text_font)
calculate_text.grid(row=1, column=1)

value_to_convert = tk.StringVar()
input_field = tk.Entry(app, borderwidth=2, relief="sunken", textvariable=value_to_convert, font=text_font)
input_field.grid(row=1, column=2)

mpa_text = tk.Label(app, text=" MPa", font=text_font)
mpa_text.grid(row=1, column=3)

into_text = tk.Label(app, text='into', font=text_font)
into_text.grid(row=2, column=2)

calculated_value = tk.Label(app, text='', borderwidth=2, 
                        relief="groove", width=15, font=text_font)
calculated_value.grid(row=3, column=2)

psi_text = tk.Label(app, text=' psi', font=text_font)
psi_text.grid(row=3, column=3)

tk.Label(app, text="").grid(row=4, column=2)

convert_button = tk.Button(app, text="Convert", command=lambda: 
                            convert_mpa_to_psi(value_to_convert.get(),                                                                    
                            calculated_value), font=text_font)
convert_button.grid(row=5, column=2)
app.mainloop()











