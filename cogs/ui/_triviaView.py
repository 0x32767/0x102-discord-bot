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

from cogs.ui._choseReward import ChoseReward
from random import shuffle as shuffle_list
from discord import SelectOption, Embed
from discord.ui import View, Select
from discord import Interaction
from typing import TypeVar

T = TypeVar("T")


class TriviaQuestionDropdown(Select):
    def __init__(
        self: "TriviaQuestionDropdown",
        question: str,
        answers: list[str],
        correct: str,
    ) -> None:
        self.correct: str = correct
        super().__init__(
            max_values=1,
            min_values=1,
            options=[SelectOption(label=f"{i}", value=f"{i}", description=i) for i in self.shuffle(answers)],
            placeholder=question,
        )

    def shuffle(self: "TriviaQuestionDropdown", arr: list[T]) -> list[T]:
        shuffle_list(arr)
        return arr

    async def callback(self: "TriviaQuestionDropdown", ctx: Interaction) -> None:
        if self.correct == self.values[0]:
            await ctx.response.send_message(
                embed=Embed(
                    title="Correct!",
                    description=f"{self.correct} is correct!",
                    color=0x00FF00,  # Hex code for green
                ).add_field(
                    name="Chose what you want",
                    value="Chose betweene a random item or some coins",
                ),
                view=ChoseReward(choices=["random_coins"]),
            )
        else:
            await ctx.response.send_message(
                embed=Embed(
                    title="Incorrect!",
                    description=f"The correct answer was {self.correct}",
                    color=0xFF0000,  # hex code for red
                )
            )


class TriviaView(View):
    def __init__(self: "TriviaView", data: dict) -> None:
        super().__init__()
        self.add_item(
            TriviaQuestionDropdown(
                question=data["question"].replace("&quot;", '"'),
                answers=data["incorrect_answers"] + [data["correct_answer"]],
                correct=data["correct_answer"],
            )
        )
