from Player import Player
from Variants import Variants

bot = Player(variants=Variants.SCISSORS, name="ALEX")

alex = Player(variants=Variants.PAPER, name="STEVE")

print(bot.whoWins(target=alex))
bot.whoWinsDefault(foo=alex,target=bot)