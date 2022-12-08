import disnake
from disnake.ext import commands
from Kiriko.Core import Kiriko


class Template(commands.Cog):
    def __init__(self, bot: Kiriko):
        self.bot: Kiriko = bot

    @commands.slash_command(name="Template", description="A Template")
    async def Template(self, interaction: disnake.CommandInteraction):
        # True -> Only the Invoker can see the response; False -> everyone can see the response
        await interaction.response.defer(ephemeral=True)
        await interaction.edit_original_message(content=f"This is a Template")

    @commands.command(name="ping")
    async def TemplateCTX(self, ctx: commands.Context):
        await ctx.reply(content=f"This is a Template")  # reply, send


def setup(bot: Kiriko):
    bot.add_cog(Template(bot))
