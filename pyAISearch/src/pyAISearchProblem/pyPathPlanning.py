'''
Created on 7 Mar 2021

@author: Francisco Dominguez
'''
import numpy as np
from pyProblem import AISearchProblem

class PathPlanningState():
    def __init__(self):
        self.map=np.array([
            [0,0,1,0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0,0],
            [0,0,1,0,1,1,1,0,0,0],
            [0,0,1,0,0,0,1,0,0,0],
            [0,0,1,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,1,0,0,0],
            [0,0,0,1,1,1,1,0,0,0]
            ]) 
        self.location=(0,0)
    def setLocation(self,l): self.location=l
    def getLocation(self): return self.location
    def getLocationX(self): return self.location[0]
    def getLocationY(self): return self.location[1]
    def __str__(self):
        s=" 0123456789\n"
        for row in range(self.map.shape[0]):
            s+=str(row)
            for col in range(self.map.shape[1]):
                if (col,row)==self.location:
                    s+="@"
                    continue
                if self.map[row,col]==0:
                    s+=" "
                if self.map[row,col]==1:
                    s+="#"
            s+="\n"
        return s
        
class PathPlanning(AISearchProblem):
    '''
    Find a path from origin to target location
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
        self.state=PathPlanningState()
        self.origin=(0,0)
        self.target=(9,9)
        self.state.setLocation(self.origin)
        self.actions=["U","D","L","R"]
    def canTakeAction(self,a,state):
        if a=="U":
            if state.getLocationY()==0:
                return False
            newLocation=(state.getLocationX(),state.getLocationY()-1)
            if state.notWall(newLocation):
                return True
        if a=="D":
            if state.getLocationY()==state.map.shape[0]:
                return False
            newLocation=(state.getLocationX(),state.getLocationY()+1)
            if state.notWall(newLocation):
                return True
        if a=="L":
            if state.getLocationX()==0:
                return False
            newLocation=(state.getLocationX(),state.getLocationX()-1)
            if state.notWall(newLocation):
                return True
        if a=="R":
            if state.getLocationX()==state.map.shape[1]:
                return False
            newLocation=(state.getLocationX(),state.getLocationX()+1)
            if state.notWall(newLocation):
                return True
        return False
    #return a collection of action,state,cost
    def successosrs(self,state):
        sucessors=[]
        for a in self.actions:
            if self.canTakeAction(a,state):
                newState=state.walk(a)
                sucessors.apend(newState,a,1)
        return sucessors
    def isGoal(self,state):
        return state.getLocation()==self.target
  