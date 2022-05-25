from abc import ABC, abstractmethod

class Component(ABC):
  @property
  def parent(self) -> Component:
    return self._parent

  @parent.setter
  def parent(self, parent: Component):
    self._parent = parent

  def add(self, component: Component) -> None:
    pass

  def remove(self, component: Component) -> None:
    pass

  def is_composite(self) -> bool:
    return False

  @abstractmethod
  def operation(Self) -> str:
    pass

class Leaf(Component):
  def operation(Self) -> str:
      return "Leaf"
