class Tool:
    """
    Base class for all tools.
    """

    name = "tool"
    description = ""

    def run(self, input: str) -> str:
        raise NotImplementedError("Tool must implement run()")
