from __future__ import annotations


from cogs._types import t_rewards, t_reward, RewardShard
from discord import Button, Interaction
from db.api import get_temp_dat, create_temp_dat
from typing import Optional
from discord import ui
from uuid import uuid4


class GenericReward(Button):
    def __init__(self, type_: t_reward, uuid: str) -> None:
        super().__init__(label="???")
        self.uuid = uuid

    async def callback(self: GenericReward, ctx: Interaction) -> None:
        if get_temp_dat("temp-rewards")


class ChoseReward(ui.View):
    def __init__(self, rewards: t_rewards, *, timeout: Optional[float] = 180) -> None:
        super().__init__(timeout=timeout)
        uuid: str = uuid4()
        for rew in rewards:
            self.add_item(GenericReward(rew, uuid=uuid))
