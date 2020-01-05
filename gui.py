from tkinter import *
from tkinter import messagebox
from password_generator import GeneratePassword


# Graphics User Interface of the Program
class Gui:
    def __init__(self, master):
        self.master = master
        self.password = []

        master.geometry('500x500')  # size
        master.resizable(0, 0)  # Resizable
        master.title('Random Password Generator')  # Title

        # Blank Label
        Label(
            master, text=''
        ).pack(fill=X)

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
            master, textvariable=self.length, width=2, font=('Times New Roman', 18)
        ).place(x=275, y=265)
        self.length.set(10)

        # Password Display Label
        Label(
            master, text='', bg='white', width=32, justify='center', font=('Times New Roman', 18)
        ).place(x=25, y=320)

        def c_button():
            master.clipboard_clear()
            master.clipboard_append(self.password)

        # Button to copy Password to Clipboard
        Button(
            master, text='C', command=c_button, font=('Times New Roman', 16)
        ).place(x=425, y=318)

        # Function calls when 'Generate' button is pressed
        def generate_button():
            if not 8 <= self.length.get() <= 30:
                messagebox.showwarning('Warning', 'Length can only be from 8 to 30')
                return 0
            try:
                # calls 'generate_password' from 'password_generator' python file
                self.password = GeneratePassword(
                    self.length.get(), self.uppercase.get(), self.lowercase.get(), self.number.get(), self.symbol.get()
                ).password
            except TclError:
                messagebox.showwarning('Warning', 'Length cannot be string')
            except IndexError:
                messagebox.showwarning(
                    'Warning',
                    'Must checked at least one checkbox\n\n\t=> UpperCase\n\t=> LowerCase\n\t=> Number\n\t=> Symbol'
                )

            self.password = ''.join(self.password)
            Label(
                master, text=self.password, bg='white', width=32, justify='center', font=('Times New Roman', 18)
            ).place(x=25, y=320)

        # Button to create password
        Button(
            master, text='Generate', command=generate_button, padx=60, font=('Times New Roman', 16)
        ).place(x=150, y=370)

        # Line Label (for better graphics)
        Label(
            master, text='-----------------------------------------------------------------------'
        ).place(y=420)

        # Button to save 'Domain', 'ID' & 'Password' to a .csv file
        Button(
            master, text='  Save  ', padx=60, font=('Times New Roman', 16)
        ).place(x=150, y=450)


# Main Function
if __name__ == '__main__':
    root = Tk()
    Gui(root)
    root.mainloop()
