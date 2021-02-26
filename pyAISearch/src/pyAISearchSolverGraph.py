'''
Created on 21 Feb 2021

@author: Francisco Dominguez
'''
from pyAISearchSolver import AISearchSolver
from pyAISearchCollections.pyAISearchCollection import AISearchCollection
from pyAISearchNode import AISearchNode

class AISearchSolverGraph(AISearchSolver):
    def __init__(self, problem):
        super(AISearchSolver).__init__(problem)
        self.frontier=AISearchCollection()
        self.explored=set()
    def expandIfNotIn(self,currentNode):
        currentState=currentNode.getState()
        for action,state,cost in self.problem.sucessors(currentState):        
            node=AISearchNode()
            node.setState(state)
            node.setFather(currentNode)
            node.setAction(action)
            node.setCostPath(currentNode.getCostPath()+cost)
            node.setDepth(currentNode.getDepth()+1)
            if self.frontier.contains(node) or node in self.explored:
                continue
            self.frontier.insert(node)
    def search(self):
        self.frontier.insert(self.problem.getStateInit())
        while self.frontier.isEmpty():
            currentNode=self.frontier.selectNode()
            currentState=currentNode.getState()
            if self.problem.isGoal(currentState):
                return True
            self.explored.add(currentNode)
            self.expandIfNotIn(currentNode)
        return False
