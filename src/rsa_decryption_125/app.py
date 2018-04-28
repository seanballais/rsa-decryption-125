import tkinter
from tkinter import *
from rsa_decryption_125 import decryptor


class AppWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_window()

    
    def init_window(self):
        self.master.title('RSA Decryptor')
        self.pack(fill=BOTH, expand=1)

        self.encrypted_message_label = Label(self, text='Encrypted Message')
        self.encrypted_message_label.place(x=0, y=0)
        self.encrypted_message_entrybox = Entry(self)
        self.encrypted_message_entrybox.place(x=122, y=0, width=300)

        self.public_key_label = Label(self, text='Public Key')
        self.public_key_label.place(x=0, y=25)

        self.n_label = Label(self, text='n =')
        self.n_label.place(x=96, y=40)
        self.n_entrybox = Entry(self)
        self.n_entrybox.place(x=122, y=40, width=300)
        
        self.e_label = Label(self, text='e =')
        self.e_label.place(x=96, y=70)
        self.e_entrybox = Entry(self)
        self.e_entrybox.place(x=122, y=65, width=300)
        
        self.decrypted_message_label = Label(self, text='Decrypted message')
        self.decrypted_message_label.place(x=0, y=95)
        self.decrypted_message_box = Text(self, width=60, height=12)
        box_scroll = Scrollbar(self, command=self.decrypted_message_box.yview)
        self.decrypted_message_box.configure(yscrollcommand=box_scroll.set)
        self.decrypted_message_box.place(x=0, y=115)

        self.decrypt_button = Button(self, text="Decrypt message", command=self.get_decrypted_message)
        self.decrypt_button.place(x=0, y=305)

    
    def get_decrypted_message(self):
        self.decrypt_button['text'] = 'Decrypting message...'
        self.decrypt_button['state'] = 'disabled'
        self.encrypted_message_entrybox['state'] = 'disabled'
        self.n_entrybox['state'] = 'disabled'
        self.e_entrybox['state'] = 'disabled'
        
        encrypted = str(self.encrypted_message_entrybox.get())
        n = int(self.n_entrybox.get())
        e = int(self.e_entrybox.get())
        decrypted = decryptor.decrypt(encrypted, n, e)

        self.decrypted_message_box.delete('1.0', END)

        try:
            self.decrypted_message_box.insert(END, decryptor.decode_message(decrypted))
        except ValueError as ve:
            tkinter.messagebox.showerror(
                'Error!', '{}. Invalid encrypted message or public key.'.format(ve)
            )
        except Exception as e:
            tkinter.messagebox.showerror(
                'Something went terribly wrong!', e
            )
        
        self.decrypt_button['text'] = 'Decrypt message'
        self.decrypt_button['state'] = 'normal'
        self.encrypted_message_entrybox['state'] = 'normal'
        self.n_entrybox['state'] = 'normal'
        self.e_entrybox['state'] = 'normal'
        self.decrypted_message_box['state'] = 'normal'


    def app_exit(self):
        exit()

    
def main():
    root = Tk()
    root.geometry('430x350')
    root.resizable(False, False)
    app = AppWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()