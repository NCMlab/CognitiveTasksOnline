import wx 
import xml.etree.ElementTree as ET
from xml.dom import minidom
import numpy as np
import pandas as pd
import shutil
import os
import sys
from pronounceable import PronounceableWord

XMLInputPath = '/etc/guacamole'
XMLInputPath = '/Users/jasonsteffener/Documents/GitHub/XMLtemp'
sys.path.insert(0,XMLInputPath)
from GuacURL import *

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
      #self.XMLInputPath = '/Users/jasonsteffener/Documents/GitHub/XMLtemp'

      self.XMLInputFile = 'user-mapping.xml'
      self.AuthUserFile = 'AuthUser'
      self.VNCPassword = ''
      
      self.GuacURL = GuacURL
      # Create a connection list. These are all possible desktop connections
      # that are available. Essentially, these are the VNC connections
      self.DesktopPortList = ['5911','5912','5913','5914','5915']
      # Load up the authorized user list
      self.LoadAuthorizedUserList(os.path.join(XMLInputPath,self.AuthUserFile))
      # Once the GUI is open. Check the user list and load it
      self.OnCickUpdateDisplayedList(0)
      # Make list of unused ports
      PortList = self.MakeListOfUsedPorts()
      print(PortList)
      self.FindAvailablePorts(PortList)
      print(self.AvailablePorts)
      # When the user list is checked. First the internal list is checked. If it is empty, then load up the XML 
      # file. If it is not empty then just check the internal file.
      # self.btnPartEntry1 = wx.Button(panel,-1,label = "Check User List", pos = (100,0), size = ((200,50))) 
      # Make a subid text entry
      self.PartID = wx.TextCtrl(panel,-1,'',size=(130,30),pos = (190,30))
      self.btnPartEntry3 = wx.Button(panel,-1,label = "Add User", pos = (100,30), size = ((80,30))) 
      self.btnPartEntry2 = wx.Button(panel,-1,label = "Delete Selected User", pos = (100,60), size = ((200,30)))
      self.btnPartEntry4 = wx.Button(panel,-1,label = "Save Login File", pos = (100,90), size = ((200,30))) 
      self.btnPartEntry6 = wx.Button(panel,-1,label = "Create Login Text for User", pos = (100,120), size = ((200,30))) 
      self.btnPartEntry5 = wx.Button(panel,-1,label = "Close", pos = (100,220), size = ((200,30))) 
      
      
      
      # Bind the button to a function and pass a list to it
      # self.Bind(wx.EVT_BUTTON, lambda event: self.OnCickUpdateDisplayedList(event), self.btnPartEntry1)
      self.btnPartEntry2.Bind(wx.EVT_BUTTON, self.RemoveUser)
      self.btnPartEntry3.Bind(wx.EVT_BUTTON, self.AddUser)
      self.btnPartEntry4.Bind(wx.EVT_BUTTON, self.SaveLoginFile)
      self.btnPartEntry5.Bind(wx.EVT_BUTTON, self.CloseGUI)
      self.btnPartEntry6.Bind(wx.EVT_BUTTON, self.MakeEmail)
      
      # Bind an action to the list box
      self.Bind(wx.EVT_LISTBOX, self.onListBox, self.lst) 
      panel.Fit() 
      
      self.Centre() 
      #self.Bind(wx.EVT_LISTBOX, self.onListBox, self.lst) 
      self.Show(True)  

      
      
    # Set the list into the text ctrl box
    
   def OnCickUpdateDisplayedList(self, event):
      # Check to see if the internal list is empty
      # If it is, than load up the user login file
      if self.UserList == '':
        UserList = self.ReadUsermapping(os.path.join(XMLInputPath, self.XMLInputFile))
        # Once the list has been updated store it in the self variable so it can 
        # be passed between functions
      else: 
        UserList = self.UserList
        # PasswordList = self.PasswordList
      print(UserList)
      self.UserList = UserList
      # self.PasswordList = PasswordList
      # print(PasswordList)
      # Once the list is loaded up, compare each item to teh auth user list
      # If someone is an authorized user then remove them from the list displayed
      self.RemoveAuthListFromInternalList()
      print(self.UserList)
      # Write the user list to the GUI
      self.lst.Set(self.UserList)
      
   def UpdateList(self):
        # An internal function for updating the list displayed on the screen
      self.lst.Set(self.UserList)
      
   def RemoveUser(self, event):
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
            # Fin dthe selected username
            username = self.UserList[index]
            # remove them from the internal list
            self.UserList.remove(self.UserList[index])
            # update the screen
            self.UpdateList()
            # reset the internal selection variable
            self.Selection = ''
            # Find this users connection name
            connectionName = self.XMLFindConnectionName(username)
            # Remove this connection for everyone
            self.XMLRemoveConnection(connectionName)
            # Remove user from the XML
            self.XMLRemoveUser(username)
