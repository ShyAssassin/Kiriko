import disnake
from disnake.ext import commands
from Kiriko.Core import Kiriko


class Ping(commands.Cog):
    def __init__(self, bot: Kiriko):
        self.bot: Kiriko = bot

    @commands.slash_command(name="ping")
    async def Ping(self, interaction: disnake.CommandInteraction):
        await interaction.response.defer(ephemeral=True)
        await interaction.edit_original_message(content=f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command(name="ping")
    async def PingCTX(self, ctx: commands.Context):
        await ctx.reply(f"Pong! {round(self.bot.latency * 1000)}ms")


def setup(bot: Kiriko):
    bot.add_cog(Ping(bot))
