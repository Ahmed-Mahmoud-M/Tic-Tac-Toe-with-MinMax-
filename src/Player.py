from Agent import Agent
class Player:
    def __init__(self,symol:str,isAgent=False):
        self.symbol= symol
        
        if isAgent:
            self.agent = Agent() # to get functionality of the agent

    

    def makemove(self):
        pass
