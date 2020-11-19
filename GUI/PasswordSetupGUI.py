import wx 
import xml.etree.ElementTree as ET
from pronounceable import PronounceableWord

class Mywin(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title,size = (350,300))
        # Make a panel
      panel = wx.Panel(self) 
        # This is the initial list
      languages = []   
        # This is a second list and used only for demonstration purposes
        # Make a list box
      self.lst = wx.ListBox(panel, size = (100,300), choices = languages, style = wx.LB_SINGLE)
      # Initialize with an empty list
      self.UserList = ''
      self.PasswordList = ''
      self.Selection = ''
      # When the user list is checked. First the internal list is checked. If it is empty, then load up the XML 
      # file. If it is not empty then just check the internal file.
      self.btnPartEntry1 = wx.Button(panel,-1,label = "Check User List", pos = (100,0), size = ((150,50))) 
      # Make a subid text entry
      self.PartID = wx.TextCtrl(panel,-1,'',size=(130,-1),pos = (210,50))
      self.btnPartEntry3 = wx.Button(panel,-1,label = "Add User", pos = (100,35), size = ((100,50))) 
      self.btnPartEntry2 = wx.Button(panel,-1,label = "Delete Selected User", pos = (100,100), size = ((150,50))) 
      self.btnPartEntry4 = wx.Button(panel,-1,label = "Save Login File", pos = (100,200), size = ((150,50))) 
      
      
      
      # Bind the button to a function and pass a list to it
      self.Bind(wx.EVT_BUTTON, lambda event: self.OnCickUpdateDisplayedList(event), self.btnPartEntry1)
      self.btnPartEntry2.Bind(wx.EVT_BUTTON, self.RemoveSelection)
      self.btnPartEntry3.Bind(wx.EVT_BUTTON, self.AddUser)
      self.btnPartEntry4.Bind(wx.EVT_BUTTON, self.SaveLoginFile)
      # Bind an action to the list box
      self.Bind(wx.EVT_LISTBOX, self.onListBox, self.lst) 
      panel.Fit() 
      
      self.Centre() 
      #self.Bind(wx.EVT_LISTBOX, self.onListBox, self.lst) 
      self.Show(True)  
      
    # Set the list into the text ctrl box
    
   def OnCickUpdateDisplayedList(self, event):
      # Check to see if the internal lus is empty
      # If it is then load up the user login file
      if self.UserList == '':
        [UserList, PasswordList] = self.ReadUsermapping("items004.xml")
        # Once the list has been updated store it in the self variable so it can 
        # be passed between functions
      else: 
        UserList = self.UserList
        PasswordList = self.PasswordList
      self.UserList = UserList
      self.PasswordList = PasswordList
      print(PasswordList)
      # Write the user list to the GUI
      self.lst.Set(UserList)
      
   def UpdateList(self):
        # An internal function for updating the list displayed on the screen
      self.lst.Set(self.UserList)
      
   def RemoveSelection(self, event):
      # Remove the selected item from the list
      # Check to see if anything is selected
      if self.Selection != '':
        # Add a warning to double check
        resp = wx.MessageBox('You have selected to delete user %s. Are you sure?'%(self.Selection), 'Warning',
                                     wx.OK | wx.CANCEL | wx.ICON_WARNING)
        if resp == wx.OK:
            # remove the item
            # Find where in the list the item is
            index = self.UserList.index(self.Selection)
            self.UserList.remove(self.UserList[index])
            self.PasswordList.remove(self.PasswordList[index])
            self.UpdateList()
            # reset the internal selection variable
            self.Selection = ''

   
   def AddUser(self, event):
        # Check to see if anything has been entered
      UserToAdd = self.PartID.GetValue()
      if UserToAdd == '':
            resp = wx.MessageBox('You need to enter a User ID', 'Warning',
                                     wx.OK | wx.ICON_WARNING)

      else:
            # Add the new user to the list
            self.UserList.append(UserToAdd)
            # Create a Password
            self.PasswordList.append(self.MakePassword())
            
      # Update the list
      self.UpdateList()
      # Reset the text entry 
      self.PartID.SetValue('')
            
   def onListBox(self, event):
        # Get the selected user from the list
      Selection = event.GetEventObject().GetStringSelection()
        # print the selected user
      print(Selection)
      self.Selection = Selection
   
   def ReadUsermapping(self, fileName):
        # Read the user-mapping.xml file and make a list of the authorized users 
        # and their passwords
        tree = ET.parse(fileName)
        root = tree.getroot()
        # How many user mappings
        NUsers = len(root)
        # Make list of user mappings
        UserList = []
        PasswordList = []
        for i in range(NUsers):
            UserList.append(root[i].attrib['username'])
            PasswordList.append(root[i].attrib['password'])
            
        # print(UserList)
        # print(PasswordList)
        return UserList, PasswordList
        
   def SaveLoginFile(self, event):
     # Create the out XML file
      data = self.CreateXML()
      
   def CreateXML(self):
        # Create the vey base XML file for user mapping for GUAC
        data = ET.Element('user-mapping')
        print(data)
        return data      
        
   def CreateNewUser(self, data, username, password):
    # Create the authorization for a GUAC user.
    # Note the hardcoded VNC password!
    user01level1 = ET.SubElement(data, 'authorize')
    user01level1.set('username',username)
    user01level1.set('password',password)
    
    user01level2 = ET.SubElement(user01level1, 'connection')
    user01level3a = ET.SubElement(user01level2, 'protocol')
    user01level3a.text = 'vnc'
    user01level3b = ET.SubElement(user01level2, 'param')
    user01level3b.set('name','hostname')
    user01level3b.text = 'localhost'
    user01level3c = ET.SubElement(user01level2, 'param')
    user01level3c.set('name','port')
    user01level3c.text = '5901'
    user01level3d = ET.SubElement(user01level2, 'param')
    user01level3d.set('name','password')
    user01level3d.text = 'VNCPASSWORD'
    return data
    
   def MakePassword(self):
    # Make a password as a pronouncable word plus two digits
    randomword = PronounceableWord().length(5,9)
    randomnumber = int(np.round(10+90*np.random.uniform()))
    Password = randomword + str(randomnumber)
    return Password
    
ex = wx.App() 
Mywin(None,'ListBox Demo') 
ex.MainLoop()