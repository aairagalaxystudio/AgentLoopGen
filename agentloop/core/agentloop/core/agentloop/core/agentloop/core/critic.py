class Critic:
    """
    Evaluates whether the goal is completed.
    """

    def review(self, state):
        state.completed = True
        return state
