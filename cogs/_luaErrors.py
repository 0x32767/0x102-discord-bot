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
     |     raise MaxEmbedFieldsExceeded({
     |          "message": f"the maximum amount of embeds has been reached got {len(embed['fields'])} >= 26",
     |          "ErrorUrl": "https://github.com/0x32767/0x102-discord-bot/..."
     | })
    """

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
     |    raise EmbedInitializeError({
     |          "message": "The embed was not initialized correctly",
     |          "ErrorUrl": ""
     | })
    """
