#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 21:50:04 2020

@author: jasonsteffener
"""

import wx

Top = 20
Left = 20
RowWidth = 80
ColWidth = 140
# Button height cannot be changed
ButtonHeight = -1
ButtonWidth = 120
LabelOffset = 10
BoxVerticalShift = 12
# Allow flexible number of rows
NRows =  6
# Create a list of what pixel each row is to be set to
RowPixel = []
for i in range(NRows):
    RowPixel.append(Top + i*RowWidth)
# Use the number of rows to define the GUI height
GUIHeight = max(RowPixel) + RowWidth


# Allow flexible number of columns
NCols =  4
# Create a list of what pixel each row is to be set to
ColPixel = []
for i in range(NCols):
    ColPixel.append(Top + i*ColWidth)
# Use the number of rows to define the GUI height
GUIWidth = max(ColPixel) + 2*ColWidth
NColForBox = NCols

class PopMenu(wx.Menu): 
    # This creates a pop-up list of items next to the button that calls it
    def __init__(self, parent, list): 
        # Take a list of items and use these to make the list
        super(PopMenu, self).__init__() 
        self.parent = parent 
        for i in list:
            popmenu = wx.MenuItem(self, wx.NewId(), i)
            self.Append(popmenu) 


class Mywin(wx.Frame): 
   def __init__(self, parent, title): 
    # size = (width, height)
    # Create the GUI window
      super(Mywin, self).__init__(parent, title = title,size = (GUIWidth,GUIHeight))  
      self.panel = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
      

      
      self.VisitFolderPath = 'empty'
      # Setup Row One
      self.PartIDLabel = wx.StaticText(self.panel, -1, label = "Participant ID:", pos = (ColPixel[0],RowPixel[0]))
#      self.PartID = wx.TextCtrl(self.panel,-1,'9999999',size=(ButtonWidth,-1),pos = (ColPixel[1],RowPixel[0]))
      self.btnPartEntry1 = wx.Button(self.panel,-1,label = "Check User List", pos = (ColPixel[0],RowPixel[4]), size = ((ButtonWidth, ButtonHeight))) 
      self.btnPartEntry2 = wx.Button(self.panel,-1,label = "Remove User", pos = (ColPixel[1],RowPixel[4]), size = ((ButtonWidth, ButtonHeight))) 
      self.btnPartEntry3 = wx.Button(self.panel,-1,label = "Three", pos = (ColPixel[2],RowPixel[0]), size = ((ButtonWidth, ButtonHeight))) 
      
      self.btnPartEntry1.Bind(wx.EVT_BUTTON, self.OnCickPartEntry)
#      self.PartIDLabel = wx.StaticText(self.panel, -1, label = "Output folder:", pos = (ColPixel[3], RowPixel[0]))
      
      # Center the GUI In the screen
      self.Centre() 
      # SHow the GUI to the user
      self.Show() 
      
   def OnCickPartEntry(self, event):
        languages = ['aaaa','bbbbb','ccccc','dddd']
        #lst = wx.ListBox(self.panel, size = (200,100),  choices = languages, style = wx.LB_SINGLE)
        self.PopupMenu(PopMenu(self,languages)) 
        
        
print('Got Here 1')
app = wx.App() 
print('Got Here 2')
# Create the GUI
MyGui = Mywin(None,  'NCM Lab') 
# Disable all the buttons except teh Part ID entry 
app.MainLoop()