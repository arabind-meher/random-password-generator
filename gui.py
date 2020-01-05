from tkinter import *
from password_generator import generate_password


# Graphics User Interface of the Program
class Gui:
    def __init__(self, master):
        self.master = master

        master.geometry('500x500')  # size
        master.resizable(0, 0)  # Resizable
        master.title('Random Password Generator')  # Title

        # Blank Label
        Label(master, text='').pack(fill=X)

        # Heading Label
        Label(
            master, text='Random Password Generator', font=('Open Sans', 24)
        ).pack(fill=X)

        # Line Label (for better graphics)
        Label(
            master, text='-----------------------------------------------------------------------'
        ).pack(fill=X)

        # Domain Label & Entry Field
        self.domain_text = StringVar()
        Label(
            master, text='Domain:', font=('Times New Roman', 18)
        ).place(x=10, y=75)
        Entry(
            master, textvariable=self.domain_text, width=32, font=('Times New Roman', 18)
        ).place(x=100, y=75)

        # ID Label and Entry Field
        self.id_text = StringVar()
        Label(
            master, text='    ID:', font=('Times New Roman', 18)
        ).place(x=10, y=115)
        Entry(
            master, textvariable=self.id_text, width=32, font=('Times New Roman', 18)
        ).place(x=100, y=115)

        # Line Label (for better graphics)
        Label(
            master, text='-----------------------------------------------------------------------'
        ).place(y=155)

        # UpperCase CheckButton
        self.uppercase = IntVar()
        Checkbutton(
            master, text='  UpperCase', variable=self.uppercase, onvalue=1, offvalue=0, font=('Times New Roman', 18)
        ).place(x=20, y=180)

        # LowerCase CheckButton
        self.lowercase = IntVar()
        Checkbutton(
            master, text='  LowerCase', variable=self.lowercase, onvalue=1, offvalue=0, font=('Times New Roman', 18)
        ).place(x=250, y=180)

        # Number CheckButton
        self.number = IntVar()
        Checkbutton(
            master, text='  Number', variable=self.number, onvalue=1, offvalue=0, font=('Times New Roman', 18)
        ).place(x=20, y=220)

        # Symbol CheckButton
        self.symbol = IntVar()
        Checkbutton(
            master, text='  Symbol', variable=self.symbol, onvalue=1, offvalue=0, font=('Times New Roman', 18)
        ).place(x=250, y=220)

        # Password Length Label & Entry Field
        self.length = IntVar()
        Label(
            master, text='Length:', font=('Times New Roman', 18)
        ).place(x=190, y=265)
        Entry(
            master, textvariable=self.length, width=2, justify='right', font=('Times New Roman', 18)
        ).place(x=275, y=265)

        # Password Display Label
        Label(master, text='', bg='white', width=32, justify='center', font=('Times New Roman', 18)).place(x=25, y=320)

        # Button to copy Password to Clipboard
        Button(master, text='C', font=('Times New Roman', 16)).place(x=425, y=318)

        # Function calls when 'Generate' button is pressed
        def generate_button():
            password = self.get_password(
                self.length.get(), self.uppercase.get(), self.lowercase.get(), self.number.get(), self.symbol.get()
            )
            Label(
                master, text=password, bg='white', width=32, justify='center', font=('Times New Roman', 18)
            ).place(x=25, y=320)

        # Button to create password
        Button(
            master, text='Generate', command=generate_button, font=('Times New Roman', 16), padx=60
        ).place(x=150, y=370)

        # Line Label (for better graphics)
        Label(
            master, text='-----------------------------------------------------------------------'
        ).place(y=420)

        # Button to save 'Domain', 'ID' & 'Password' to a .csv file
        Button(master, text='  Save  ', font=('Times New Roman', 16), padx=60).place(x=150, y=450)

    # Method that calls 'generate_password' from 'password_generator' python file
    @staticmethod
    def get_password(n_length, is_upper, is_lower, is_number, is_symbol):
        return generate_password(n_length, is_upper, is_lower, is_number, is_symbol)


# Main Function
if __name__ == '__main__':
    root = Tk()
    Gui(root)
    root.mainloop()
