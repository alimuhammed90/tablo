
import discord
from discord.ext import commands
from discord import ui, ButtonStyle, TextStyle
from config import TOKEN

# Bot ayarları
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


# Modal pencere
class TestModal(ui.Modal, title="Test başlık"):

    field_1 = ui.TextInput(label="Kısa metin")

    field_2 = ui.TextInput(
        label="Uzun metin",
        style=TextStyle.paragraph
    )

    async def on_submit(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            f"Kısa metin: {self.field_1.value}\n"
            f"Uzun metin: {self.field_2.value}"
        )


# Buton
class TestButton(ui.Button):

    def __init__(self):
        super().__init__(
            label="Test etiketi",
            style=ButtonStyle.blurple
        )

    async def callback(self, interaction: discord.Interaction):

        # Modal pencereyi aç
        await interaction.response.send_modal(TestModal())

        # Buton rengini değiştir
        self.style = ButtonStyle.gray

        await interaction.message.edit(view=self.view)


# Buton görünümü
class TestView(ui.View):

    def __init__(self):
        super().__init__(timeout=180)
        self.add_item(TestButton())


# Bot hazır
@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı!")


# Test komutu
@bot.command()
async def test(ctx):

    await ctx.send(
        "Aşağıdaki butona tıklayın:",
        view=TestView()
    )


# Botu çalıştır
bot.run(TOKEN)
