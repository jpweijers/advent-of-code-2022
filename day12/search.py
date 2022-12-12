from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[T]) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent

    def __lt__(self, other: T) -> bool:
        pass


def dfs(initial, goal_test, move_options):
    frontier = Stack()
    frontier.push(Node(initial, None))
    explored = {initial}

    while not frontier.empty:
        # print(frontier)
        current_node = frontier.pop()
        current_state = current_node.state

        if goal_test(current_state):
            print("Goal found!")
            return current_node

        explored.add(current_state)

        print(move_options(current_state))
        for state in move_options(current_state):
            if state in explored:
                continue
            frontier.push(Node(state, current_node))

    return None

def node_to_path(node: Node[T]) -> List[T]:
    path: List[T] = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path