# from __future__ import annotations
# from abc import ABC, abstractmethod
# from typing import List

# class Component(ABC):
#   @property
#   def parent(self) -> Component:
#     return self._parent

#   @parent.setter
#   def parent(self, parent: Component):
#     self._parent = parent

#   def add(self, component: Component) -> None:
#     pass

#   def remove(self, component: Component) -> None:
#     pass

#   def is_composite(self) -> bool:
#     return False

#   @abstractmethod
#   def operation(self) -> str:
#     pass

# class Leaf(Component):
#   def operation(self) -> str:
#       return "Leaf"

# class Composite(Component):
#   def __init__(self) -> None:
#       self._children: List[Component] = []

#   def add(self, component: Component) -> None:
#       self._children.append(component)
#       component.parent = self

#   def remove(self, component: Component) -> None:
#       self._children.remove(component)
#       component.parent = None

#   def is_composite(self) -> bool:
#       return True

#   def operation(self) -> str:
#       results = []

#       for child in self._children:
#         results.append(child.operation())

#       return results

# def client_code(component: Component) -> None:
#   print(component.operation())

# def client_code_2(component1: Component, component2: Component) -> None:
#   if component1.is_composite():
#     component1.add(component2)

#   print(component1.operation())

# if __name__ == "__main__":
#     simple = Leaf()
#     client_code(simple)
#     print("\n")

#     tree = Composite()

#     branch1 = Composite()
#     branch1.add(Leaf())
#     branch1.add(Leaf())

#     branch2 = Composite()
#     branch2.add(Leaf())

#     tree.add(branch1)
#     tree.add(branch2)

#     print("Client: Now I've got a composite tree:")
#     client_code(tree)
#     print("\n")

#     print("Client: I don't need to check the components classes even when managing the tree:")
#     client_code_2(tree, simple)

from abc import ABCMeta, abstractmethod

class GraphicInterface(metaclass=ABCMeta):
  @staticmethod
  @abstractmethod
  def print():
    pass

class Elipse(GraphicInterface):
  def print(self):
    print("Elipse")

class Circle(GraphicInterface):
  def print(self):
    print("Circle")

class Composite(GraphicInterface):
  def __init__(self) -> None:
    self.components = []

  def add(self, component):
    self.components.append(component)

  def print(self):
    for component in self.components:
      component.print()

COMPOSITE1 = Composite()
ELIPSE1 = Elipse()
CIRCLE1 = Circle()

COMPOSITE1.add(ELIPSE1)
COMPOSITE1.add(CIRCLE1)

ELIPSE2 = Elipse()
COMPOSITE2 = Composite()

# COMPOSITE1.print()

COMPOSITE2.add(COMPOSITE1)
COMPOSITE2.add(ELIPSE2)

COMPOSITE2.print()
