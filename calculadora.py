import customtkinter as ctk
import math

class CalculadoraCientifica(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Scientific Pro Elite")
        self.geometry("420x700")
        ctk.set_appearance_mode("dark")
        
        self.expressao = ""
        self.historico = ""

        # Bind de teclas do teclado real
        self.bind("<Key>", self.teclado_real)

        # --- Display Estilizado ---
        self.display_frame = ctk.CTkFrame(self, fg_color="#121212", corner_radius=20, border_width=1, border_color="#333")
        self.display_frame.pack(padx=20, pady=25, fill="x")

        self.lbl_historico = ctk.CTkLabel(self.display_frame, text="", font=("Roboto", 18), 
                                          text_color="#55efc4", anchor="e")
        self.lbl_historico.pack(padx=20, pady=(15, 0), fill="x")

        self.lbl_display = ctk.CTkLabel(self.display_frame, text="0", font=("Roboto", 54, "bold"), 
                                        anchor="e", text_color="white")
        self.lbl_display.pack(padx=20, pady=(0, 15), fill="x")

        # --- Grid de Botões ---
        self.grid_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_frame.pack(padx=15, pady=5, fill="both", expand=True)

        self.criar_botoes()

    def criar_botoes(self):
        for i in range(4): self.grid_frame.columnconfigure(i, weight=1)
        for i in range(6): self.grid_frame.rowconfigure(i, weight=1)

        botoes = [
            ('C', 0, 0, "#ff4757"), ('⌫', 0, 1, "#3d3d3d"), ('^', 0, 2, "#3d3d3d"), ('/', 0, 3, "#5352ed"),
            ('sin', 1, 0, "#2f3542"), ('cos', 1, 1, "#2f3542"), ('tan', 1, 2, "#2f3542"), ('*', 1, 3, "#5352ed"),
            ('7', 2, 0, "#1e272e"), ('8', 2, 1, "#1e272e"), ('9', 2, 2, "#1e272e"), ('-', 2, 3, "#5352ed"),
            ('4', 3, 0, "#1e272e"), ('5', 3, 1, "#1e272e"), ('6', 3, 2, "#1e272e"), ('+', 3, 3, "#5352ed"),
            ('1', 4, 0, "#1e272e"), ('2', 4, 1, "#1e272e"), ('3', 4, 2, "#1e272e"), ('√', 4, 3, "#3d3d3d"),
            ('0', 5, 0, "#1e272e"), ('.', 5, 1, "#1e272e"), ('log', 5, 2, "#3d3d3d"), ('=', 5, 3, "#2ed573")
        ]

        for (texto, r, c, cor) in botoes:
            # Cores dinâmicas de hover
            h_color = "#ff6b81" if texto == 'C' else "#7bed9f" if texto == '=' else "#555"
            
            btn = ctk.CTkButton(self.grid_frame, text=texto, fg_color=cor, 
                                hover_color=h_color, font=("Roboto", 20, "bold"), 
                                corner_radius=15, height=70,
                                command=lambda t=texto: self.clique(t))
            btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

    def teclado_real(self, event):
        tecla = event.char
        if tecla.isdigit() or tecla in "+-*/.^":
            self.clique(tecla)
        elif event.keysym == "Return":
            self.clique("=")
        elif event.keysym == "BackSpace":
            self.clique("⌫")
        elif event.keysym == "Escape":
            self.clique("C")

    def clique(self, tecla):
        if tecla == "C":
            self.expressao = ""
            self.historico = ""
        elif tecla == "⌫":
            self.expressao = self.expressao[:-1]
        elif tecla == "=":
            self.calcular()
        elif tecla in ["sin", "cos", "tan", "√"]:
            self.calcular_cientifico(tecla)
        else:
            # Evita múltiplos pontos ou operadores seguidos
            if self.expressao == "Erro": self.expressao = ""
            self.expressao += str(tecla)
        
        self.atualizar_display()

    def atualizar_display(self):
        txt = self.expressao if self.expressao else "0"
        self.lbl_display.configure(text=txt)
        self.lbl_historico.configure(text=self.historico)

    def calcular_cientifico(self, operacao):
        try:
            val = float(self.expressao)
            self.historico = f"{operacao}({val})"
            if operacao == "sin": res = math.sin(math.radians(val))
            elif operacao == "cos": res = math.cos(math.radians(val))
            elif operacao == "tan": res = math.tan(math.radians(val))
            elif operacao == "√": res = math.sqrt(val)
            
            # Formatação inteligente: se for inteiro, tira o .0
            res = round(res, 8)
            self.expressao = str(int(res) if res == int(res) else res)
        except:
            self.expressao = "Erro"
        self.atualizar_display()

    def calcular(self):
        try:
            self.historico = self.expressao + " ="
            # Sanitização da expressão
            expr = self.expressao.replace('^', '**')
            resultado = eval(expr, {"math": math, "__builtins__": None}, {})
            
            resultado = round(resultado, 8)
            self.expressao = str(int(resultado) if resultado == int(resultado) else resultado)
        except Exception:
            self.expressao = "Erro"
        self.atualizar_display()

if __name__ == "__main__":
    app = CalculadoraCientifica()
    app.mainloop()