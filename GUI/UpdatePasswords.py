#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:15:50 2020

@author: jasonsteffener
"""

from pronounceable import PronounceableWord
import numpy as np
import os
from xml.dom import minidom
import sys 

import xml.etree.ElementTree as ET
import xml
from xml.etree import ElementTree
from xml.dom import minidom
from tkinter import * 
from tkinter import messagebox
BaseDir = "/Users/jasonsteffener/Documents/GitHub/CognitiveTasksOnline/GUI"
sys.path.append(BaseDir)

def MakePassword():
    # Make a password as a pronouncable word plus two digits
    randomword = PronounceableWord().length(5,9)
    randomnumber = int(np.round(10+90*np.random.uniform()))
    Password = randomword + str(randomnumber)
    return Password

def ReadUsermapping(fileName):
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

def PrintUserList(UserList):
    for i in UserList:
        print(i)

def RemoveAuthorizedUser(UserList, PasswordList, UserToRemove):
    # Is the entered user in the list?
    try:
        UserIndex = UserList.index(UserToRemove)
        print("Removing user %s"%(UserToRemove))
        del UserList[UserIndex] 
        del PasswordList[UserIndex]
    except:
        print('User not found in list')
    return UserList, PasswordList

def TestReadXML(fileName):
    UserList, PasswordList = ReadUsermapping(fileName)
    PrintUserList(UserList)
    RemoveAuthorizedUser(UserList, PasswordList, 'Person001')
    PrintUserList(UserList)

def SelectUserFromList(UserList, PasswordList):
    # Create a GUI to select which use to delete
    master = Tk()

    variable = StringVar(master)
    variable.set(UserList[0]) # default value

    w = OptionMenu(master, variable, *UserList)
    w.pack()
    
    def WhatToDoWithSelectionFromList():
        global UserToRemove
        UserToRemove = variable.get()
        print ("value is:" + UserToRemove)
        master.destroy()
        
    button = Button(master, text="OK", command=WhatToDoWithSelectionFromList)
    button.pack()

    mainloop()
    # Remove this entry from the list and return the user list
    print("Use to remove is %s"%(UserToRemove))
    [UserList, PasswordList] = RemoveAuthorizedUser(UserList, PasswordList, UserToRemove)
    PrintUserList(UserList)

def WriteWithPrettify(tree, fileName):
    # Write out an XML file, making it pretty
    with open(fileName, 'w') as output:
     output.write(prettify(tree))

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def CreateXML():
    # Create the vey base XML file for user mapping for GUAC
    data = ET.Element('user-mapping')
    return data

def CreateNewUser(data, username, password):
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



[UserList, PasswordList] = ReadUsermapping("items004.xml")
CreateNewUser(data, username, password)

SelectUserFromList(UserList, PasswordList)

CreateXML()
CreateNewUser(data, username, password)