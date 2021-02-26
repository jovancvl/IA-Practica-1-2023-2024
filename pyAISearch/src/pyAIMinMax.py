'''
Created on 25 Feb 2021

@author: Francisco Dominguez
'''
from pyAISearchSolver import AISearchSolver

class AIMinMax(AISearchSolver):
    def __init__(self, problem):
        super(AISearchSolver).__init__(problem)
        self.maxUpToNow=-10e100
        self.minUpToNow= 10e100
    def maxValue(self,state):
        if state.isTerminal():
            return state.utility()
        succesors=self.problem.expand(state)
        for s in succesors:
            self.maxUpToNow=max(self.maxUpToNow,self.minValue(s))
        return self.maxUpToNow
    def minValue(self,state):
        if state.isTerminal():
            return state.utility()
        succesors=self.problem.expand(state)
        for s in succesors:
            self.minUpToNow=min(self.minUpToNow,self.maxValue(s))
        return self.minUpToNow