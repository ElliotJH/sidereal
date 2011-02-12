"""The code for the basic display, I guess."""

# The basic unit for the graphics in Panda3d is ShowBase, which contains
# the render tree, and the task manager and so on.

# As such, our class needs a reference to it, to do ANYTHING.

import panda3d.core
import direct.gui.DirectGui

class LoadingScreen(object):
    def __init__(self,showbase):
        self.base = showbase
        self.background()

        self.lights()
        self.camera()
        self.teapot()
        self.onscreen_text()
        self.action()

    def teapot(self):
        # load the model, and attach it to the render tree
        self.teapot = self.base.loader.loadModel('models/teapot')
        self.teapot.reparentTo(self.base.render)
        self.teapot.setPos(0,-20,-10)

        self.teapot_movement = self.teapot.hprInterval(50,(0,360,360))
        self.teapot_movement.loop()
        self.teapot.setColor(1,0,0,1)
    def background(self):
        self.base.setBackgroundColor(0,0,0,1)
    def onscreen_text(self):
        # ugh, indenting to ensure <80 chars
        self.text = direct.gui.DirectGui.OnscreenText("BOOM",
                                      style=1,
                                      fg=(1,1,1,1),
                                      mayChange=1,
                                      pos=(-1.3,0.80),
                                      align=panda3d.core.TextNode.ALeft,
                                      scale = 0.05,
                                      shadow=(0,0,0,1),
                                      shadowOffset=(0.1,0.1)
                                                     )

    def lights(self):
        # make our directional lightnode, and attach it to the render tree
        dlightnode = panda3d.core.DirectionalLight('light')
        dlightnode.setColor((0.8,0.7,0.6,1))
        dlight = self.base.render.attachNewNode(dlightnode)
        # by setting dlight to light "render", it also lights all nodes
        # attached to render's subtree, as in, everything
        self.base.render.setLight(dlight)

        # same for ambient light
        alightnode = panda3d.core.AmbientLight('ambient')
        alightnode.setColor((0.2,0.2,0.2,1))
        alight = self.base.render.attachNewNode(alightnode)
        self.base.render.setLight(alight)
    def camera(self):
        self.base.camLens.setNearFar(1.0,10000)
        self.base.camLens.setFov(75)
        self.base.disableMouse()
    def action(self):
        pass

if __name__=='__main__':
    # This is mostly debugging test stuff, and will not be run when
    # this is called on as a module.
    import direct.showbase.ShowBase
    s = direct.showbase.ShowBase.ShowBase()
    loadingscreen = LoadingScreen(s)
    s.run()
