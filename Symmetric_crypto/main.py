import tkinter as tk 
from tkinter import filedialog

from sym_crypto import Crypto

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.c = Crypto()
        self.filename = ''

        self.title = tk.Label(text='Criptografia', font='Arial, 14')
        self.title.place(width=None, height=None, x=185, y=10)

        self.file_lbl = tk.Label(text='Selecione um arquivo')
        self.file_lbl.place(width=None, height=None, x=20, y=50)

        self.file_btn = tk.Button(text='File', command= self.open_file)
        self.file_btn.place(width=60, height=None, x=140, y=48)

        self.file_chkr = tk.Label(text='Arquivo selecionado:')
        self.file_chkr.place(width=None, height=None, x=20, y=80)

        self.file_path = tk.Label(text='Nenhum arquivo selecionado')
        self.file_path.place(width=None, height=None, x=140, y=80)

        self.crypt_btn = tk.Button(text='Criptografar', command= self.encrypt)
        self.crypt_btn.place(width=None, height=None, x=150, y=120)

        self.decrypt_btn = tk.Button(text='Descriptografar', command= self.pswd_screen)
        self.decrypt_btn.place(width=None, height=None, x=230, y=120)

        self.msg = tk.Label(text='')
        self.msg.place(width=None, height=None, x=170, y=160)

    def open_file(self):
        self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file")
        self.file_path['text'] = (self.filename)

    def pswd_screen(self):
        self.msg['text'] = ''

        self.pswd_label = tk.Label(text="Chave de Segurança")
        self.pswd_label.place(width=None, height=None, x=185, y=160)

        self.pswd_entry = tk.Entry()
        self.pswd_entry.place(width=270, height=20, x=105, y=190)

        self.pswd_btn = tk.Button(text="Iniciar", command=self.decrypt)
        self.pswd_btn.place(width=None, height=None, x=220, y=220)

    def encrypt(self):
        try:
            self.pswd_label.destroy()
            self.pswd_entry.destroy()
            self.pswd_btn.destroy()
        except:
            pass

        if self.filename == '':
            msg = """
impossível encriptar, 
nenhum arquivo foi selecionado
                """
            self.msg['text'] = msg
            self.msg.place(width=None, height=None, x=170, y=160)
        else:    
            self.c.crypt(self.filename)
            if self.c.crypt(self.filename) == True:
                msg = (f"""
Arquivo encriptado
    com sucesso

Chave de segurança: 
{self.c.key}
                """)
                print(self.c.key)
                self.msg['text'] = msg
                self.msg.place(width=None, height=None, x=80, y=160)
            else:
                msg = """
O arquivo não foi
encriptado corretamente
                """
                self.msg['text'] = msg
                self.msg.place(width=None, height=None, x=170, y=160)


    def decrypt(self):
        if self.pswd_entry.get() != '':
            key = self.pswd_entry.get()
        else:
            key = self.c.key 

        print(key)
        self.pswd_label.destroy()
        self.pswd_entry.destroy()
        self.pswd_btn.destroy()

        if self.filename == '':
            msg = """
impossível decriptar, 
nenhum arquivo foi selecionado
                """
            self.msg['text'] = msg
            self.msg.place(width=None, height=None, x=170, y=160)
        else:
            self.c.decrypt(self.filename, key)
            if self.c.decrypt(self.filename, key) == True:
                msg = """
Arquivo decriptado
    com sucesso
                """
                self.msg['text'] = msg
                self.msg.place(width=None, height=None, x=170, y=160)
            else:
                msg = """
O arquivo não está
encriptado corretamente
                """
                self.msg['text'] = msg
                self.msg.place(width=None, height=None, x=170, y=160)


app = App()
app.geometry("480x360")
app.mainloop()