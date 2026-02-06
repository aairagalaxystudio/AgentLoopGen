from agentloop.ml.intent import IntentModel  def main():
    tools = ToolRegistry()
    tools.register(CalculatorTool())

    intent_model = IntentModel()

    loop = AgentLoop(
        planner=Planner(),
        executor=Executor(tools, intent_model),
        critic=Critic(),
    )

    result = loop.run("Calculate 12 * 8 and explain result")

    print("Completed:", result.completed)
    print("Plan:", result.plan)
    print("Results:", result.results)      
