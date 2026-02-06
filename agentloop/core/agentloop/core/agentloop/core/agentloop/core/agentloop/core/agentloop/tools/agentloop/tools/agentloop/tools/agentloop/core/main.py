from agentloop.core.planner import Planner
from agentloop.core.executor import Executor
from agentloop.core.critic import Critic
from agentloop.core.loop import AgentLoop
from agentloop.tools.registry import ToolRegistry
from agentloop.tools.calculator import CalculatorTool


def main():
    tools = ToolRegistry()
    tools.register(CalculatorTool())

    loop = AgentLoop(
        planner=Planner(),
        executor=Executor(tools),
        critic=Critic(),
    )

    result = loop.run("Calculate 12 * 8")

    print("Completed:", result.completed)
    print("Plan:", result.plan)
    print("Results:", result.results)


if __name__ == "__main__":
    main()
