"""
 | This file is the lua ctx module. The reason why we use a
 | separate class (with only one method) is because we don't
 | want one user to destroy stuff including the server, by
 | deleting all channels, roles, etc.
 |
 | This module is not with the other module that contains the
 | executer, because we want to be able to expand upon the
 | `luaCtx` module, and add new features.
"""

from discord import Interaction


class luaCtx:
    def __init__(self, interaction: Interaction) -> None:
        self.reply = interaction.response.send_message
