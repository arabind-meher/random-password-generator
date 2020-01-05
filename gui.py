import pyperclip

from tkinter import *
from tkinter import messagebox
from password_generator import GeneratePassword


# Graphics User Interface of the Program
class Gui:
    def __init__(self, master):
        self.master = master
        self.password = []

        master.geometry('500x450')  # size
        master.resizable(0, 0)  # Resizable = False
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

        # UpperCase CheckButton
        self.uppercase = IntVar()
        Checkbutton(
            master, text='  UpperCase', variable=self.uppercase, onvalue=1, offvalue=0, font=('Times New Roman', 18)
        ).place(x=20, y=100)

        # LowerCase CheckButton
        self.lowercase = IntVar()
        Checkbutton(
            master, text='  LowerCase', variable=self.lowercase, onvalue=1, offvalue=0, font=('Times New Roman', 18)
        ).place(x=250, y=100)

        # Number CheckButton
        self.number = IntVar()
        Checkbutton(
            master, text='  Number', variable=self.number, onvalue=1, offvalue=0, font=('Times New Roman', 18)
        ).place(x=20, y=150)

        # Symbol CheckButton
        self.symbol = IntVar()
        Checkbutton(
            master, text='  Symbol', variable=self.symbol, onvalue=1, offvalue=0, font=('Times New Roman', 18)
        ).place(x=250, y=150)

        # Password Length Label & Entry Field
        self.length = IntVar()
        Label(
            master, text='Length:', font=('Times New Roman', 18)
        ).place(x=180, y=220)
        Entry(
            master, textvariable=self.length, width=2, font=('Times New Roman', 18)
        ).place(x=265, y=220)
        self.length.set(10)

        # Password Display Label
        Label(
            master, text='', bg='white', width=32, justify='center', font=('Times New Roman', 18)
        ).place(x=15, y=300)

        def c_button():
            pyperclip.copy(self.password)

        # Button to copy Password to Clipboard
        Button(
            master, text='Copy', command=c_button, font=('Times New Roman', 16)
        ).place(x=415, y=297)

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
            ).place(x=15, y=300)

        # Button to create password
        Button(
            master, text='Generate', command=generate_button, padx=60, font=('Times New Roman', 16)
        ).place(x=150, y=375)

 
# Main Function
if __name__ == '__main__':
    root = Tk()
    Gui(root)
    root.mainloop()
