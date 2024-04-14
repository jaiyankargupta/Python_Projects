class NotepadGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        
        self.textarea = tk.Text(root, wrap="word", undo=True)
        self.textarea.pack(expand=True, fill="both")
        
        self.menubar = tk.Menu(root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        
        self.filemenu.add_command(label="New", command=lambda: backend.new_file(self.textarea))
        self.filemenu.add_command(label="Open", command=lambda: backend.open_file(self.textarea))
        self.filemenu.add_command(label="Save", command=lambda: backend.save_file(self.textarea))
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=lambda: backend.quit_app(self.root))
        
        self.editmenu.add_command(label="Cut", command=lambda: backend.cut_text(self.textarea))
        self.editmenu.add_command(label="Copy", command=lambda: backend.copy_text(self.textarea))
        self.editmenu.add_command(label="Paste", command=lambda: backend.paste_text(self.textarea))
        
        self.helpmenu.add_command(label="About Notepad", command=self.about)
        
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        
        self.root.config(menu=self.menubar)
        
        self.scrollbar = tk.Scrollbar(self.textarea)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.textarea.yview)
        self.textarea.config(yscrollcommand=self.scrollbar.set)
    
    def about(self):
        messagebox.showinfo("About Notepad", "This is a simple notepad application.")
