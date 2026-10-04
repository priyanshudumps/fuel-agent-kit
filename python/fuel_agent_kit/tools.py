from typing import Callable, Any

class Tool:
    def __init__(self, name: str, description: str, func: Callable):
        self.name = name
        self.description = description
        self.func = func

    def __call__(self, *args, **kwargs) -> Any:
        return self.func(*args, **kwargs)
