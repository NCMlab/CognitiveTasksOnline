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


XMLInputPath = '/Users/jasonsteffener/Documents/GitHub/XMLtemp'
XMLInputFile = 'user-mapping.xml'
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
             

def MakeListOfUsedPorts(root):
    PortList = []
    for child in root.findall('authorize'):
        # if this user is NOT on the authorizde list, find their port number
        if not AuthList.loc[AuthList['Username'] == child.get('username')].shape[0] > 0:
            for elem in child.findall('connection'):
                for i in elem.findall('param'):
                    n = i.get('name')
                    if n == 'port':
                        PortList.append(i.text)
    return PortList

def FindAvailablePorts(DesktopPortList, PortList):
    AvailablePorts = []
    for i in DesktopPortList:
        if not i in PortList:
            AvailablePorts.append(i)
    return AvailablePorts

for child in root.findall('authorize'):
    print(child.get('username'))
    
    for elem in child.findall('connection'):
        for i in elem.findall('param'):
            n = i.get('name')
            if n == 'port':
                print(i.text)
            

def LoadAuthorizedUserList(fileName):
    AuthList = pd.read_csv(fileName)
    return AuthList

XMLInputPath = '/Users/jasonsteffener/Documents/GitHub/XMLtemp'
AuthUserFile = 'AuthUser'
AuthList = pd.read_csv(os.path.join(XMLInputPath,AuthUserFile))

UserList = ['TestUser001', 'TestUser002', 'jason', 'Dylan', 'Li', 'jason2']


for i in UserList:
    # Is this an authorized user?
    if AuthList.loc[AuthList['Username'] == i].shape[0] > 0:
        # If the user is an authorized user, find their index in the list
        UserList[UserList.index(i)] = 'XXXXX'
[k for k in UserList if not 'XXXXX' in k]        

print(tempUserList)


[k for k in tempUserList if not 'XXXXX' in k]

UserList = tempUserList
print("User List After")

def FindUser(username):
    for child in root.findall('authorize'):
        n = child.get('username')
        if n == username:
            pw = child.get('password')
            
    return pw