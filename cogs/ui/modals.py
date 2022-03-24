import discord
import traceback


class Feedback(discord.ui.Modal, title='Feedback'):
    name = discord.ui.TextInput(
        label='Name',
        placeholder='Your name here...',
    )

    feedback = discord.ui.TextInput(
        label='What do you think of this new feature?',
        style=discord.TextStyle.long,
        placeholder='Type your feedback here...',
        required=False,
        max_length=300,
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your feedback, {self.name.value}!', ephemeral=True)

    async def on_error(self, error: Exception, interaction: discord.Interaction) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)
        traceback.print_tb(error.__traceback__)


# todo : make a callback
def trivia_question(config: dict) -> discord.ui.Modal:
    class TriviaQuestion(discord.ui.Modal, title=config['question']):
        for ans in config['choices']:
            question = discord.ui.Button(
                label=ans
            )

    return TriviaQuestion()
