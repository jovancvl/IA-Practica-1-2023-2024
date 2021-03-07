'''
Created on 14 Feb 2021

@author: Francisco Dominguez
'''
class AISearchNode(object):
    def __init__(self,state=None,father=None,action=None,cost=1):
        self.state=state
        self.father=father
        self.action=action
        self.costPath=0
        self.depth=0
        if father!=None: 
            self.costPath=father.getCostPath()+cost
            self.depth=father.getDepth()+1
    def setState(self,s):    self.state=s
    def setFather(self,f):   self.father=f
    def setActoin(self,a):   self.action=a
    def setCostPath(self,c): self.costPath=c
    def setDepth(self,d):    self.depth=d
    def getState(self):    return self.state
    def getFather(self):   return self.father
    def getAction(self):   return self.action
    def getCostPath(self): return self.costPath
    def getDepth(self):    return self.depth