<<<<<<< Updated upstream
            
            self.FindAvailablePorts(self.MakeListOfUsedPorts())
            
            # Make sure to remove the connection for this port also
=======
            # Cycle over authorized users
            self.FindAvailablePorts(self.MakeListOfUsedPorts())

>>>>>>> Stashed changes
   
   def AddUser(self, event):
        # Check to see if anything has been entered
      UserToAdd = self.PartID.GetValue()
      if UserToAdd == '':
            wx.MessageBox('You need to enter a User ID', 'Warning',
                                     wx.OK | wx.ICON_WARNING)
      else:
          # Check to see if there are any ports avalable.
          # If not then a user cannot be added
            if len(self.AvailablePorts) > 0:
                # Add the new user to the list
                self.UserList.append(UserToAdd)
                # Create a Password
                NewPassword = self.MakePassword()
                # self.PasswordList.append(NewPassword)
                # print(self.PasswordList)
                
                # Find an unused port
                port = self.AvailablePorts[0]
                print(port)
                # Add the user to the XML
                self.XMLAddUser(UserToAdd, NewPassword)
                
                # Add connections
                connectionName = UserToAdd+'_'+port
                self.XMLAddConnection(UserToAdd, port, connectionName)
                self.AddNewConnectionToAuthUsers(port, connectionName)
                self.FindAvailablePorts(self.MakeListOfUsedPorts())
                print(self.MakeListOfUsedPorts())
            else:
                wx.MessageBox('Sorry, there are not available ports! Try removing a user', 'Warning',
                                     wx.OK | wx.ICON_WARNING)
            
            # When a user is added add their desktop access to all authorized users
      # Update the available ports list
      
      # Update the list
      self.UpdateList()
      # Reset the text entry 
      self.PartID.SetValue('')
      
   def AddNewConnectionToAuthUsers(self, port, connectionName):
       print("adding new users connection to Auth users also")
       for i in self.AuthList['Username']:
           print("adding to %s"%(i))
           self.XMLAddConnection(i, port, connectionName)   
           
   def onListBox(self, event):
        # Get the selected user from the list
      Selection = event.GetEventObject().GetStringSelection()
        # print the selected user
      print(Selection)
      self.Selection = Selection
   
   def ReadUsermapping(self, fileName):
        # Read the user-mapping.xml file and make a list of the authorized users 
        # and their passwords
        print(os.path.exists(fileName))
        tree = ET.parse(fileName)
        root = tree.getroot()
        # What is the VNC Password?
        self.VNCPassword = root[0][0][3].text
        # How many user mappings
        NUsers = len(root)
        # Make list of user mappings
        UserList = []
        # PasswordList = []
        for i in range(NUsers):
            UserList.append(root[i].attrib['username'])
            # PasswordList.append(root[i].attrib['password'])
            
        # print(UserList)
        # print(PasswordList)
        print(self.VNCPassword)
        # Save the root XML to self so it can be used
        self.XML = root
        return UserList
   
   def SaveLoginFile(self, event):
        # Make a copy of the old XML file first
        BackupName = 'BACKUP_' + self.XMLInputFile
        shutil.copy(os.path.join(XMLInputPath, self.XMLInputFile),os.path.join(XMLInputPath, BackupName))
        
        self.WriteWithPrettify(self.XMLInputFile)
      
   def CreateXML(self):
        # Create the base XML file for user mapping for GUAC
        data = ET.Element('user-mapping')
        print(data)
        return data      
    
   def MakePassword(self):
        # Make a password as a pronouncable word plus two digits
        randomword = PronounceableWord().length(5,9)
        randomnumber = int(np.round(10+90*np.random.uniform()))
        Password = randomword + str(randomnumber)
        return Password
    
   def WriteWithPrettify(self, fileName):
       # Write out an XML file, making it pretty
       with open(os.path.join(XMLInputPath,fileName), 'w') as output:
             output.write(self.prettify(self.XML))
        # Clean up the XML file and remove the extra blank lines
       with open(os.path.join(XMLInputPath,fileName)) as xmlfile:
           lines = [line for line in xmlfile if line.strip() != ""]

       with open(os.path.join(XMLInputPath,fileName), "w") as xmlfile:
           xmlfile.writelines(lines)

   def prettify(self, elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

   def MakeEmail(self, event):
       # Change this so that it reads the XML instead of an internal list
       # This way an internal list is not stored and worked with
       if self.Selection != '':
            username = self.Selection
            Str = "Please visit the site: %s \n"%(self.GuacURL)
            Str = Str + "Use the following login and password for access\n"
            Str = Str + "Username: %s \n"%(username)
            Str = Str + "Password: %s \n"%(self.XMLFindUserPassword(username))
            wx.MessageBox(Str, 'Login Information',
                                     wx.OK | wx.ICON_WARNING)
          
   def LoadAuthorizedUserList(self, fileName):
       self.AuthList = pd.read_csv(fileName)
          
   def HowManyDesktopsAreUsed():
       pass

   def CompareUserToAuthList(self, AuthList, TestUser):
        # Check to see if this user is in the authorized user list
        return AuthList.loc[AuthList['Username'] == TestUser].shape[0] > 0
    
       
   def RemoveAuthListFromInternalList(self):
       for i in self.UserList:
           # Is this an authorized user?
           if self.AuthList.loc[self.AuthList['Username'] == i].shape[0] > 0:
               # If the user is an authorized user, find their index in the list
               self.UserList[self.UserList.index(i)] = 'XXXXX'
       self.UserList = [k for k in self.UserList if not 'XXXXX' in k]       
       

   def MakeListOfUsedPorts(self):
        PortList = []
        for child in self.XML.findall('authorize'):
            # if this user is NOT on the authorizde list, find their port number
            if not self.AuthList.loc[self.AuthList['Username'] == child.get('username')].shape[0] > 0:
                for elem in child.findall('connection'):
                    for i in elem.findall('param'):
                        n = i.get('name')
                        if n == 'port':
                            PortList.append(i.text)
        return PortList


   def FindAvailablePorts(self, PortList):
        AvailablePorts = []
        for i in self.DesktopPortList:
            if not i in PortList:
                AvailablePorts.append(i)
        self.AvailablePorts = AvailablePorts
         
   def XMLFindUserPassword(self, username):
    for child in self.XML.findall('authorize'):
        n = child.get('username')
        if n == username:
            pw = child.get('password')
    return pw

   def XMLAddUser(self, username, password):
         # Create the authorization for a GUAC user.
         # Note the hardcoded VNC password!
         user01level1 = ET.SubElement(self.XML, 'authorize')
         user01level1.set('username',username)
         user01level1.set('password',password)
         
   def XMLRemoveUser(self, username):
        # Find the supplied user name ane remove it
        # Remove a user
        for child in self.XML.findall('authorize'):
            n = child.get('username')
            if n == username:
                self.XML.remove(child)
                
   def XMLRemoveConnection(self, connectionName):
        # Find the connection and remove it for everyone
        for child in self.XML.findall('authorize'):
            for elem in child.findall('connection'):
                n = elem.get('name')
                if n == connectionName:
                    child.remove(elem)
    
                     
   def XMLAddConnection(self, username, port, connectionName):
        # Once a user is made, add connections to it
        for child in self.XML.findall('authorize'):
            n = child.get('username')
            if n == username:
                
                 user01level2 = ET.SubElement(child, 'connection')
                 user01level2.set('name',connectionName)
                 user01level3a = ET.SubElement(user01level2, 'protocol')
                 user01level3a.text = 'vnc'
                 user01level3b = ET.SubElement(user01level2, 'param')
                 user01level3b.set('name','hostname')
                 user01level3b.text = 'localhost'
                 user01level3c = ET.SubElement(user01level2, 'param')
                 user01level3c.set('name','port')
                 user01level3c.text = port
                 user01level3d = ET.SubElement(user01level2, 'param')
                 user01level3d.set('name','password')
                 user01level3d.text = self.VNCPassword

   def XMLFindConnectionName(self, userName):
       # Find the user
       for child in self.root.findall('authorize'):
           tempUser  = child.get('username')
           if tempUser == userName:
               # Find their connection name
               # This assumes each user has one connection
               for elem in child.findall('connection'):
                   ConnectionName = elem.get('name')
       return ConnectionName
             
             
   def CloseGUI(self, event):
       self.Close()

    
ex = wx.App() 
s = Mywin(None,'ListBox Demo') 
ex.MainLoop()
