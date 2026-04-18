# 🧮 Scientific Pro Elite 
 
**Scientific Pro Elite** é uma calculadora científica de alta performance desenvolvida em Python. O projeto utiliza a biblioteca `CustomTkinter` para entregar uma interface moderna e refinada, inspirada em softwares profissionais de engenharia, com suporte a cálculos matemáticos complexos e interatividade via teclado físico. 
 
--- 
 
## 🌟 Diferenciais do Projeto 
 
- **Interface UI/UX Moderna:** Design focado em legibilidade com tema Dark, cantos arredondados e feedback visual de *hover*. 
- **Display de Dupla Camada:** Visualização em tempo real da expressão atual e do histórico de operações. 
- **Funções Científicas:** Suporte nativo para Trigonometria (Seno, Cosseno, Tangente), Radiciação, Logaritmos e Potenciação. 
- **Integração com Hardware:** Mapeamento completo das teclas do teclado numérico real (Enter, Backspace, Esc e Operadores). 
- **Lógica de Cálculo Segura:** Processamento de expressões matemáticas via `math` com tratamento de exceções para evitar travamentos. 
 
## 🛠️ Tecnologias Utilizadas 
 
- **Python 3.x** 
- **CustomTkinter:** Framework de interface moderna baseada em Tkinter. 
- **Math Module:** Funções matemáticas avançadas para alta precisão. 
- **Programação Orientada a Objetos (POO):** Estrutura modular e escalável. 
 
## 🎮 Como Instalar e Executar 
 
1. **Clone o repositório:** 
  ```bash 
  git clone [https://github.com/teu-usuario/scientific-pro-elite.git](https://github.com/teu-usuario/scientific-pro-elite.git) 
 

Instale a dependência necessária: 

Bash 

pip install customtkinter 
 

Inicie a aplicação: 

Bash 

python main.py 
 

⌨️ Atalhos do Teclado Real 

0-9 e . : Inserção de valores. 

+, -, *, /, ^ : Operadores matemáticos. 

Enter : Calcular resultado (=). 

BackSpace : Apagar último caractere (⌫). 

Esc : Limpar tudo (C). 

🗂️ Estrutura de Código 

CalculadoraCientifica: Classe principal que herda de ctk.CTk. 

criar_botoes: Gerador dinâmico de botões usando dicionários e loops para manter o código limpo (DRY). 

calcular_cientifico: Lógica dedicada para conversão de radianos e cálculos trigonométricos. 

eval com Sanitização: Uso seguro da função de avaliação para processar strings matemáticas complexas. 

 

✒️ Autores 

Luis Guilherme G.B. 

 

Este projeto foi desenvolvido com o objetivo de aplicar conceitos de Álgebra Linear, Matemática Discreta e Interface Homem-Máquina (IHM). 
 
