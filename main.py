import mytoken
import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print(f"Sync for {self.user}")

    async def on_ready(self):
        print("Online")


bot = Bot()


@bot.hybrid_command(
    name="test", description="Calcula los dias restantes para la fecha entregada."
)
@app_commands.guilds(discord.Object(id=1491945644254957639))
async def test(ctx: commands.Context, date_user: str):
    try:
        date = datetime.strptime(date_user, "%d-%m-%Y").date()
        today = datetime.now().date()
        days_left = (date - today).days

        if days_left < 0:
            await ctx.send(f"Amigo te atrasaste {abs(days_left)}")
        elif days_left == 0:
            await ctx.send(f"¡ES HOY! 🥳")
        else:
            await ctx.send(f"Faltan {days_left} días para el {date_user}")
    except ValueError:
        await ctx.send("Esta mal escrita la fecha nano. Solo se acepta DD-MM-YYYY")


if __name__ == "__main__":
    bot.run(mytoken.TOKEN)
