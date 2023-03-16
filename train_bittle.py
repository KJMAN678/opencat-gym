import time

import pybullet as p
from opencat_gym_env_bittle import OpenCatGymEnv
from stable_baselines3 import A2C, PPO, SAC, TD3
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.env_util import make_vec_env

# Create OpenCatGym environment from class
env = OpenCatGymEnv()
check_env(env)

# Training
# env = make_vec_env(lambda: env, n_envs=25) # only for PPO
model = SAC(
    "MlpPolicy",
    env,
    learning_starts=0,
    use_sde=False,
    use_sde_at_warmup=False,
    verbose=1,
    tensorboard_log="./sac_opencat_tensorboard/",
).learn(4.5e5)

# model.save("sac_opencat_bittle")
# model.save_replay_buffer("sac_opencat_replay_buffer_bittle")

# Load model to continue previous training
# model = SAC.load("sac_opencat_bittle", env, verbose=1, learning_starts = 0, verbose=1, tensorboard_log="./sac_opencat_tensorboard/")
# model.load_replay_buffer("sac_opencat_replay_buffer_bittle")
# model.learn(4.5e5)
