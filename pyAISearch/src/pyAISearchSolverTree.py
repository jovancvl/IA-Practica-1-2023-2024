'''
Created on 15 Feb 2021

@author: Francisco Dominguez
'''
from pyAISearchSolver import AISearchSolver
from pyAISearchCollections.pyAISearchCollection import AISearchCollection
from pyAISearchNode import AISearchNode

class AISearchSolverTree(AISearchSolver):
    def __init__(self, problem):
        super(AISearchSolver).__init__(problem)
        self.frontier=AISearchCollection()
    def expand(self,currentNode):
        currentState=currentNode.getState()
        for action,state,cost in self.problem.sucessors(currentState):
            node=AISearchNode()
            node.setState(state)
            node.setFather(currentNode)
            node.setAction(action)
            node.setCostPath(currentNode.getCostPath()+cost)
            node.setDepth(currentNode.getDepth()+1)
            self.frontier.insert(node)
    def search(self):
        self.frontier.insert(self.problem.getStateInit())
        while self.frontier.isEmpty():
            currentNode=self.frontier.selectNode()
            currentState=currentNode.getState()
            if self.problem.isGoal(currentState):
                return True
            self.expand(currentNode)
        return False
    