import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import sqlite3
import re

# obs .. pra adicionar as imagem e icon tem quer esta na msm pasta 
# caso contrario as imagem e icon nao vai aparece baixa o arquivo 
# copactado e assim todo os dados vai esta na msm pasta pra roda com imagem e icon


#Função para criar a tabela de usuários no banco de dados SQLite
def criar_tabela_usuarios():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                      id INTEGER PRIMARY KEY,
                      nome TEXT,
                      sobrenome TEXT,
                      email TEXT,
                      senha TEXT)''')

    conn.commit()
    conn.close()

#Função para inserir um novo usuário no banco de dados
def inserir_usuario(nome, sobrenome, email, senha):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, sobrenome, email, senha) VALUES (?, ?, ?, ?)",
                   (nome, sobrenome, email, senha))
    conn.commit()
    conn.close()

# Função login
def login():
    email = nome_entre.get()
    senha = password_entre.get()

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    resultado = cursor.fetchone()

    if resultado:
        msg = messagebox.showinfo(title="Logado", message="Parabéns! Usuário logado com sucesso!")

# Oculte o quadro de login e mostre a interface principal

        login_frame.pack_forget()
        tela_principal_logado ()
    else:
        messagebox.showerror(title="Erro de login", message="Email ou senha incorretos.")

    conn.close()

# tela_principal_logado do Orkut
def tela_principal_logado ():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")

    janela.geometry("900x500")
    janela.title("Voce esta logando com sua conta no orkut seja bem vindo! ")

# foto do Orkut/comunidade
    foto_frame = ctk.CTkFrame(master=janela, width=130, height=130)
    foto_frame.place(x=11, y=11)

    img= PhotoImage (file = "odeio_acorda_cedo.png")
    foto_img = ctk.CTkLabel(master = foto_frame, image= img, text=" ")
    foto_img.place(x=-17,y=-14)

#nome de usuario /comunidade em baixo da foto
    nome_usuario_frame = ctk.CTkFrame(master=janela, width=130, height=280)
    nome_usuario_frame.place(x=10, y=150)

    nome_usuario_label = ctk.CTkLabel(master=nome_usuario_frame, text="COMUNIDADE", text_color="black")
    nome_usuario_label.place(x=10, y=0)

    nome_usuario_label = ctk.CTkLabel(master=nome_usuario_frame, text="membros, 19.834,42", text_color="black")
    nome_usuario_label.place(x=10, y=25)

    perfil_label = ctk.CTkLabel(master=nome_usuario_frame, text="perfil", text_color="black")
    perfil_label.place(x=10, y=50)

    recados_label = ctk.CTkLabel(master=nome_usuario_frame, text="recados", text_color="black")
    recados_label.place(x=10, y=75)

    fotos_label = ctk.CTkLabel(master=nome_usuario_frame, text="fotos", text_color="black")
    fotos_label.place(x=10, y=95)

    videos_label = ctk.CTkLabel(master=nome_usuario_frame, text="videos", text_color="black")
    videos_label.place(x=10, y=115)

    depoimentos_label = ctk.CTkLabel(master=nome_usuario_frame, text="depoimentos", text_color="black")
    depoimentos_label.place(x=10, y=135)

    eventos_label = ctk.CTkLabel(master=nome_usuario_frame, text="eventos", text_color="black")
    eventos_label.place(x=10, y=155)

    APP_label = ctk.CTkLabel(master=nome_usuario_frame, text="APP", text_color="black")
    APP_label.place(x=10, y=180)

    atualizações_label = ctk.CTkLabel(master=nome_usuario_frame, text="atualizações", text_color="black")
    atualizações_label.place(x=10, y=200)

    configurações_label = ctk.CTkLabel(master=nome_usuario_frame, text="configurações", text_color="black")
    configurações_label.place(x=10, y=220)

    span_label = ctk.CTkLabel(master=nome_usuario_frame, text="span", text_color="black")
    span_label.place(x=10, y=240)

#frame seja bem vindo
    bem_vindo_frame = ctk.CTkFrame(master=janela, width=500, height=235)
    bem_vindo_frame.place(x=145, y=10)
    bem_vindo_label = ctk.CTkLabel(master=bem_vindo_frame, text="Eu Odeio Acoeda Cedo ! ", text_color="black")
    bem_vindo_label.place(x=9, y=1)
    recados_label = ctk.CTkLabel(master=bem_vindo_frame, text="-----------------------------------Descrição da comunidade-------------------------------------------------", text_color="green")
    recados_label.place(x=9, y=50)
    fotos_label = ctk.CTkLabel(master=bem_vindo_frame, text="Para todo aquele que achar que o dia só começa depois do meio dia...", text_color="green")
    fotos_label.place(x=9, y=100)
    fãs_label = ctk.CTkLabel(master=bem_vindo_frame, text="Eu faço samba até mais tarde e tenho muito sono de manhã (Chico Buarque)\n-----------------------------------------------------------------------------------------", text_color="green")
    fãs_label.place(x=9, y=150)
    fãs_label = ctk.CTkLabel(master=bem_vindo_frame, text="A Maior Comunidade do Orkut !!!", text_color="red")
    fãs_label.place(x=150, y=200)

#Descrições comunidade
    embaixo_frame = ctk.CTkFrame(master=janela, width=500, height=180)
    embaixo_frame.place(x=145, y=250)

    embaixo_label = ctk.CTkLabel(master=embaixo_frame, text="idioma:", text_color="green")
    embaixo_label.place(x=10, y=5)

    embaixo_label = ctk.CTkLabel(master=embaixo_frame, text="portugues", text_color="green")
    embaixo_label.place(x=57, y=5)

    embaixo_label = ctk.CTkLabel(master=embaixo_frame, text="categorias:", text_color="green")
    embaixo_label.place(x=10, y=30)

    bem_vindo_label = ctk.CTkLabel(master=embaixo_frame, text="outros", text_color="green")
    bem_vindo_label.place(x=80, y=30)

    bem_vindo_label = ctk.CTkLabel(master=embaixo_frame, text="moderadores:", text_color="green")
    bem_vindo_label.place(x=10, y=60)

    bem_vindo_label = ctk.CTkLabel(master=embaixo_frame, text="dono", text_color="green")
    bem_vindo_label.place(x=90, y=60)

    bem_vindo_label = ctk.CTkLabel(master=embaixo_frame, text="tipo:", text_color="green")
    bem_vindo_label.place(x=10, y=90)

    bem_vindo_label = ctk.CTkLabel(master=embaixo_frame, text="publica", text_color="green")
    bem_vindo_label.place(x=37, y=90)

    bem_vindo_label = ctk.CTkLabel(master=embaixo_frame, text="criada em:", text_color="green")
    bem_vindo_label.place(x=10, y=120)

    bem_vindo_label = ctk.CTkLabel(master=embaixo_frame, text="23/05/2004", text_color="green")
    bem_vindo_label.place(x=37, y=120)

    bem_vindo_label = ctk.CTkLabel(master=embaixo_frame, text="local:", text_color="green")
    bem_vindo_label.place(x=10, y=150)

    bem_vindo_label = ctk.CTkLabel(master=embaixo_frame, text="RJ, Brasil", text_color="green")
    bem_vindo_label.place(x=37, y=150)

#meus amigos
    amigos_frame = ctk.CTkFrame(master=janela, width=238, height=230)
    amigos_frame.place(x=651, y=15)
    amigos_label = ctk.CTkLabel(master=amigos_frame, text="Meus amigos (0)", text_color="black")
    amigos_label.place(x=10, y=5)

#busca amigos
    busca_amigos_tela_principal = ctk.CTkEntry(master=amigos_frame, placeholder_text="Busca Amigos", width=220)
    busca_amigos_tela_principal.place(x=10, y=30)

#minhas comunidade
    comunidades_frame = ctk.CTkFrame(master=janela, width=238, height=180)
    comunidades_frame.place(x=651, y=250)

    comunidades_label = ctk.CTkLabel(master=comunidades_frame, text="Minhas comunidades (3)", text_color="black")
    comunidades_label.place(x=10, y=5)

#busca comunidade
    busca_comunidades_tela_principal = ctk.CTkEntry(master=comunidades_frame, placeholder_text="Busca Comunidades", width=220)
    busca_comunidades_tela_principal.place(x=10, y=30)

# frame roda pe
    roda_pe_frame = ctk.CTkFrame(master=janela, width=880, height=50)
    roda_pe_frame.place(x=15, y=435)

    roda_pe_label = ctk.CTkLabel(master=roda_pe_frame, text="Orkut", text_color="black")
    roda_pe_label.place(x=10, y=10)

    roda_pe_label = ctk.CTkLabel(master=roda_pe_frame, text=" Sobre Orkut / ", text_color="black")
    roda_pe_label.place(x=60, y=10)
 
    roda_pe_label = ctk.CTkLabel(master=roda_pe_frame, text=" Novidades / ", text_color="black")
    roda_pe_label.place(x=150, y=10)
 
    roda_pe_label = ctk.CTkLabel(master=roda_pe_frame, text=" Centro de segurança / ", text_color="black")
    roda_pe_label.place(x=220, y=10)
 
    roda_pe_label = ctk.CTkLabel(master=roda_pe_frame, text=" Privacidade / ", text_color="black")
    roda_pe_label.place(x=350, y=10)
 
    roda_pe_label = ctk.CTkLabel(master=roda_pe_frame, text=" termos de uso / ", text_color="black")
    roda_pe_label.place(x=430, y=10)
 
    roda_pe_label = ctk.CTkLabel(master=roda_pe_frame, text="ajuda", text_color="black")
    roda_pe_label.place(x=530, y=10)

#botão sair
    sair_button = ctk.CTkButton(master=roda_pe_frame, text="Sair", width=100, command=janela.destroy)
    sair_button.place(x=770, y=5)

#COMUNIDADE2
    img= PhotoImage (file = "comunidade4.png")
    foto_comunidades_img = ctk.CTkLabel(master = comunidades_frame, image= img, text=" ")
    foto_comunidades_img.place(x=15,y=70)

    janela.mainloop()

# função de registro
def tela_registro():
    login_frame.pack_forget()
    rg_frame.pack(side=RIGHT)

# função de volta
def volta():

    rg_frame.pack_forget()
    login_frame.pack(side=RIGHT)

def validar_email(email):

    #verificar se o email possui o formato @

    if re.match(r"^[a-zA-Z0-9._%+-]+@(gmail\.com|hotmail\.com)$", email):
        return True
    else:
        return False

def cadastro_passoas():
    nome = nome_entre_rg.get()
    sobrenome = sobrenome_entre_rg.get()
    email = userneme_entre_rg.get()
    senha = senha_entre_rg.get()
    confirmasenha = confirmasenha_entre_rg.get()
 
    if nome and sobrenome and email and senha and senha == confirmasenha:
        if validar_email (email):  
            
            # Verifique o formato do email
            inserir_usuario(nome, sobrenome, email, senha)
            msg = messagebox.showinfo(title="Bem-vindo ao Orkut", message="Parabéns! Usuário cadastrado com sucesso!")
 
            # Limpar os campos de entrada após o cadastro bem-sucedido
            nome_entre_rg.delete(0, END)
            sobrenome_entre_rg.delete(0, END)
            userneme_entre_rg.delete(0, END)
            senha_entre_rg.delete(0, END)
            confirmasenha_entre_rg.delete(0, END)
        else:
            messagebox.showerror(title="Erro de cadastro", message="Formato de e-mail inválido. Use um e-mail valido do Gmail ou Hotmail.")
    else:
        messagebox.showerror(title="Erro de cadastro", message="Preencha todos os campos e verifique a senha.")

janela = ctk.CTk()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#dimencoes da tela login e cadastro
janela.geometry("1000x390")
janela.title("Bem-vindo ao Orkut")
janela.resizable(False, False)




# obs .. pra adicionar as imagem e icon tem quer esta na msm pasta 
# caso contrario as imagem e icon nao vai aparece 

  # icon 

#janela.iconbitmap("icon.ico")

  # imagem da tela 

#img= PhotoImage (file = "orkut.png")
#Label_img = ctk.CTkLabel(master=janela, image= img, text=" ")
#Label_img.place(x=-3,y=2)

login_frame = ctk.CTkFrame(master=janela, width=350, height=390)
login_frame.pack(side=RIGHT)

#titulo tela login
label= ctk.CTkLabel(master=login_frame, text="Acesse o Orkut com a sua \n Conta do Google")
label.place (x=110, y=35)

# tela pra fazer login com E-meil e senha
nome_entre = ctk.CTkEntry(master=login_frame, placeholder_text="E-mail", width=300)
neme_label = ctk.CTkLabel(master= login_frame, text="*compo de Usuario Obrigatorio", text_color= "green").place(x= 40, y= 135)

password_entre = ctk.CTkEntry(master=login_frame, placeholder_text="Senha", width=300, show="*")
password_label = ctk.CTkLabel(master= login_frame, text="*compo de senha Obrigatorio", text_color= "green").place(x= 40, y= 214)

nome_entre.place(x=30, y=105)
password_entre.place(x=30, y=185)

# Adicione uma caixa de seleção "Lembrar Senha"
checkbox= ctk.CTkCheckBox(master= login_frame, text="salvar as minha informações neste computandor").place(x=30, y= 250)

# butao_de_login
login_button = ctk.CTkButton(master=login_frame, text="Login", width=300, command=login)
login_button.place(x=30, y=290)

cadastro_span = ctk.CTkLabel(master=login_frame, text="Ainda não é membro?")
cadastro_span.place(x=40, y=340)

# butao_de_cadadatro
cadastro_button = ctk.CTkButton(master=login_frame, text="Cadastre-se", width=150, fg_color="green", hover_color="#2D9334", command=tela_registro)
cadastro_button.place(x=180, y=340)

# frame tela registro
rg_frame = ctk.CTkFrame(master=janela, width=350, height=390)

# formulario_de_cadadatro_titulo_e_subtitulo

label = ctk.CTkLabel(master=rg_frame, text="Façar seu Cadastro no Orkut")
label.place(x=100, y=15)

label = ctk.CTkLabel(master=rg_frame, text="Use um e-mail valido do \n Gmail ou Hotmail para finalizar seu cadastro")
label.place(x=60, y=50)

# formulario_de_cadadatro

nome_entre_rg = ctk.CTkEntry(master=rg_frame, placeholder_text="Nome", width=300)
sobrenome_entre_rg = ctk.CTkEntry(master=rg_frame, placeholder_text="Sobrenome", width=300)
userneme_entre_rg = ctk.CTkEntry(master=rg_frame, placeholder_text="E-mail de Usuario", width=300)
senha_entre_rg = ctk.CTkEntry(master=rg_frame, placeholder_text="Senha", width=300, show="*")
confirmasenha_entre_rg = ctk.CTkEntry(master=rg_frame, placeholder_text="Confirma senha", width=300, show="*")

#Aceita ternos
checkbox = ctk.CTkCheckBox(master=rg_frame, text="Aceito os termos e politica da plataformar").place(x=30, y= 300)

# formulario_de_cadadatro
nome_entre_rg.place(x=30, y=100)
sobrenome_entre_rg.place(x=30, y=140)
userneme_entre_rg.place(x=30, y=180)
senha_entre_rg.place(x=30, y=220)
confirmasenha_entre_rg.place(x=30, y=260)

# butao_de_cadadatro
cadastro_button = ctk.CTkButton(master=rg_frame, text="Cadastra", width=145, fg_color="green", hover_color="#014B05", command=cadastro_passoas)
cadastro_button.place(x=30, y=340)

# butao_de_volt
voltar_button = ctk.CTkButton(master=rg_frame, text="Voltar", width=150, fg_color="gray", hover_color="#202020", command=volta)
voltar_button.place(x=180, y=340)

criar_tabela_usuarios()

janela.mainloop()