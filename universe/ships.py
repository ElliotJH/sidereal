import json
import io


# This is the example configuration for an example ship
# Most of these stats may or may not make any sense as we work
# on the physics system. But it should indicate the vague feel of it
_exampleconfiguration = {
    "classname":"Striker",
    "race":["foobeings","barbeings"],
    "mass":5000,
    "engines":[
        {"placement":(10,-50,0),
         "thrust":2000,
         "warmuptime":10,
        },
        {"placement":(-10,-50,0),
         "thrust":2000,
         "warmuptime":10,
        }
    ],
    "guns":[
        {"type":"massdriver",
         "mass":5,
         "damage":50
        }
    ],
}
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
