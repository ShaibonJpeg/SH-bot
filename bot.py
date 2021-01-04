import vkquick as vq
bot = vq.Bot.init_via_token("f757ab54278ff4eb3c6d36668b0b3a9e4f99af40e4fdaeb04294e63f50c39c1bae2540259fb7925344c3f")

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
