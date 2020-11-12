import wx 
class Mywin(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title,size = (350,300))
        # Make a panel
      panel = wx.Panel(self) 
        # This is the initial list
      languages = []   
        # This is a second list and used only for demonstration purposes
      NewList = ['a','b','c']  
        # Make a list box
      self.lst = wx.ListBox(panel, size = (100,300), choices = languages, style = wx.LB_SINGLE)
      # Initialize with an empty list
      self.List = []
      self.Selection = ''
      # Make a button
      self.btnPartEntry1 = wx.Button(panel,-1,label = "Check User List", pos = (100,200), size = ((100,50))) 
      self.btnPartEntry2 = wx.Button(panel,-1,label = "Delete Selected User", pos = (100,100), size = ((100,50))) 
      
      # Bind the button to a function and pass a list to it
      self.Bind(wx.EVT_BUTTON, lambda event: self.OnCickUpdateDisplayedList(event, NewList), self.btnPartEntry1)
      self.btnPartEntry2.Bind(wx.EVT_BUTTON, self.RemoveSelection)
      # Bind an action to the list box
      self.Bind(wx.EVT_LISTBOX, self.onListBox, self.lst) 
      panel.Fit() 
      
      self.Centre() 
      #self.Bind(wx.EVT_LISTBOX, self.onListBox, self.lst) 
      self.Show(True)  
      
    # Set the list into the text ctrl box
    
   def OnCickUpdateDisplayedList(self, event, list):
      # Once the list has been updated store it in the self variable so it can 
      # be passed between functions
      self.List = list
      self.lst.Set(list)
      
   def UpdateList(self):
        # An internal function for updating the list displayed on the screen
      self.lst.Set(self.List)
      
   def RemoveSelection(self, event):
        # Check the inyternal
      print(self.List)
      print("Hello")
      # Remove the selected item from the list
      self.List.remove(self.Selection)
      self.UpdateList()
      
      
   def onListBox(self, event):
        # Get the selected user from the list
      Selection = event.GetEventObject().GetStringSelection()
        # print the selected user
      print(Selection)
      self.Selection = Selection
      
ex = wx.App() 
Mywin(None,'ListBox Demo') 
ex.MainLoop()