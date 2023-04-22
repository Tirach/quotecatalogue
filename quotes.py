# Import the necessary module(s).
import tkinter
import tkinter.messagebox
import json
from tkinter import font


class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading and reading the data from the text file and creating the user interface.
        # Set up window
        self.main = tkinter.Tk()
        self.main.resizable(0, 0)
        self.main.geometry('500x200')
        self.main.title("Quote Catalogue")

        # Setting font
        self.main.defaultFont = font.nametofont('TkDefaultFont')
        self.main.defaultFont.configure(family='Calibri',
                                        size=12)

        # Try to open file, error message on exception & destroy process
        try:
            read_data = open('data.txt', 'r')
            self.data = json.load(read_data)
            read_data.close()

        except FileNotFoundError:
            tkinter.messagebox.showerror(
                default='ok', title='Error!', message='Missing/Invalid file.')
            self.main.destroy()
            return

        except:
            tkinter.messagebox.showerror(
                default='ok', title='Error!', message='Something went wrong!')
            self.main.destroy()
            return

        # Main quote label
        global quotes
        quotes = tkinter.Label(
            self.main, font='45', height='5', wraplength='300')
        quotes.pack()

        # Skip button
        skip_btn = tkinter.Button(
            self.main, text='Skip', width='10', bd='3', command=lambda: self.rate_quote('skip'), padx=5)
        skip_btn.place(relx=0.35, rely=0.7, anchor='se')

        # Like button
        like_btn = tkinter.Button(
            self.main, text='Like', width='10', bd='3', command=lambda: self.rate_quote('likes'), padx=5)
        like_btn.place(relx=0.5, rely=0.7, anchor='s')

        # Love button
        love_btn = tkinter.Button(
            self.main, text='Love', width='10', bd='3', command=lambda: self.rate_quote('loves'), padx=5)
        love_btn.place(relx=0.65, rely=0.7, anchor='sw')

        # Current quote index
        self.current_quote = 0

        self.show_quote()

        tkinter.mainloop()

    def show_quote(self):
        # This method is responsible for displaying the details of the current quote in the GUI.
        quote_update = self.data[self.current_quote]
        quotes.config(
            text=f'"{quote_update["quote"].capitalize()}" \n\n'
                 f'-- {quote_update["author"].title()}, {quote_update.get("year", "Unknown")}')

    def rate_quote(self, rating):
        # This method is responsible for recording the rating of the quote when a button is clicked.
        if rating != 'skip':
            self.data[self.current_quote][rating] += 1

            save_my_plus_one = open('data.txt', 'w')
            json.dump(self.data, save_my_plus_one, indent=4)
            save_my_plus_one.close()

            tkinter.messagebox.showinfo(
                default='ok', title='Rating Recorded', message='Your rating has been recorded.')
        else:
            tkinter.messagebox.showinfo(
                default='ok', title='Rating Skipped', message='You have skipped rating this quote.')

        # Increment quote index by 1
        self.current_quote += 1

        if self.current_quote == len(self.data):
            tkinter.messagebox.showinfo(
                default='ok', title='End of Quotes', message='That was the last quote! This program will now terminate.')
            self.main.destroy()
            return
        else:
            self.show_quote()


        # Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
