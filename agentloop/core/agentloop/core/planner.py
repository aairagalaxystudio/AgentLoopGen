class Planner:
    """
    Breaks a goal into steps.
    """

    def plan(self, state):
        # Temporary static plan (LLM comes later)
        state.plan = [
            "Understand the goal",
            "Execute the task",
            "Verify the result",
        ]
        return state
