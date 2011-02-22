import ConfigParser as configparser
# Renamed to that in Python3, may as well start now

import io


# This is the example configuration for an example ship
# Most of these stats may or may not make any sense as we work
# on the physics system. But it should indicate the vague feel of it
exampleconfig = """
[coreship]
classname = Striker
race = foobar
mass = 5000
engines = engine1,engine2
guns = gun1,

[engine1]
placement = (10,-50,0)
thrust = 2000
warmuptime = 10

[engine2]
placement = (-10,-50,0)
thrust = 2000
warmuptime = 10

[gun1]
type = massdriver
mass = 5
damage = 50
"""

class Ship(object):
    """The basic core ship class in Sidereal."""
    def __init__(self):
        pass

    @classmethod
    def create_from_config(cls, config):
        """Given a configparser that has already read a ship configuration
        file, builds a new Ship object, and returns it."""
        pass

if __name__=='__main__':
    pass
