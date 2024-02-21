import ply.lex as lex
import tkinter as tk
from tkinter import ttk, scrolledtext

class LexicalAnalyzer:
    def __init__(self):
        self.tokens = [
            'IDENTIFICADOR', 'NUMERO',
            'MAS', 'MENOS', 'MULTIPLICACION', 'DIVISION',
            'MAYOR', 'MENOR', 'IGUAL', 'MAYORIGUAL', 'MENORIGUAL',
            'LLAVEIZQ', 'LLAVEDER', 'PUNTOCOMA', 'DOSPUNTOS',
            'COMENTARIO', 'LEFT_PAREN', 'RIGHT_PAREN', 'FOR', 'DOT','WHILE', 'IF','RIGHT_BRACKET','LEFT_BRACKET','INCREMENT'
        ]
        self.reserved_words = {
            'FOR': 'FOR', 'WHILE': 'WHILE', 'IF': 'IF',
        }

        self.lexer = lex.lex(module=self)

    t_MAS = r'\+'
    t_INCREMENT =r'\++'
    t_MENOS = r'-'
    t_MULTIPLICACION = r'\*'
    t_DIVISION = r'/'
    t_MAYOR = r'>'
    t_MENOR = r'<'
    t_IGUAL = r'='
    t_MAYORIGUAL = r'>='
    t_MENORIGUAL = r'<='
    t_LLAVEIZQ = r'\{'
    t_LLAVEDER = r'\}'
    t_PUNTOCOMA = r';'
    t_DOSPUNTOS = r':'
    t_LEFT_PAREN = r'\('
    t_RIGHT_PAREN = r'\)'
    t_DOT = r'\.'
    t_LEFT_BRACKET = r'\['
    t_RIGHT_BRACKET = r'\]'
    t_ignore = ' \t'

    def t_IDENTIFICADOR(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved_words.get(t.value.upper(), 'IDENTIFICADOR')
        return t

    def t_NUMERO(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_COMENTARIO(self, t):
        r'//.*'
        pass

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print(f"Carácter ilegal: '{t.value[0]}' en la línea {t.lineno}")
        t.lexer.skip(1)

    def analyze(self, data):
        self.lexer.input(data)
        tokens = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            tokens.append(tok)
        return tokens

def analyze_code():
    code = input_code.get("1.0", "end-1c")
    analyzer = LexicalAnalyzer()
    tokens = analyzer.analyze(code)

    # Clear the Treeview before displaying new results
    for item in result_tree.get_children():
        result_tree.delete(item)

    # Insert the results into the Treeview
    for token in tokens:
        result_tree.insert("", 'end', values=(token.value, token.type, token.lineno))

# Create the GUI
root = tk.Tk()
root.title("Lexical Analyzer")

input_label = tk.Label(root, text="Ingresa tu código:")
input_label.pack()

input_code = scrolledtext.ScrolledText(root, width=50, height=10)
input_code.pack()

analyze_button = tk.Button(root, text="Analizar", command=analyze_code)
analyze_button.pack()

result_tree = ttk.Treeview(root, columns=("Valor", "Tipo", "Línea"))
result_tree.heading("#1", text="Valor")
result_tree.heading("#2", text="Tipo")
result_tree.heading("#3", text="Línea")
result_tree.pack()

root.mainloop()
