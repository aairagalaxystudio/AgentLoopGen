from agentloop.core.planner import Planner
from agentloop.core.executor import Executor
from agentloop.core.critic import Critic
from agentloop.core.loop import AgentLoop


def main():
    loop = AgentLoop(
        planner=Planner(),
        executor=Executor(),
        critic=Critic(),
    )

    result = loop.run("Test AgentLoop")

    print("Completed:", result.completed)
    print("Plan:", result.plan)
    print("Results:", result.results)


if __name__ == "__main__":
    main()
