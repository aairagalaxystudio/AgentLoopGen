from agentloop.core.state import AgentState


class AgentLoop:
    """
    Controls planner → executor → critic.
    """

    def __init__(self, planner, executor, critic):
        self.planner = planner
        self.executor = executor
        self.critic = critic

    def run(self, goal: str):
        state = AgentState(goal)
        state = self.planner.plan(state)
        state = self.executor.execute(state)
        state = self.critic.review(state)
        return state
