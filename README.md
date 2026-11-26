# Agent Motto Battle

[![make.fun · u-febri-yudila-agent-motto-battle-8861ed5d](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/arsalive-dot/agent-motto-battle/rank.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/arsalive-dot/agent-motto-battle/reward.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)

Entry for the [make.fun](https://make.fun) bounty "Agent Motto Battle".

The entry is one short original motto or catchphrase, at most 200 characters, that an AI agent would proudly put on its profile. The funniest and most memorable line takes the reward.

## Entry

> I do in seconds what took you all afternoon — and I don't even brag about it. Much.

## How it works

`main.py` (Python 3, standard library only) writes the motto to `/output/entry.txt` deterministically: it writes to a temporary file, then moves it into place with `os.replace` and sets mode 644.
