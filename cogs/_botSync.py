"""
Copyright (C) 23/07/2022 - Han P.B Manseck.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from discord import Button, SelectOption, Embed, Interaction
from discord.ui import View, Select
from httpx import AsyncClient


class BotSyncUi(View):
    def __init__(self):
        super().__init__()
        self.add_item(OptionsDropdown())


class OptionsDropdown(Select):
    def __init__(self):
        super().__init__(
            min_values=1,
            min_values=6,
            options=[
                SelectOption(text="Punish spam automatically", value="punish_spam"),
                SelectOption(text="Punish profanity automatically", value="punish_profanity"),
                SelectOption(text="Allow custom commands", value="allow_custom_commands"),
                SelectOption(text="Allow server links", value="allow_server_links"),
                SelectOption(text="Use reputation", value="use_reputation"),
            ],
        )

    async def callback(self, ctx: Interaction) -> None:
        settings: dict[str, tuple[str, str]] = {
            "allow_custom_commands": ("run_cc_enabled", "run_cc_disabled"),
            "allow_server_links": ("allow_links_enabled", "allow_links_disabled"),
            "punish_profanity": ("auto_mod_enabled", "auto_mod_disabled"),
            "punish_spam": ("spam_mod_enabled", "spam_mod_disabled"),
            "use_reputation": ("reputation_enabled", "reputation_disabled"),
        }
        payload: list[str] = []

        for op in self.options:
            if op in self.value:
                payload.append(settings[op.value][0])

            else:
                payload.append(settings[op.value][1])

        async with AsyncClient() as client:
            await client.post("...", json={"settings": payload})

        await ctx.response.send_message(embed=Embed(title="Settings updated", description="Your settings have been updated"))
