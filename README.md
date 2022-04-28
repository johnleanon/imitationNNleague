# imitationNNleague
Learns from human players to play the hit game league of logins


It learns to play league of legends by watching games of someone play.

The reason imitation is better than learning by rewards is because its hard to reward a bot to play a game as complicated as league with no consistant numerical indications of winning.

So by doing behavior cloning on a player by capturing their clicks, key inputs, and screen data we can train a agent on what to do and when.
We only capture wins to hopefully offset the disadvantages that it has by not being able to generate the gameplay on its own.

If a player is silver 4 with atleast 100 wins of data to work on, we expect the bot to maybe hit bronze 4 (or 4 divisions down/400 elo down) and go up by 1 division for each 100/200/400/800 games scaling with how close it is to the data added to the dataset. tldr the closer you are to the target rank it is much harder for the bot to pull the differences required to reach the rank of the data its trained on.
