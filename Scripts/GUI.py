import wx 
import Database
import config
import sys 

class Mywin(wx.Frame): 
            
    def __init__(self, parent, title): 
        super(Mywin, self).__init__(parent, title = title,size = (600,500))

        panel = wx.Panel(self) 
        box = wx.BoxSizer(wx.HORIZONTAL) 

        db = Database.Database()

        db.openConnection()

        data = db.get_data(config.DB_COLLECTION)
            
        self.list = wx.ListCtrl(panel, -1, style = wx.LC_REPORT) 
        self.list.InsertColumn(0, 'Position', width = 100) 
        self.list.InsertColumn(1, 'Company', wx.LIST_FORMAT_RIGHT, 100) 
        self.list.InsertColumn(2, 'Location', wx.LIST_FORMAT_RIGHT, 100) 
        self.list.InsertColumn(3, 'URL', wx.LIST_FORMAT_RIGHT, 100) 
        self.list.InsertColumn(4, 'Applied', wx.LIST_FORMAT_RIGHT, 100) 
        for i in data: 
            index = self.list.InsertStringItem(self.list.GetItemCount(), i["Title"]) 
            self.list.SetItem(index, 1, i["company"]) 
            self.list.SetItem(index, 2, i["location"]) 
            self.list.SetItem(index, 3, i["link"]) 
            self.list.SetItem(index, 4, str(False)) 
        
        self.text = wx.StaticText(panel, label="")

        button = wx.Button(panel, wx.ID_ANY, 'Apply', (10, 10))
        button.Bind(wx.EVT_BUTTON, self.onButton)
        
        box.Add(self.list,1,wx.EXPAND) 
        box.Add(self.text, 1, wx.EXPAND)
        box.Add(button, wx.EXPAND)

        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onListBox, self.list) 
        
        panel.SetSizer(box) 
        panel.Fit() 
        self.Centre() 
            
        self.Show(True)  

    def onButton(self, event):
        print("Button pressed.")

    def onListBox(self, event): 
        choice= self.list.GetFirstSelected()
        item = self.list.GetItem(itemIdx=choice, col=0)
        textItem=item.GetText()
        print(choice)
        print(textItem)
        self.text.SetLabel(textItem)

ex = wx.App() 
Mywin(None,'ListBox Demo') 
ex.MainLoop()