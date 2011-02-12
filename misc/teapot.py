"""The code for the basic display, I guess.

No scrap that, this is pretty hacked together code for showing
a flipping rotating teapot. We should totally include this in the
credits. XD"""

# The basic unit for the graphics in Panda3d is ShowBase, which contains
# the render tree, and the task manager and so on.

# As such, our class needs a reference to it, to do ANYTHING.

import panda3d.core
import direct.task
import direct.gui.DirectGui

import random

class LoadingScreen(object):
    def __init__(self,showbase):
        self.base = showbase
        self.background()

        self.teapot()

        self.lights()
        self.camera()
        self.onscreen_text()
        self.action()

    def teapot(self):
        # load the model, and attach it to the render tree
        self.teapot = self.base.loader.loadModel('models/teapot')
        self.teapot.reparentTo(self.base.render)
        self.teapot.setPos(0,0,0)

        self.teapot_movement = self.teapot.hprInterval(50,(0,360,360))
        self.teapot_movement.loop()
        self.teapot.setColor(1,1,1,1)
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
        dlight = panda3d.core.DirectionalLight('light')
        dlight.setColor((0.2,0.2,0.8,1))
        dlight_nodepath = self.base.render.attachNewNode(dlight)
        # by setting dlight to light "render", it also lights all nodes
        # attached to render's subtree, as in, everything
        self.base.render.setLight(dlight_nodepath)

        # same for ambient light
        alightnode = panda3d.core.AmbientLight('ambient')
        alightnode.setColor((0.2,0.2,0.2,1))
        alight = self.base.render.attachNewNode(alightnode)
        self.base.render.setLight(alight)
        dlight_nodepath.lookAt(self.teapot)
    def camera(self):
        self.base.camLens.setNearFar(1.0,10000)
        self.base.camLens.setFov(75)
        self.base.camera.setPos(0,0,50)
        self.base.camera.setHpr(0,-90,0)
        self.base.disableMouse()
    def randomise_camera(self,task):
        coords = []
        for i in range(3):
            coords.append(random.randint(-50,50))
        print coords
        self.base.camera.setPos(tuple(coords))
        self.base.camera.lookAt(self.teapot)
        return direct.task.Task.again

    def action(self):
        self.base.taskMgr.doMethodLater(0.5,self.randomise_camera,'randomise')

if __name__=='__main__':
    # This is mostly debugging test stuff, and will not be run when
    # this is called on as a module.
    import direct.showbase.ShowBase
    s = direct.showbase.ShowBase.ShowBase()
    loadingscreen = LoadingScreen(s)
    s.run()
