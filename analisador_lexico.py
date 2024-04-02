import customtkinter as ctk

palavras_reservadas = [('while', 1), ('void', 2), ('string', 3), ('return', 4), ('main', 11), ('integer', 13), ('inicio', 14), ('if', 15), 
                       ('for', 17), ('float', 18), ('fim', 19), ('else', 20), ('do', 21), ('count', 22), ('cin', 23), ('char', 24), 
                       ('callfuncao', 25), ('>>', 26), ('>=', 27), ('>', 28), ('==', 29), ('=', 30), ('<=', 31), ('<<', 32), ('<', 33), 
                       ('++', 34), ('+', 35), ('}', 36), ('{', 37), (';', 38), (':', 39), ('/', 40), (',', 41), ('*', 42), (')', 43), 
                       ('(', 44), ('$', 45), ('!=', 46), ('--', 47), ('-', 38)]

codigo = ''

def pegar_text():
    global codigo
    codigo = textBox.get("1.0", "end-1c")
    
def printar_text():
    print(codigo)

app = ctk.CTk()

app.title("Analisador Léxico")
app.geometry("1000x600")
app.grid_columnconfigure((0,1,2), weight=1)
app.grid_rowconfigure((0,1,2,3), weight=1)

textBox = ctk.CTkTextbox(app)
textBox.grid(row=0, column=0, rowspan=3, columnspan=3, sticky="nsew", padx=10, pady=10)

btnAnalisar = ctk.CTkButton(app, text="Analisar", command=pegar_text)
btnAnalisar.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

app.mainloop()