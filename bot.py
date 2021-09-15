import telebot, telegram
import time, logging
from PIL import Image
import requests, os
from io import BytesIO
from datetime import datetime
import yfinance as yf, random
import pyshorteners

# Bot Token & Login
TOKEN = os.environ["API_KEY"]
bot = telebot.TeleBot(TOKEN)

# Variable Resources
IMAGE_LINK = "https://i.insider.com/602ee9e3d3ad27001837f2af?width=1200&format=jpeg"
IMAGE_LINK_2 = "https://i.redd.it/e89q25yrt1b71.png"
MTG_IMG_LINK = "https://yt3.ggpht.com/ytc/AKedOLQ7DfRifmKKL1O0C0HlDtbqgcR0cXvxzHoLyX0FzQ=s900-c-k-c0x00ffffff-no-rj"
AUDIO_LINK = "https://www.soundjay.com/human/sounds/burp-1.mp3"
AUDIO_LINK_2 = "https://www.soundjay.com/communication/sounds/computer-keyboard-1.mp3"
VIDEO_LINK = "https://preview.redd.it/fe9zyvsavdc71.gif?format=mp4&s=f717b27d53684ccfe7a618d17cf0a452a3cab761"
VIDEO_LINK_2 = "https://www.hubspot.com/hubfs/Smiling%20Leo%20Perfect%20GIF.gif"
VIDEO_LINK_3 = "https://i.gifer.com/H6u.gif"
SUBTOMORX_TEXT = "Like MorxTheGamer? Well, you can subscribe to his YouTube Channel:\nhttps://youtube.com/morxthegamer\n\nHere's a little secret: MorxTheGamer is the creator of this bot."
COMMANDS_TEXT = "All the avaliable commands for the DJ-Fresh Utilities Bot:\n\nInterface Commands:\n/start - Starts the bot.\n/stop - Stops the bot.\n/commands - Show this message.\n\nStatistics Commands:\n/covid19stats - Gives you a link to the latest covid 19 stats website.\n/bbsongcharts - Gives you a link to the latest billboard song chart lists.\n/topsubreddits - Gives you a link to the daily top subreddits on reddit.\n/memecmdstats - Shows you all the links to the memes used in the meme commands.\n\nFun Commands:\n/meme - Shows you a meme...You'll love this command.\n/rick - Shows you a image of rick. You'll also love this command.\n/morx - Shows you an image of MorxTheGamer & a link to his YouTube channel.\n/memevid - Shows you a meme video (its a short one).\n/toastvid - Shows you video of a man making a toast.\n/rickroll - You should know what this command will do.\n/wake - Sends a wake sticker.\n/jump - Sends a jumping sticker.\n/ktype - Sends an audio of someone typing on a keyboard.\n/burp - Sends an audio of someone burping (don't use this).\n/ntime - Tells the current time.\n\nSuper Fun Commands:\n/say (text) - Replies with what you want you to say.\n/rand (first num, second num) - Generates a random number from the two numbers you sent.\n\nStock Commands:\n/price (stock) - Tells the price of the stock mentioned (yahoo finance).\n/stks - Tells you the stocks and their prices (yahoo finance).\n\nNB: Make sure to use '/' before every command!"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def download_file(url, name):
  r = requests.get(url, stream=True)
  with open(name, 'wb') as f:
      for chunk in r.iter_content(chunk_size=1024):
          if chunk:
              f.write(chunk)

def echo(update, context):
  update.message.reply_text('Help!')

def short(url):
  return pyshorteners.Shortener().tinyurl.short(url)

def getargs(text):
  _args = text.split()[1:]
  return _args

# Stocks Command
@bot.message_handler(commands=['stks'])
def get_stocks(message):
  response = ""
  stocks = ['gme', 'amc', 'nok']
  stock_data = []
  for stock in stocks:
    data = yf.download(tickers=stock, period='2d', interval='1d')
    data = data.reset_index()
    response += f"-----{stock}-----\n"
    stock_data.append([stock])
    columns = ['stock']
    for index, row in data.iterrows():
      stock_position = len(stock_data) - 1
      price = round(row['Close'], 2)
      format_date = row['Date'].strftime('%m/%d')
      response += f"{format_date}: {price}\n"
      stock_data[stock_position].append(price)
      columns.append(format_date)
    print()

  response = f"{columns[0] : <10}{columns[1] : ^10}{columns[2] : >10}\n"
  for row in stock_data:
    response += f"{row[0] : <10}{row[1] : ^10}{row[2] : >10}\n"
  response += "\nStock Data"
  print(response)
  bot.send_message(message.chat.id, response)

