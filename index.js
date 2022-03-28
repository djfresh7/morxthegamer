const { Telegraf } = require("telegraf")
const bot = new Telegraf(process.env.API_KEY)
const server = require("./serv.js")
const fs = require("fs")
const randomNumbers = (n1, n2) => {
  return Math.floor(Math.random() * (n2 - n1) + n2)
}
const warnUser = (userId, reason, count, name) => {
  fs.writeFile(`./userWarnings/${userId}.json`,
  JSON.stringify({
    userId: userId,
    name: name,
    reason: reason,
    warningCount: count
  }), (e,d) => {
    if (e) return
  })
}

const readUserWarn = (userId) => {
  fs.readFile(`/userWarnings/${userId}`, "utf-8", (e, d) => {
    if (d) return d;
  })
}

server.listening();

bot.start(ctx => ctx.reply("Hi, I'm @DJ-Fresh's Mod Bot. What would you like me to do for you?"))
bot.help(ctx => {
  fs.readFile("commands.txt", { encoding: "utf-8" }, (e,d) => {
    ctx.reply(d)
  })
})

bot.command("data", ctx => ctx.reply(ctx.message.from))
bot.command("meme", ctx => bot.telegram.sendPhoto(ctx.message.chat.id, "./memeeman.jpg"))

bot.command("random", ctx => {
  const message = String(ctx.message.text)
  const numbers = message.slice(7, message.length).split(",")
  ctx.reply(randomNumbers(numbers[0], numbers[1]))
})

bot.command("currentTime", ctx => {
  const date = new Date().toString();
  const todaysDate = date.slice(15, 24);
  ctx.reply(`The Current Time is: ${todaysDate}`)
})

bot.command("say", ctx => {
  const messageSent = ctx.message.text
  const slicedMessage = messageSent.slice(5, messageSent.length)
  ctx.reply(slicedMessage)
  console.log(messageSent, slicedMessage)
})

// Mod Commands:

bot.command("warn", ctx => {
  const msg = ctx.message.text.toString().slice(5, ctx.message.text.length)
  const userId = msg.split(",")[0]
  const name = msg.split(",")[1]
  const reason = msg.split(",")[2]
  warnUser(userId, reason, 1, name);
  ctx.reply(`${name} has been warned.`)
})

bot.command("ban", ctx => {
  const text = ctx.message.text.toString()
  const person = parseInt(`${text.slice(4, text.length)}`)
  bot.telegram.banChatMember(ctx.message.chat.id, person)
  ctx.reply(`${person} has been banned.`)
})

bot.command("mute", ctx => {
  const msg = ctx.message.text
  const items = msg.slice(6, msg.length)
  const userId = parseInt(items.split(",")[0])
  const reason = items.split(",")[1]
  bot.telegram.restrictChatMember(ctx.message.chat.id, userId, { "can_send_messages": false })
  ctx.reply(`${userId} has been muted due to ${reason}.`)
})

bot.command("warnings", ctx => {
  const msg = ctx.message.text
  const userId = msg.slice(9, msg.length)
  console.log(readUserWarn(userId))
})

bot.hears("boxcover", ctx => {
  bot.telegram.deleteMessage(ctx.message.chat.id, ctx.message.message_id)
  ctx.reply("Don't say that word in here.")
})

bot.launch()