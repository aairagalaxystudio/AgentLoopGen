class AgentState:
    """
    Holds state for a single agent run.
    """

    def __init__(self, goal: str):
        self.goal = goal
        self.plan = []
        self.results = []
        self.completed = False