def stock_request(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "/price":
    return False
  else:
    return True

@bot.message_handler(func=stock_request)
def send_price(message):
  request = message.text.split()[1]
  data = yf.download(tickers=request, period='5m', interval='1m')
  if data.size > 0:
    data = data.reset_index()
    data["format_date"] = data['Datetime'].dt.strftime('%m/%d %I:%M %p')
    data.set_index('format_date', inplace=True)
    print(data.to_string())
    bot.send_message(message.chat.id, data['Close'].to_string(header=False))
  else:
    bot.send_message(message.chat.id, "No data!?")

# Main Commands
@bot.message_handler(commands=["start"])
def start(message):
  print(message.text)
  bot.reply_to(message, "Hi, I'm @DJ-Fresh's Utilities. What would you like me to do for you?")

@bot.message_handler(commands=["commands", "cmds"])
def commands(message):
  bot.reply_to(message, COMMANDS_TEXT)
  bot.send_message(message.chat.id, "Ready to use these commands?\n\nWell, you can:\n\n1. Choose & Run any of the commands above.\n2. If you're using a PC, start typing / to see & use any command.\n3. If you're on mobile, press the Menu tab to see & use any command.")

@bot.message_handler(commands=["covid19stats"])
def covid19stats(message):
  bot.reply_to(message, "To review the latest statistics with Covid-19, please go to:\nhttps://www.worldometers.info/coronavirus/")

@bot.message_handler(commands=["bbsongcharts"])
def bbsongcharts(message):
  bot.reply_to(message, "To see the lastest billboard song charts, please go to:\nhttps://www.billboard.com/charts")

@bot.message_handler(commands=["topsubreddits"])
def topsubreddits(message):
  bot.reply_to(message, "To see today's top subreddits on reddit, please go to:\nhttps://www.reddit.com/subreddits/leaderboard")

@bot.message_handler(commands=["memecmdstats"])
def memecmdstats(message):
  bot.reply_to(message, "All current memes used in the meme commands:\n\n/meme command:\nLink: https://i.redd.it/e89q25yrt1b71.png\n\n/memevid command:\nLink: https://preview.redd.it/fe9zyvsavdc71.gif?format=mp4&s=f717b27d53684ccfe7a618d17cf0a452a3cab761\n\nAll meme commands get updated every week, so don't miss out on all the fresh memes coming out every week!\n\nAll memes are distributed from https://reddit.com/r/memes.")

@bot.message_handler(commands=["meme"])
def meme(message):
  response = requests.get(IMAGE_LINK_2)
  meme = Image.open(BytesIO(response.content))
  bot.send_photo(message.chat.id, meme)
  print(meme)

@bot.message_handler(commands=["rick"])
def rick(message):
  response = requests.get(IMAGE_LINK)
  image = Image.open(BytesIO(response.content))
  bot.send_photo(message.chat.id, image)
  print(image)

@bot.message_handler(commands=["morx"])
def mtgimg(message):
  response = requests.get(MTG_IMG_LINK)
  mtg = Image.open(BytesIO(response.content))
  bot.send_photo(message.chat.id, mtg)
  bot.send_message(message.chat.id, SUBTOMORX_TEXT)
  print(mtg)

@bot.message_handler(commands=["wake"])
def wake(message):
  bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEClttg8fr5P1IP1Bw5LzCzg9bR16odwAACEAADwDZPE-qBiinxHwLoIAQ")

@bot.message_handler(commands=["jump"])
def jump(message):
  bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEClt9g8fxNV33-tFE7hvYAAWv1ijRbSMAAAgEAA8A2TxMYLnMwqz8tUSAE")

@bot.message_handler(commands=["ntime"])
def ntime(message):
  now = datetime.now()
  date_time = now.strftime("The current time is:\n%d/%m/%y, %H:%M:%S")
  bot.reply_to(message, date_time)
  print()

@bot.message_handler(commands=["say"])
def texttospeech(message):
  args = getargs(message.text)
  text = "".join(args[0:1])
  try:
    bot.reply_to(message, text)
  except Exception as e:
    bot.reply_to(message, "There was an error running this command.")
    return e
  print(text)

@bot.message_handler(commands=["rand"])
def rand(message):
  stuff1 = message.text[6:7]
  stuff2 = message.text[8:10]
  s1 = int(stuff1)
  s2 = int(stuff2)
  num = random.randrange(s1, s2)
  try:
    bot.reply_to(message, num)
  except Exception as a:
    bot.reply_to(message, "There was an error running this command.")
    return a
  print(num, message.text)

@bot.message_handler(commands=["stop"])
def stop(message):
  bot.send_message(message.chat.id, "Bot stopped. Use the /start command to start the bot.")
  print(message.text)

@bot.message_handler(content_types=['photo', 'video', 'document', 'audio'])
def file_sent(message):
  try:
    bot.send_message(message.chat.id, short(bot.get_file_url(message.document.file_id)))
  except AttributeError:
      try:
        bot.send_message(message.chat.id, short(bot.get_file_url(message.photo[0].file_id)))
      except AttributeError:
          try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.video.file_id)))
          except AttributeError:
            try:
              bot.send_message(message.chat.id, short(bot.get_file_url(message.audio.file_id)))
            except AttributeError:
              pass
              print()

# video & audio commands
@bot.message_handler(commands=["memevid", "mvd"])
def memevid(message):
  download_file(VIDEO_LINK, "mvd.gif")
  vidmeme = open("mvd.gif", "rb")
  bot.send_video(message.chat.id, vidmeme)
  print(vidmeme)

@bot.message_handler(commands=["toastvid", "tvd"])
def toastvid(message):
  download_file(VIDEO_LINK_2, "tvd.gif")
  toavid = open("tvd.gif", "rb")
  bot.send_video(message.chat.id, toavid)
  print(toavid)

@bot.message_handler(commands=["rickroll", "rkr"])
def rickroll(message):
  download_file(VIDEO_LINK_3, "rkr.gif")
  rkrgif = open("rkr.gif", "rb")
  bot.send_video(message.chat.id, rkrgif)
  print(rkrgif)

@bot.message_handler(commands=["ktype", "ktp"])
def ktype(message):
  download_file(AUDIO_LINK_2, "ktype.mp3")
  ktpf = open("ktype.mp3", "rb")
  bot.send_audio(message.chat.id, ktpf)
  print(ktpf)

@bot.message_handler(commands=["burp", "bp"])
def burp(message):
  download_file(AUDIO_LINK, "burp.mp3")
  bep = open("burp.mp3", "rb")
  bot.send_audio(message.chat.id, bep)
  print(bep)

while True:
    try:
        bot.polling()
    except:
        time.sleep(5)