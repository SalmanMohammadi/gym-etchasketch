import gym
import sys
from gym import error, spaces, utils, logger
from gym.utils import seeding


class EtchASketchEnv(gym.Env):
    """
    Description:
        A pole is attached by an un-actuated joint to a cart, which moves along
        a frictionless track. The pendulum starts upright, and the goal is to
        prevent it from falling over by increasing and reducing the cart's
        velocity. 
        
    Source:
        This environment corresponds to the version of the cart-pole problem
        described by Barto, Sutton, and Anderson

    Observation:
        Type: Box(NxN)
        
        The black-and-white pixel values of the NxN pixel screen.


    Actions:
        Type: Discrete (4)
        Box[0] rotates the left controller left
        Box[1] rotates the left controller right
        Box[2] rotates the right controller left
        Box[3] rotates the right controller right

        Box[i] == Box[j] means no movement for i,j in [(0,1), (2, 3)]

    Reward:
        Reward is 1 for every step taken, including the termination step
        Starting State:
        All observations are assigned a uniform random value in [-0.05..0.05]

    Episode Termination:
        Pole Angle is more than 12 degrees.
        Cart Position is more than 2.4 (center of the cart reaches the edge of
        the display).
        Episode length is greater than 200.

    Solved Requirements:
        Considered solved when the average return is greater than or equal to
        195.0 over 100 consecutive trials.
    """
    metadata = {'render.modes': ['human']}

    def __init__(self, image_shape):
      self.observation_space = spaces.Box(low=0, high=1, shape=image_shape)
      self.action_space = spaces.Box(low=0, high=1, shape=(2,))
    def step(self, action):
        ...
    def reset(self):
        ...
        
    def render(self, mode='human'):
        ...
    def close(self):
        ...