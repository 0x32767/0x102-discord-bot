class MaxEmbedFieldsExceeded(Exception):
    """
     | ::context::
     | The discord api does not allow embeds to have over 25 fields.
     |
     | ::use::
     | The exception is raised when a lua table which has more than 25, as of the error being made there is no limit to how
     | many fields can be added to the embed.
     |
     | ::example::
     |
     |  -- btw this embed would have 26 fields
     | function test(cotext)
     |     return createEmbed{title="Field overflow", description="..."}.addField(
     |       ).addField().addField().addField().addField().addField().addField(
     |       ).addField().addField().addField().addField().addField().addField(
     |       ).addField().addField().addField().addField().addField().addField(
     |       ).addField().addField().addField().addField().addField().addField().addField()
     | end
     |
     | ::In-code use::
     | if len(embed["fields"]) >= 26:
     |     return MaxEmbedFieldsExceeded({
     |          "message": f"the maximum amount of embeds has been reached got {len(embed['fields'])} >= 26",
     |          "ErrorUrl": "https://github.com/0x32767/0x102-discord-bot/..."
     | })
    """

    @property
    def embed(self):
        import discord

        return discord.Embed(
            title="Embed Field Overflow",
            description="The maximum amount of embed fields has been reached.",
            color=0xFF0000,
            url=self.args[0]["ErrorUrl"]
        ).add_field(
            name="Error Name",
            value=self.__class__.__name__,
        )


class EmbedInitializeError(Exception):
    """
     | ::context::
     | discord.py requires embeds to created with the following syntax:
     |
     | embed: Embed = Embed(
     |      title=">>INSERT TITLE HERE<<",
     |      description=">>INSERT DESCRIPTION HERE<<",
     |      color=0x00ff00 # this creates a nice matrix gereen
     | )
     |
     | These paramiters are accessed from the embed object created by the user.
     |
     | ::use::
     | The exception is raised when a keyError is thrown (python can not find the identifier), this can be caused if the keys
     | or values in the embed are missing or not of the expected type.
     |
     | ::example::
     | function test()
     |  --               vvvvv (a title was not specified)
     |      return newEmbed{description="..."}
     | end
     |
     | ::in-code use::
     | try:
     |    em: Embed = Embed(
     |          title=embed["name"],
     |          description=embed["description"],
     |          color=embed["color"]
     |      )
     | except KeyError:
     |    return EmbedInitializeError({
     |          "message": "The embed was not initialized correctly",
     |          "ErrorUrl": ""
     | })
    """

    @property
    def embed(self):
        import discord

        return discord.Embed(
            title="Embed Initialization Error",
            description="The embed was not initialized correctly.",
            color=0xFF0000,
            url=self.args[0]["ErrorUrl"]
        ).add_field(
            name="Error Name",
            value=self.__class__.__name__,
        )


class FieldInitializeError(Exception):
    """
     | ::context::
     | discord.py requires three paramiters when initializing an embed field: name, value and inline.
     |
     | ::use::
     | The exception is raised when a keyError is thrown. This can be caused if the key is not found in the lua table.
     | This can also be caused if the value is not of the expected type.
     |
     | ::example::
     | function test()
     |      return newEmbed{title="...", description="..."}.addField(
     |          name="...", -- the value argument is missing
     |          inline=true
     |      )
     | end
     |
     | ::in-code use::
     | try:
     |    em.addField(
     |          name=field["name"],
     |          value=field["value"],
     |          inline=field["inline"]
     |      )
     | except KeyError:
     |    return FieldInitializeError({
     |          "message": "The field was not initialized correctly",
     |          "ErrorUrl": ""
     | })
    """

    @property
    def embed(self):
        import discord

        return discord.Embed(
            title="Embed Field Initialization Error",
            description="An embedField was not initialized properly.",
            color=0xFF0000,
            url=self.args[0]["ErrorUrl"]
        ).add_field(
            name="Error Name",
            value=self.__class__.__name__,
        )


class FooterInitializeError(Exception):
    """
     | ::context::
     | discord.py requires a paramiter when initializing an embed footer text.
     |
     | ::use::
     | The exception is raised when a keyError is thrown. This can be caused if the key is not found in the lua table.
     | This can also be caused if the value is not of the expected type.
     |
     | ::example::
     | function test()
     |      return newEmbed{title="...", description="..."}.addFooter() -- the text argument is missing
     | end
     |
     | ::in-code use::
     | try:
     |     em.set_footer(text=embed["footer"]["text"])
     |
     | except KeyError:
     |    return FieldInitializeError({
     |        "message": "the embed was not initialized correctly, the following keys were not found: footer",
     |        "ErrorUrl": ""
     |    })
    """

    @property
    def embed(self):
        import discord

        return discord.Embed(
            title="Embed Footer Initialization Error",
            description="The embed footer was not initialized correctly.",
            color=0xFF0000,
            url=self.args[0]["ErrorUrl"]
        ).add_field(
            name="Error Name",
            value=self.__class__.__name__,
        )
