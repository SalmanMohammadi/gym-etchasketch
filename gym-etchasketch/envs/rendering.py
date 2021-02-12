import os
import sys
from gym import error
import pyglet
from typing import Tuple
import numpy as np


try:
    import pyglet
except ImportError as e:
    raise ImportError('''
    Cannot import pyglet.
    HINT: you can install pyglet directly via 'pip install pyglet'.
    But if you really just want to install all Gym dependencies and not have to think about it,
    'pip install -e .[all]' or 'pip install gym[all]' will do it.
    ''')

try:
    from pyglet.gl import *
except ImportError as e:
    raise ImportError('''
    Error occurred while running `from pyglet.gl import *`
    HINT: make sure you have OpenGL install. On Ubuntu, you can run 'apt-get install python-opengl'.
    If you're running on a server, you may need a virtual frame buffer; something like this should work:
    'xvfb-run -s \"-screen 0 1400x900x24\" python <your_script.py>'
    ''')


# inspired by https://github.com/openai/gym/blob/8a721ace460cbaf8c3e6c03c12d06c616fd6e1e8/gym/envs/classic_control/rendering.py#L335
class BlackAndWhiteImageViewer(object):
    def __init__(self, shape: Tuple[int, int]):
        self.height, self.width = shape
        self.is_open = False
        self.display = pyglet.canvas.get_display()
        self.window = None

    def imshow(self, arr: np.ndarray):
        if self.window is None:
            config = self.display.get_screens()[0].get_best_config()
            context = config.create_context(None)
            height, width, *_ = arr.shape
            self.window = pyglet.window.Window(
                width=width, height=height, display=self.display, config=config, vsync=False, resizable=True, context=context)
            self.is_open = True

            @self.window.event
            def on_resize(width, height):
                self.width = width
                self.height = height

            @self.window.event
            def on_close():
                self.is_open = False
                self.window.close()

        image = pyglet.image.ImageData(
            arr.shape[1], arr.shape[0], "L", arr.tobytes(), pitch=arr.shape[1]*-1)
        gl.glTexParameteri(gl.GL_TEXTURE_1D,
                           gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
        texture = image.get_texture()
        texture.width = self.width
        texture.height = self.height
        self.window.clear()
        self.window.switch_to()
        self.window.dispatch_events()
        texture.blit(0, 0)
        self.window.flip()

    def close(self):
        if self.is_open and sys.meta_path:
            # ^^^ check sys.meta_path to avoid 'ImportError: sys.meta_path is None, Python is likely shutting down'
            self.window.close()
            self.is_open = False

    def __del__(self):
        self.close()
