'''
Created on 7 Mar 2021

@author: Francisco Dominguez
'''
from pyAISearchProblem.pyPathPlanning import PathPlanning,PathPlanningState
from pyAISearchSolverGraph import AISearchSolverGraph
if __name__ == '__main__':
    pps=PathPlanningState()
    pp=PathPlanning()
    sg=AISearchSolverGraph(pp)
    found=sg.search()
    if not found:
        print("Solution not found")
    else:
        print("The solution is,....")
    print(pps)