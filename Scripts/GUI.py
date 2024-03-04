import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk

class MultiColumnListbox(object):
    """use a ttk.TreeView as a multicolumn ListBox"""

    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()
        

    def _setup_widgets(self):
        s = """\click on header to sort by that column
to change width of column drag boundary
        """
        msg = ttk.Label(wraplength="4i", justify="left", anchor="n",
            padding=(10, 2, 10, 6), text=s)
        # msg.pack(fill='x')
        container = ttk.Frame()
        container.pack(fill='both', expand=True)
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=headers, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        b1 = tk.Button(container,text = "Apply")
        b1.grid(column=2, row=0,sticky=tk.E)

    def _build_tree(self):
        for col in headers:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))

        for item in entries:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(headers[ix],width=None)<col_w:
                    self.tree.column(headers[ix], width=col_w)

def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
        int(not descending)))

def apply(event):
    pass

# the test data ...

headers = ['car', 'repair','is true']
entries = [
('Hyundai', 'brakes',True) ,
('Honda', 'light',True) ,
('Lexus', 'battery',True) ,
('Benz', 'wiper',True) ,
('Ford', 'tire',True) ,
('Chevy', 'air',True) ,
('Chrysler', 'piston',True) ,
('Toyota', 'brake pedal',True) ,
('BMW', 'seat',True)
]

root = tk.Tk()
root.title("Multicolumn Treeview/Listbox")
listbox = MultiColumnListbox()
b1 = tk.Button(root, text = "Apply")
# b1.grid(row=1,column=1,sticky=tk.E)
root.mainloop()