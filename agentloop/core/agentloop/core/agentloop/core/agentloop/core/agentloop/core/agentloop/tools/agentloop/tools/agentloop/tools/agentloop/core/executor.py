class Executor:
    """
    Executes steps and uses tools when required.
    """

    def __init__(self, tools):
        self.tools = tools

    def execute(self, state):
        for step in state.plan:
            if "calculate" in step.lower():
                tool = self.tools.get("calculator")
                result = tool.run(step.replace("calculate", "").strip())
            else:
                result = f"Executed step: {step}"

            state.results.append(result)

        return state
