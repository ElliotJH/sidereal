"""The universe in sidereal is the game space, it is the space
in which all ingame object occupy. It should keep track of all in-game
related objects, such as ships, explosions, projectiles, and so on, or be
able to keep track of them on demand."""

__all__ = ["Universe","foo","bar"]

class Universe(object):
    def __init__(self):
        pass
    def foo(self):
        pass
    def bar(self):
        pass

# inspired by python's random module, create one instance, and export its
# functions as module-level functions. The user can create their own
# Universe() instance if they like
_inst = Universe()
foo = _inst.foo
bar = _inst.bar
