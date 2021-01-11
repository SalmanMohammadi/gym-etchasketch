from gym.envs.registration import register

register(
    id='etchasketch-v0',
    entry_point='etchasketch.envs:EtchASketchEnv',
)
