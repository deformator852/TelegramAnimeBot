from create_bot import bot,data_base
from aiogram import types,Dispatcher
from keyboards.keyboard import kb_bot,kb_anime
import re
con = data_base.cursor()

async def take_info(message,ID):
    data = con.execute(f"SELECT name,content,images FROM anime WHERE ID = {ID} ")
    for d in data:
        await bot.send_message(message.from_user.id, "Name: " + d[0])
        await bot.send_message(message.from_user.id, d[1])
        await bot.send_photo(message.from_user.id,types.InputFile(d[2]))
        if d == d:
            break
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,"You started anime bot!",reply_markup=kb_bot)
async def command_output_anime_list(message:types.Message):
    data = con.execute("SELECT name,genre FROM anime")
    for d in data:
        await bot.send_message(message.from_user.id,"Name: "+d[0]+" | Genre: "+d[1])
async def command_anime_info(message:types.Message):
    await bot.send_message(message.from_user.id,"⁠",reply_markup=kb_anime)
async def command_Anime_ByReleaseDate(message: types.Message):
    data = con.execute("SELECT data_release,name FROM anime")
    data = list(data)
    data.sort()
    for d in data:
        await bot.send_message(message.from_user.id,d[1]+" — "+d[0])

async def command_BackMenu(message:types.Message):
    await bot.send_message(message.from_user.id,"⁠",reply_markup=kb_bot)
async def command_Shonen(message: types.Message):
    data = con.execute(r"SELECT name,genre FROM anime")
    for d in data:
        if re.search(r"[Ss]honen",d[1]):
          await bot.send_message(message.from_user.id,d[0])
async def command_Naruto(message:types.Message):
  await take_info(message,1)
async def command_DemonSlayer(message:types.Message):
  await take_info(message,2)
async def command_BlackClover(message:types.Message):
  await take_info(message,3)
async def command_HunterXHunter(message:types.Message):
  await take_info(message,4)
async def command_DeathNote(message:types.Message):
  await take_info(message,5)
async def command_TokyoGhoul(message:types.Message):
  await take_info(message,6)
async def command_CyberpunkEdgerunners(message:types.Message):
  await take_info(message,7)
async def command_ChainsawMan(message:types.Message):
  await take_info(message,8)
async def command_DarlingInTheFranXX(message:types.Message):
  await take_info(message,9)
async def command_AttackOnTitan(message:types.Message):
  await take_info(message,10)
async def command_SwordArtOnline(message:types.Message):
  await take_info(message,11)
async def command_ThePromisedNeverland(message:types.Message):
  await take_info(message,12)
async def command_TokyoRevengers(message:types.Message):
  await take_info(message,13)
async def command_Horimiya(message:types.Message):
  await take_info(message,14)
async def command_TheSevenDeadlySins(message:types.Message):
  await take_info(message,15)
async def command_ClassroomOfTheElite(message:types.Message):
  await take_info(message,16)
async def command_TheQuintessentialQuintuplets(message:types.Message):
  await take_info(message,17)
async def command_OnePiece(message:types.Message):
    await take_info(message,18)
async def command_Bleach(message:types.Message):
    await take_info(message,19)
async def command_KurokoBasketball(message:types.Message):
    await take_info(message,20)
def register_handlers_anime_list(dp: Dispatcher):
    dp.register_message_handler(command_start, commands="start")
    dp.register_message_handler(command_output_anime_list,commands="Output_the_anime_list")
    dp.register_message_handler(command_anime_info,commands="Anime_info")
    dp.register_message_handler(command_Anime_ByReleaseDate, commands="AnimeByReleaseDate")
    dp.register_message_handler(command_BackMenu,commands="BackMenu")
    dp.register_message_handler(command_Shonen, commands="Shonen")
    dp.register_message_handler(command_Naruto,commands="Naruto")
    dp.register_message_handler(command_DemonSlayer, commands="DemonSlayer")
    dp.register_message_handler(command_BlackClover, commands="BlackClover")
    dp.register_message_handler(command_HunterXHunter, commands="HunterXHunter")
    dp.register_message_handler(command_DeathNote, commands="DeathNote")
    dp.register_message_handler(command_TokyoGhoul, commands="TokyoGhoul")
    dp.register_message_handler(command_CyberpunkEdgerunners, commands="CyberpunkEdgerunners")
    dp.register_message_handler(command_ChainsawMan, commands="ChainsawMan")
    dp.register_message_handler(command_DarlingInTheFranXX,commands="DarlingInTheFranXX")
    dp.register_message_handler(command_AttackOnTitan, commands="AttackOnTitan")
    dp.register_message_handler(command_SwordArtOnline, commands="SwordArtOnline")
    dp.register_message_handler(command_ThePromisedNeverland, commands="ThePromisedNeverland")
    dp.register_message_handler(command_TokyoRevengers, commands="TokyoRevengers")
    dp.register_message_handler(command_Horimiya, commands="Horimiya")
    dp.register_message_handler(command_TheSevenDeadlySins, commands="TheSevenDeadlySins")
    dp.register_message_handler(command_ClassroomOfTheElite, commands="ClassroomOfTheElite")
    dp.register_message_handler(command_TheQuintessentialQuintuplets, commands="TheQuintessentialQuintuplets")
    dp.register_message_handler(command_OnePiece,commands="OnePiece")
    dp.register_message_handler(command_Bleach,commands="Bleach")
    dp.register_message_handler(command_KurokoBasketball,commands="Kuroko'sBasketball")