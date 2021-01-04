import vkquick as vq
bot = vq.Bot.init_via_token("токен сюда")

@bot.add_command(names=[".*(?:инсаф|insaf|556|инcaф|инсaф|инcаф).*"], use_regex_escape=False)
async def hello_text(ctx: vq.Context):
    await ctx.reply(sticker_id=18493)
@bot.add_command(names=[".*(?:спокойной ночи|ятам|йоклыйм).*"], use_regex_escape=False)
async def hello_text(ctx: vq.Context):
    await ctx.reply(sticker_id=16492)
@bot.add_command(names=[".*(?:доброе утро|добрый день).*"], use_regex_escape=False)
async def hello_text(ctx: vq.Context):
    await ctx.reply(sticker_id=11275)
bot.run()
