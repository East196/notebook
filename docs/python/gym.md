# OpenAI gym入门

## OpenAI gym是什么？

OpenAI gym 是一个增强学习算法的测试环境集合。可以用来快速验证你的算法。

## 增强学习（Reinforcement Learning，RL）

![增强学习原理图](http://img.blog.csdn.net/20171220175514610?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZWFzdDE5Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

- **agent**：智能体，也就是机器人，你的代码本身。

- **environment**：环境，也就是游戏本身，openai gym提供了多款游戏，也就是提供了多个环境。

- **action**：行动，比如玩超级玛丽，向上向下等动作。

- **state**：状态，每次智能体做出行动，环境会相应地做出反应，返回一个状态和奖励。

- **reward**：奖励：根据游戏规则的得分。智能体不知道怎么才能得分，它通过不断地尝试来理解游戏规则，比如它在这个状态做出向上的动作，得分，那么下一次它处于这个环境状态，就倾向于做出向上的动作。

## 安装
使用pip安装gym：

`pip install gym`

## 第一个例子：CartPole

运行 [CartPole](https://gym.openai.com/envs/CartPole-v0) 的环境来验证安装成功：
```python
import gym
env = gym.make('CartPole-v0') # 环境导入
env.reset()
for _ in range(1000):
    env.render()
    action = env.action_space.sample() # 随便动一动~~~
	env.step(action)
```

## 接口分析

gym用env作为环境接口。env包含下面几个核心方法：

- **`reset(self)`**: 重置环境的状态，返回观察。

- **`step(self, action)`**: 推进一个时间步长，返回observation，reward，done，info

- **`render(self, mode=’human’, close=False)`**: 重绘环境的一帧。默认模式一般比较友好，如弹出一个窗口
