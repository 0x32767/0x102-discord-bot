from random import shuffle as shuffle_list
from discord import Interaction
from discord import SelectOption, Embed
from discord.ui import (
    View,
    Select,
)


class TriviaQuestionDropdown(Select):
    def __init__(
        self: "TriviaQuestionDropdown",
        question: str,
        questions: list[str],
        correct: str,
    ) -> None:
        """
        | this constructs a dropdown of the question
        | as the placeholder and the answers as the
        | options.
        """
        self.correct: str = correct
        super().__init__(
            max_values=1,
            min_values=1,
            options=[
                SelectOption(label=f"{i}", value=f"{i}", description=i)
                for i in self.shuffle(questions)
            ],
            placeholder=question,
        )

    def shuffle(self: "TriviaQuestionDropdown", arr: list[str]) -> list[str]:
        self.pass_()
        shuffle_list(arr)
        return arr

    async def callback(self: "TriviaQuestionDropdown", ctx: Interaction) -> None:
        """
        | This is the callback function
        | that is called when the user
        | selects an option.
        """
        if self.correct == self.values[0]:
            await ctx.response.send_message(
                embed=Embed(
                    title="Correct!",
                    description=f"{self.correct} is correct!",
                    color=0x00FF00,
                )
            )
        else:
            await ctx.response.send_message(
                embed=Embed(
                    title="Incorrect!",
                    description=f"The correct answer was {self.correct}",
                    color=0xFF0000,
                )
            )

    def pass_(self: "TriviaQuestionDropdown") -> None:
        ...


class TriviaView(View):
    def __init__(self: "TriviaView", data: dict) -> None:
        super().__init__()
        self.add_item(
            TriviaQuestionDropdown(
                question=data["question"].replace("&quot;", '"'),
                questions=data["incorrect_answers"] + [data["correct_answer"]],
                correct=data["correct_answer"],
            )
        )
