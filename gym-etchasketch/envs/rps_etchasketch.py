import gym
import sys
import numpy as np
from gym import error, spaces, utils, logger
from gym.utils import seeding
import scipy.misc as smp


class EtchASketchEnv(gym.Env):
    """
    Description:
        # https://openaccess.thecvf.com/content_ICCV_2019/papers/Huang_Learning_to_Paint_With_Model-Based_Deep_Reinforcement_Learning_ICCV_2019_paper.pdf
        # is quite relevant
    Source:

    Observation:
        Type: Box(NxN)

        The black-and-white pixel values of the NxN pixel screen.


    Actions:
        Move
        Type: Box (2)
        Box[0] rotates the left knob [-1, 1] -> [-2PI, 2PI], moving the cursor sin(x)
        Box[1] rotates the right knob[-1, 1] -> [-2PI, 2PI], moving the cursor cos(x)
        Reset
        Type: Discrete(1)
        Num
        0   Don't reset the state
        1   Reset the state

    Reward:

        The reward will be given at the end of an episode (sparse) as the negative log bernoulli likelihood 
        between the pixel values of the target image and the current environment.

    Episode Termination:
        Episode length is greater than __.

    Solved Requirements:

    """
    metadata = {'render.modes': ['human', 'array']}

    def __init__(self, shape: (int, int)):
        self.shape = shape
        self.action_space = spaces.Dict(
            {"cursor": spaces.Box(low=np.array(
                [-1.0, 1.0]), high=np.array([-1.0, 1.0]), dtype=np.float32),
                "reset": spaces.Discrete(2)
             })
        self.observation_space = spaces.Box(low=0, high=1, shape=image_shape)

        self.viewer = None

        self.cursor = (shape[0] // 2, shape[1] // 2)
        self.state = np.zeros((image_shape), dtype=np.uint8)
        self.state[self.cursor] = 255

        self.seed()
        self.reset()

    def step(self, action: spaces.Dict):
        pass

    def reset(self) -> spaces.Box:
        self.state = np.zeros((self.shape), dtype=np.uint8)
        self.cursor = (self.shape[0] // 2, self.shape[1] // 2)
        self.state[self.cursor] = 255
        return self.state

    def seed(self, seed: int = None) -> [int]:
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        pass

    def render(self, mode='human') -> bool:
        if mode == 'array':
            return self.state
        elif mode == 'human':
            from rendering import BlackAndWhiteImageViewer
            if self.viewer is None:
                self.viewer = BlackAndWhiteImageViewer(self.shape)
            self.viewer.imshow(self.state)
            return self.viewer.is_open

    def close(self):
        if self.viewer is not None:
            self.viewer.close()
            self.viewer = None


if __name__ == "__main__":
    image_shape = (512, 512)
    env = EtchASketchEnv(image_shape)

    while True:
        env.render()
