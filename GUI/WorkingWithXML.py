#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:12:22 2020

@author: jasonsteffener
"""
import xml.etree.ElementTree as ET
from xml.etree import ElementTree
from xml.dom import minidom
import numpy as np
import pandas as pd
import shutil
import os
import pyperclip
from pronounceable import PronounceableWord

XMLInputPath = '/Users/jasonsteffener/Documents/GitHub/CognitiveTasksOnline/GUI'
XMLInputFile = 'items004.xml'
fileName = os.path.join(XMLInputPath, XMLInputFile)
print(os.path.exists(fileName))
tree = ET.parse(fileName)
root = tree.getroot()
# What is the VNC Password?
VNCPassword = root[0][0][3].text

''' Load up the XML file. Instead of rewriting it each time
just add and remove authorized users
Each athorized user is assigned one or more connections.

root[i] is the list of users
root[i][j] is the list of connections (j) for user i
For each connection there are four items

For new users add a new user to root[0]
Functions
read XML file
find if a user is in the XML
remove a user
add a user
remove a connection from a user
add a connection to a user
save to file
'''
def AddUser(data, username, password):
     # Create the authorization for a GUAC user.
     # Note the hardcoded VNC password!
     user01level1 = ET.SubElement(data, 'authorize')
     user01level1.set('username',username)
     user01level1.set('password',password)
     
def RemoveUser(root, username):
    # Find the supplied user name ane remove it
    # Remove a user
    for child in root.findall('authorize'):
        n = child.get('username')
        if n == username:
            root.remove(child)
            
def RemoveConnection(root, connectionName):
    # Find the connection and remove it for everyone
    for child in root.findall('authorize'):
        for elem in child.findall('connection'):
            n = elem.get('name')
            if n == connectionName:
                child.remove(elem)

                 
def AddConnection(data, username, port, connectionName):
    # Once a user is made, add connections to it
    for child in root.findall('authorize'):
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
             user01level3d.text = 'VNCPASSWORD'
             

   