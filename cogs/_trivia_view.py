from random import shuffle
from discord import Interaction
from discord.ui import (
    View,
    Select,
)
from discord import SelectOption, Embed


class TriviaQuestionDropdown(Select):
    def __init__(self, question: str, questions: list[str], correct: str) -> None:
        """
         | this constructs a dropdown of the question
         | as the placeholder and the answers as the
         | options.
        """
        self.correct = correct
        super().__init__(
            max_values=1,
            min_values=1,
            options=[
                SelectOption(label=f'{i}', value=f'{i}', description=i) for idx, i in enumerate(self.shuffle(questions))
            ],
            placeholder=question
        )

    def shuffle(self, arr: list) -> list:
        self.pass_()
        shuffle(arr)
        return arr

    async def callback(self, ctx: Interaction) -> None:
        """
         | This is the callback function
         | that is called when the user
         | selects an option.
        """
        if self.correct == self.values[0]:
            await ctx.response.send_message(
                embed=Embed(
                    title='Correct!',
                    description=f'{self.correct} is correct!',
                    color=0x00ff00
                )
            )
        else:
            await ctx.response.send_message(
                embed=Embed(
                    title='Incorrect!',
                    description=f'The correct answer was {self.correct}',
                    color=0xFF0000
                )
            )

    def pass_(self) -> None:
        ...


class TriviaView(View):
    def __init__(self, data: dict) -> None:
        super().__init__()
        self.add_item(
            TriviaQuestionDropdown(
                question=data['question'].replace('&quot;', '"'),
                questions=data['incorrect_answers'] + [data['correct_answer']],
                correct=data['correct_answer']
            )
        )
