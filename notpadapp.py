#notepad App 
import tkinter as tk
from tkinter import filedialog,messagebox

#mainwindow code
root = tk.Tk()
root.title("Notepad App")
root.geometry("600x400")

#text Area 
text = tk.Text(
    root,
    wrap = tk.WORD,
    font =("Helvetic", 12)
)

text.pack(expand=True,fill=tk.BOTH)

#-----------main logic------------
#funcation_newfile 
def new_file():
    text.delete(1.0,tk.END)

#funcation_openfile
def open_file():
    file_path = filedialog.askopenfilename(   #for filedilogopen
        defaultextension=".txt",
        filetypes= [("text Files",".txt")]
    )

    if file_path:
        #openfile 
        with open(file_path,"r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())   #for open filedata

#fincation_savefile
def save_file():
    file_path= filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes= [("text Files",".txt")] 
    )

    if save_file:
        with open(file_path,"w")as file:
            file.write(text.get(1.0, tk.END)) #for save new file 

    messagebox.showinfo("info","File Save Susscesfully")

# ----------EDIT FUNCTIONS ----------
# Undo
def undo_text():
    try:
        text.edit_undo()
    except tk.TclError:
        pass

# Redo
def redo_text():
    try:
        text.edit_redo()
    except tk.TclError:
        pass

# Cut
def cut_text():
    text.event_generate("<<Cut>>")

# Copy
def copy_text():
    text.event_generate("<<Copy>>")

# Paste
def paste_text():
    text.event_generate("<<Paste>>")

# Select All
def select_all():
    text.tag_add(tk.SEL, "1.0", tk.END)
    text.mark_set(tk.INSERT, "1.0")
    text.see(tk.INSERT)

#-----------DarkMode Funcation-----------

# Dark Mode
def dark_mode():
    text.config(
        bg="#1e1e1e",
        fg="white",
        insertbackground="white"
    )

# Light Mode
def light_mode():
    text.config(
        bg="white",
        fg="black",
        insertbackground="black"
    )


#manu bar
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
edit_menu = tk.Menu(menu)
mode_menu = tk.Menu(menu)

#new ,openfile,save,exit

#Add file manu to manubar 
menu.add_cascade(label="File",menu=file_menu)
#inside manu lable 
file_menu.add_command(label="New",command= new_file) #newfile 
file_menu.add_command(label="Open",command= open_file) #openfile 
file_menu.add_command(label="Save",command= save_file) #savefile 
file_menu.add_separator()
file_menu.add_command(label="Exit",command= root.quit)

#Add edit manubar
menu.add_cascade(label="Edit",menu=edit_menu)
#inside Edit lable 
edit_menu.add_command(label="Undo",command= undo_text)
edit_menu.add_command(label="Redo",command= redo_text)
edit_menu.add_command(label="Cut",command= cut_text)
edit_menu.add_command(label="Copy",command= copy_text)
edit_menu.add_command(label="Paste",command= paste_text)
edit_menu.add_command(label="Select All",command= select_all)

#add dark and light mode button
menu.add_cascade(label= "Mode",menu=mode_menu)
#inside darkmode button
mode_menu.add_command(label="DarkMood",command= dark_mode)
mode_menu.add_command(label="LightMood",command= light_mode)


#starts and keep the window open
root.mainloop()