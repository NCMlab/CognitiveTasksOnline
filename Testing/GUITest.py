import wx
########################################################################
class MyPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        
        self.Bind(wx.EVT_KEY_DOWN, self.onKey)
        
    #----------------------------------------------------------------------
    def onKey(self, event):
        """
        Check for ESC key press and exit is ESC is pressed
        """
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_ESCAPE:
            self.GetParent().Close()
        else:
            event.Skip()
        
    
########################################################################
class MyFrame(wx.Frame):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Test FullScreen")
        self.panel = MyPanel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.btnPartEntry = wx.Button(self.panel,-1,label = "Submit") 
        self.btnPartEntry.Bind(wx.EVT_BUTTON, self.Submit)
        
        main_sizer.AddStretchSpacer()
        main_sizer.Add(self.btnPartEntry, 0, wx.CENTER)
        main_sizer.AddStretchSpacer()
        
        self.panel.SetSizer(main_sizer)
        
        self.ShowFullScreen(True)
    def Submit(self, event):
        dlg = PasswordDialog(frame)
        dlg.ShowModal()
        # dlg.result is now set to 'None' if the user cancelled, else to
        # the password string
        if dlg.result == "JASON":
            self.Close()
        
# Very minimalist password entry dialogue
class PasswordDialog(wx.Dialog):
    def __init__(self, parent, id=-1, title="Enter password"):
        wx.Dialog.__init__(self, parent, id, title, size=(320, 160))
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.label = wx.StaticText(self, label="Enter password:")
        self.field = wx.TextCtrl(self, value="", size=(300, 20), style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        self.okbutton = wx.Button(self, label="OK", id=wx.ID_OK)
        self.cancelbutton = wx.Button(self, label="Cancel", id=wx.ID_CANCEL)
        self.mainSizer.Add(self.label, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.field, 0, wx.ALL, 8 )
        self.buttonSizer.Add(self.okbutton, 0, wx.ALL, 8 )
        self.buttonSizer.Add(self.cancelbutton, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.buttonSizer, 0, wx.ALL, 0)
        self.Bind(wx.EVT_BUTTON, self.onOK, id=wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
        self.Bind(wx.EVT_TEXT_ENTER, self.onOK)
        self.SetSizer(self.mainSizer)
        self.result = None

    def onOK(self, event):
        self.result = self.field.GetValue()
        self.Destroy()

    def onCancel(self, event):
        self.Destroy()        



if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
    