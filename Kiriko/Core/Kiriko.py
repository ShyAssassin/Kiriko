import os
import disnake
from disnake.ext import commands


class Kiriko(commands.Bot):
    def __init__(self, **options):
        self.Ready: bool = False
        # NOTE: If folder structure ever changed update this
        self.CogPath: str = os.path.join("Core", "Cogs")
        super().__init__(
            reload=True,
            help_command=None,
            command_prefix="*",
            case_insensitive=True,
            intents=disnake.Intents.all(),
            **options
        )

    async def on_ready(self):
        # on_ready is called more than once sometimes
        if not self.Ready:
            print(f"Bot connect to {self.user}")
            print("Loading Extensions...")
            # Dynamically load all cogs
            for cog in os.listdir(self.CogPath):
                if not cog.startswith("_") and cog.endswith(".py"):
                    CurrentCogPath = str(os.path.join(self.CogPath, cog))
                    CurrentCogModule = CurrentCogPath.replace("\\", ".")[:-3]
                    self.load_extension(CurrentCogModule)
                    print(f"Loaded Extension: Kirko.{CurrentCogModule}")
            print("All Extension Loaded!")
            self.Ready = True

    def run(self):
        super().run(os.getenv("DISCORD_TOKEN"))
