class Executor:
    """
    Executes each planned step.
    """

    def execute(self, state):
        for step in state.plan:
            result = f"Executed step: {step}"
            state.results.append(result)
        return state
