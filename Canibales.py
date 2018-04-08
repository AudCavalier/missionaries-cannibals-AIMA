# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 17:33:16 2017
 
@author: Gabriel (AudCavalier)
"""
#Imports from AIMA code
from utils import *;
from search import *;

#Class for the problem
class misioneroscanibales(Problem):
    def __init__(self, initial, goal):
        Problem.__init__(self, initial, goal);
        self.state = initial;
        
    def actions(self, state):
        """
        Actions method, gets a state and returns a list of all possible actions that can be executed
        """
        #DEFINING POSSIBLE ACTIONS ONE BY ONE
        if(state[2]==1): #boat to the right
           if(state[0]==3): #if there are 3 missionaries on the right side
               if(state[1]>=2): 
                   return ['MM', 'M', 'MC', 'C', 'CC'];
               elif(state[1]==1): 
                   return ['MM', 'M', 'MC', 'C'];
               else: 
                   return ['MM', 'M'];
           elif(state[0]==2): #if there are 2 missionaries on the right side and 1 on the left
               if(state[1]==2):
                   return ['MM', 'M', 'MC', 'C', 'CC'];
               else: #Any other state is a dead-state
                   return []; 
           elif(state[0]==1): #if there is 1 missionarie on the right side and 2 on the left
               if(state[1]==1):
                   return ['M', 'MC', 'C'];
               else: #dead-states
                   return []; 
           else: #No missionaries on the right side, 3 on the left side
               if(state[1]>=2): #if there are 2 or 3 cannibals on the right side, 0 or 1 on the left
                   return ['C', 'CC'];
               else: #if there is 1 cannibal on the right, 2 on the left
                   return ['C'];
        if(state[2]==0): #boat to the left
            #The following is the definition, like the previous one, but when boad is on the left
           if(state[0]==3): 
               if(state[1]==2): 
                   return ['C'];
               else: 
                   return ['C', 'CC'];
           elif(state[0]==2):
               if(state[1]==2): 
                   return ['M', 'MC', 'C'];
               else: #dead-state
                   return []; 
           elif(state[0]==1): 
               if(state[1]==1):
                   return ['MM', 'M', 'MC', 'C', 'CC'];
               else: #dead-state
                   return []; 
           else: 
               if(state[1]==3): 
                   return ['M', 'MM'];
               elif(state[1]==2): 
                   return ['M', 'MM', 'MC', 'C'];
               else: 
                   return ['M', 'MM', 'MC', 'CC'];
        else:
            return None;
                 
    def result(self, state, action):
        """
        result method, gets a state and an action and returns a new state result of applaying that action to the given state
        """
        state=list(state)
        if (state[2]==1):
            if action=='M':
                state[0]=state[0]-1;
                state[2]=0;
            elif action=='MM':
                state[0]=state[0]-2;
                state[2]=0
            elif action=='MC':
                state[0]=state[0]-1;
                state[1]=state[1]-1;
                state[2]=0
            elif action=='C':
                state[1]=state[1]-1;
                state[2]=0
            else:
                state[1]=state[1]-2;
                state[2]=0;
        else:
            if action=='M':
                state[0]=state[0]+1;
                state[2]=1
            elif action=='MM':
                state[0]=state[0]+2;
                state[2]=1
            elif action=='MC':
                state[0]=state[0]+1;
                state[1]=state[1]+1;
                state[2]=1
            elif action=='C':
                state[1]=state[1]+1;
                state[2]=1
            else:
                state[1]=state[1]+2;
                state[2]=1
        state=tuple(state)
        self.state=state
        return self.state
      
    def goal_test(self, state):
        """
        goal_test method: checks if current state is goal or not
        """
        if state==self.goal:
            return True;
        else:
            return False;

#Initial state
inicio=[3, 3, 1]
inicio=tuple(inicio)
#Goal state
goal=[0, 0, 0]
goal=tuple(goal)
"""
Now all is left is to instantiate the problem and using the search class from the AIMA
have it explore the solution tree to find the solution to the problem
"""
problemo=misioneroscanibales(inicio, goal)
#using breadth first search
s=breadth_first_search(problemo);
#using tree search
#s=tree_search(problemo, FIFOQueue())
#using breadth first tree search
#s=breadth_first_tree_search(problemo)
#using depth limited search: NOT OPTIMAL
#s=depth_limited_search(problemo)
#print(s.path())
for i in s.path():
    print(i)