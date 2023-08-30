import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, colorchooser
import os


class NotepadApp:
    def __init__(self, root):
        self.root = root

        self.root.title("Untitled - Notepad")
        #self.root.wm_iconbitmap("th.ico")
        self.root.geometry("710x455")
        self.root.minsize(100, 100)

        self.modified = False
        self.text_changes = []  # Keep track of text changes for Undo

        self.text_area = tk.Text(root, font="lucida  13", fg="red", wrap=tk.WORD)
        self.text_area.pack(expand=tk.YES, fill=tk.BOTH)
        # Set the focus on the text area when program run cursor present textarea
        self.text_area.focus_set()

        self.text_area.bind("<Key>", self.mark_as_modified)
        self.text_area.bind("<Key>", self.on_text_change)
        self.text_area.bind("<Control-z>", self.undo)

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # call fucntion creat_menu here
        self.create_menu()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # add scrollbar feature
        self.scrollbar = tk.Scrollbar(self.text_area)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y, ipady=1, ipadx=1)
        self.scrollbar.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scrollbar.set)

    def create_menu(self):
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="     File    ", menu=file_menu)
        file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="New window", accelerator="Ctrl+Shift+N", command=self.open_new_window)
        file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.exit_app)

        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="    Edit   ", menu=edit_menu)
        edit_menu.add_command(label="Cut ", accelerator=" Ctrl+X " , command=self.cut)
        edit_menu.add_command(label="Copy ", accelerator=" Ctrl+C ", command=self.copy)
        edit_menu.add_command(label="Paste ", accelerator=" Ctrl+V ", command=self.paste)
        edit_menu.add_command(label="Undo  ", accelerator=" Ctrl+Z", command=self.undo)

        format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="   Format   ", menu=format_menu)
        format_menu.add_command(label="Change Font", accelerator="Ctrl+F", command=self.change_font)
        format_menu.add_command(label="Font Color", accelerator="Ctrl+Shift+C", command=self.change_font_color)

        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="    Help  ", menu=help_menu)
        help_menu.add_command(label="About Notepad", command=self.about)

        self.root.bind_all("<Control-n>", lambda event: self.new_file())
        self.root.bind_all("<Control-Shift-N>", lambda event: self.open_new_window())
        self.root.bind_all("<Control-o>", lambda event: self.open_file())
        self.root.bind_all("<Control-s>", lambda event: self.save_file())
        self.root.bind_all("<Control-q>", lambda event: self.exit_app())
        self.root.bind_all("<Control-x>", lambda event: self.cut())
        self.root.bind_all("<Control-c>", lambda event: self.copy())
        self.root.bind_all("<Control-v>", lambda event: self.paste())
        self.root.bind_all("<Control-z>", lambda event: self.undo())
        self.root.bind_all("<Control-f>", lambda event: self.change_font())
        self.root.bind_all("<Control-Shift-C>", lambda event: self.change_font_color())

    def on_text_change(self, event):
        self.mark_as_modified()
        self.text_changes.append(self.text_area.get("1.0", "end-1c"))

    def undo(self, event=None):
        if self.text_changes:
            self.text_changes.pop()  # Remove the latest change
            if self.text_changes:
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert("1.0", self.text_changes[-1])
            else:
                self.text_area.delete("1.0", tk.END)
            self.mark_as_modified()

    def mark_as_modified(self, event=None):
        if not self.modified:
            self.modified = True
            self.update_title()

    def update_title(self):
        if self.modified:
            self.root.title("*" + self.root.title().lstrip("*"))
        else:
            self.root.title(self.root.title().lstrip("*"))

    def new_file(self):
        if self.modified:
            result = self.check_save_changes()

            if result == False:
                return
        self.text_area.delete(1.0, tk.END)
        self.root.title("Untitled - Notepad")
        self.modified = False
        self.update_title()

    def open_file(self):
        if self.modified:
            result = self.check_save_changes()
            if result == "cancel":
                return
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
                self.root.title(os.path.basename(file_path) + " - Notepad")
                self.modified = False
                self.update_title()

    def open_new_window(self, content=""):
        new_root = tk.Tk()
        new_app = NotepadApp(new_root)
        new_app.text_area.insert(tk.END, content)
        new_root.mainloop()

    def save_file(self):
        if self.root.title() == "*Untitled - Notepad":
            print("untitle", self.root.title() == "Untitled - Notepad")
            self.save_file_as()
        else:
            content = self.text_area.get(1.0, tk.END)
            file_path = self.root.title().replace("*", "").replace(" - Notepad", "")
            with open(file_path, "w") as file:
                file.write(content)
            self.modified = False
            self.update_title()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            content = self.text_area.get(1.0, tk.END)
            with open(file_path, "w") as file:
                file.write(content)
            self.root.title(os.path.basename(file_path) + " - Notepad")
            self.modified = False
            self.update_title()

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def about(self):
        messagebox.showinfo("About Notepad",
                            "This is a simple Notepad application created using Python and Tkinter and devloped by praveen.")

    def exit_app(self):
        if self.check_save_changes():
            self.root.destroy()

    def on_closing(self):
        if self.check_save_changes():
            self.root.destroy()

    def check_save_changes(self):
        if self.modified:
            result = messagebox.askyesnocancel("Save Changes", "Do you want to save changes?")

            if result is None or False:
                return False
            elif result:
                self.save_file()
        return True

    def change_font(self):
        font = simpledialog.askstring("Font", "Enter font details (e.g., Arial 12)")
        if font:
            try:
                self.text_area.config(font=font)
            except tk.TclError:
                messagebox.showerror("Error", "Invalid font format. Please provide a valid font name and size.")

    def change_font_color(self):
        color = colorchooser.askcolor(title="Select Font Color")[1]
        if color:

            try:

                self.text_area.tag_add("color", tk.SEL_FIRST, tk.SEL_LAST)

                self.text_area.tag_configure("color", font=f"{color}", foreground=color)

                self.text_area.update()

            except Exception as e:

                self.text_area.update()


if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()

