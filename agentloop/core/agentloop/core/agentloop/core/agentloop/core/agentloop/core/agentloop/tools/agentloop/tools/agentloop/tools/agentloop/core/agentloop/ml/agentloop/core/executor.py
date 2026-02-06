class Executor:
    """
    Executes steps using ML-based intent decisions.
    """

    def __init__(self, tools, intent_model):
        self.tools = tools
        self.intent_model = intent_model

    def execute(self, state):
        for step in state.plan:
            intent = self.intent_model.predict([step])[0]

            if intent == "math":
                tool = self.tools.get("calculator")
                result = tool.run(step.replace("calculate", "").strip())

            elif intent == "simple":
                result = f"Handled simple step: {step}"

            else:
                # Reasoning placeholder (LLM comes later)
                result = f"Reasoning required for: {step}"

            state.results.append(result)

        return state
