const { Telegraf } = require("telegraf")
const { listens } = require("./server.js")
const fs = require("fs")
const { classes, linksForClasses, timeTable, StopError } = require("./data.js")
const bot = new Telegraf(process.env.TOKEN);

listens();

bot.start(ctx => {
  ctx.reply(`Hello ${ctx.message.from.username}! What link do you want today?`);
});

bot.help(ctx => {
  fs.readFile("cmds.txt", "utf-8", (err, data) => {
    if (err) throw err;
    ctx.reply(data.toString());
  })
})

bot.command("subjects", ctx => {
  ctx.reply("Here is the list for all the classes in G9: (TOTAL: 16)")
  ctx.reply(classes.join("\n"))
})

bot.command("getlink", ctx => {
  const getClass = ctx.message.text
  const theClass = getClass.slice(9, getClass.length)
  if (!theClass) {
    ctx.reply("Please specify a class.")
    return;
  }
  if (theClass.includes(" ")) {
    ctx.reply("Please try again without spaces.");
    return;
  }
  if (eval(`linksForClasses.${theClass}`) == null) {
    ctx.reply("I have no record of this class.");
    return;
  }
  
  ctx.reply(`Meeting Link:\n${eval(`linksForClasses.${theClass}.meetingLink`)}`)
})

bot.command("getinfo", ctx => {
  const getClass = ctx.message.text
  const theClass = getClass.slice(9, getClass.length)
  if (!theClass) {
    ctx.reply("Please specify a class.")
    return;
  }
  if (theClass.includes(" ")) {
    ctx.reply("Please try again without spaces.");
    return;
  }
  if (eval(`linksForClasses.${theClass}`) == null) {
    ctx.reply("I have no record of this class.");
    return;
  }
  if (eval(`linksForClasses.${theClass}.platform`) === "Meet") {
    ctx.reply("No avaliable information for this class's credentials.")
    return;
  }
  ctx.reply(`Meeting ID: ${eval(`linksForClasses.${theClass}.meetingID`)}`)
  ctx.reply(`Meeting Password: ${eval(`linksForClasses.${theClass}.meetingPassword`)}`)
})

bot.command("getplatform", ctx => {
  const getClass = ctx.message.text
  const theClass = getClass.slice(13, getClass.length)
  if (!theClass) {
    ctx.reply("Please specify a class.")
    return;
  }
  if (theClass.includes(" ")) {
    ctx.reply("Please try again without spaces.");
    return;
  }
  if (eval(`linksForClasses.${theClass}`) == null) {
    ctx.reply("I have no record of this class.");
    return;
  }
  ctx.reply(`Platform: ${eval(`linksForClasses.${theClass}.platform`)}`)
})

bot.command("schedule", ctx => {
  const text = ctx.message.text
  const day = text.slice(10, text.length)
  if (!day) {
    ctx.reply("Please select a day.")
    return;
  }
  if (day.includes(" ")) {
    ctx.reply("Please try again without spaces.");
    return;
  }
  if (eval(`timeTable.${day}`) == null) {
    ctx.reply("I have no record of this day.")
    return;
  }
  const message = eval(`timeTable.${day}`)
  ctx.reply(`TimeTable for ${day}:`)
  ctx.reply(message.join("\n"))
})

bot.command("stop", ctx => {
  if (ctx.message.from.id === 1756444685) {
    ctx.reply("[OWNER REQUEST]: Stopping the bot...")
    throw new StopError("Owner has stopped the bot.");
  }
  bot.telegram.deleteMessage(ctx.message.chat.id, ctx.message.message_id)
  ctx.reply("Bot refused to terminate. You do not have permissions to stop this bot.");
})

bot.launch();