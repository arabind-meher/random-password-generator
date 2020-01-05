from tkinter import *
from password_generator import generate_password


class Gui:
    def __init__(self, master):
        self.master = master

        master.geometry('500x500')
        master.resizable(0, 0)
        master.title('Random Password Generator')

        Label(master, text='').pack(fill=X)

        Label(master, text='Random Password Generator', font=('Open Sans', 24)).pack(fill=X)
        Label(master, text='-----------------------------------------------------------------------').pack(fill=X)

        self.domain_text = StringVar()
        Label(master, text='Domain:', font=('Times New Roman', 18)).place(x=10, y=75)
        Entry(master, textvariable=self.domain_text, width=32, font=('Times New Roman', 18)).place(x=100, y=75)

        self.id_text = StringVar()
        Label(master, text='    ID:', font=('Times New Roman', 18)).place(x=10, y=115)
        Entry(master, textvariable=self.id_text, width=32, font=('Times New Roman', 18)).place(x=100, y=115)

        Label(master, text='-----------------------------------------------------------------------').place(y=155)

        self.uppercase = IntVar()
        Checkbutton(
            master, text='  UpperCase', variable=self.uppercase, onvalue=1, offvalue=0, font=('Times New Roman', 18)
        ).place(x=20, y=180)

        self.lowercase = IntVar()
        Checkbutton(
            master, text='  LowerCase', variable=self.lowercase, onvalue=1, offvalue=0, font=('Times New Roman', 18)
        ).place(x=250, y=180)

        self.number = IntVar()
        Checkbutton(
            master, text='  Number', variable=self.number, onvalue=1, offvalue=0, font=('Times New Roman', 18)
        ).place(x=20, y=220)

        self.symbol = IntVar()
        Checkbutton(
            master, text='  Symbol', variable=self.symbol, onvalue=1, offvalue=0, font=('Times New Roman', 18)
        ).place(x=250, y=220)

        self.length = IntVar()
        Label(master, text='Length:', font=('Times New Roman', 18)).place(x=190, y=265)
        Entry(
            master, textvariable=self.length, width=2, justify='right', font=('Times New Roman', 18)
        ).place(x=275, y=265)

        Label(master, text='', bg='white', width=32, justify='center', font=('Times New Roman', 18)).place(x=25, y=320)
        Button(master, text='C', font=('Times New Roman', 16)).place(x=425, y=318)

        def generate_button():
            password = self.get_password(self.length.get(), self.uppercase.get(), self.lowercase.get(), self.number.get(), self.symbol.get())
            Label(
                master, text=password, bg='white', width=32, justify='center', font=('Times New Roman', 18)
            ).place(x=25, y=320)

        Button(
            master, text='Generate', command=generate_button, font=('Times New Roman', 16), padx=60
        ).place(x=150, y=370)

        Label(master, text='-----------------------------------------------------------------------').place(y=420)

        Button(master, text='  Save  ', font=('Times New Roman', 16), padx=60).place(x=150, y=450)

    @staticmethod
    def get_password(n_length, is_upper, is_lower, is_number, is_symbol):
        return generate_password(n_length, is_upper, is_lower, is_number, is_symbol)


if __name__ == '__main__':
    root = Tk()
    Gui(root)
    root.mainloop()
