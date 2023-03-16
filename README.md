# OpenCat Gym

A gym reinforcement learning environment for OpenCat robots based on Stable-Baselines3 and PyBullet.

## Nybble version

![](animations/nybble_learning.gif)

## Bittle version

![](animations/bittle_learning.gif)

## Usage

Start training with train_nybble.py or train_bittle.py
To take a look at the pre-trained example, execute enjoy_nybble.py or enjoy_bittle.py.

## Links

For more information on the reinforcement training implementation: https://stable-baselines3.readthedocs.io/en/master/index.html
And for the simulation environment please refer to: https://pybullet.org/wordpress/

```sh
# M1Mac  に Miniforge をインストール (Ventura 13.2.1を使用)
brew install miniforge

# 仮想環境の作成
conda env create --name opencat --file requirements.yaml

# 仮想環境のアクティベート
conda activate opencat

python train_bittle.py
```
