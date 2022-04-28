import gym
import numpy as np
import matplotlib.pyplot as plt
from gym.envs.registration import registe
import readchar

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

arrow_keys={
    '\x1b[A':UP,
    '\x1b[B':DOWN,
    '\x1b[C':RIGHT,
    '\x1b[D':LEFT
}

register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLake'
)