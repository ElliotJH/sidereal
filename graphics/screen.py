"""The code for the basic display, I guess."""

# The basic unit for the graphics in Panda3d is ShowBase, which contains
# the render tree, and the task manager and so on.

# As such, our class needs a reference to it, to do ANYTHING.

class LoadingScreen(object):
    def __init__(self,showbase):
        self.sb = showbase

