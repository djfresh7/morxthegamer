# Init Imports
import telebot, time, os
from alive import alive
from PIL import Image
from io import BytesIO
import requests, pytube as pt
from datetime import datetime
import yfinance as yf, random
import pyshorteners as pshrts

# Init Variables
token = os.environ["API_KEY"]
bot = telebot.TeleBot(token)
imageLink = "https://i.insider.com/602ee9e3d3ad27001837f2af?width=1200&format=jpeg"
imageLink2 = "https://i.redd.it/e89q25yrt1b71.png"
mtgImgLink = "https://yt3.ggpht.com/ytc/AKedOLQ7DfRifmKKL1O0C0HlDtbqgcR0cXvxzHoLyX0FzQ=s900-c-k-c0x00ffffff-no-rj"
audioLink = "https://www.soundjay.com/human/sounds/burp-1.mp3"
audioLink2 = "https://www.soundjay.com/communication/sounds/computer-keyboard-1.mp3"
videoLink = "https://preview.redd.it/fe9zyvsavdc71.gif?format=mp4&s=f717b27d53684ccfe7a618d17cf0a452a3cab761"
videoLink2 = "https://www.hubspot.com/hubfs/Smiling%20Leo%20Perfect%20GIF.gif"
videoLink3 = "https://i.gifer.com/H6u.gif"
subToMorxText = "Like MorxTheGamer? Well, you can subscribe to his YouTube Channel:\nhttps://youtube.com/morxthegamer\n\nHere's a little secret: MorxTheGamer is the creator of this bot."
errorText = "There was an error running this command."

with open("botsfiles/cmds.txt", "r") as cmds:
  commandsText = cmds.read()
with open("botsfiles/shorts.txt", "r") as shrts:
  shortsText = shrts.read()

# Init Functions
def download_file(url, name):
  r = requests.get(url, stream=True)
  with open(name, 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
      if chunk:
          f.write(chunk)

def download_yt_file(url, path):
  yt = pt.YouTube(url)
  yt = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
  if not os.path.exists(path):
    os.mkdir(path)
  yt.download(path)

def short(url):
  return pshrts.Shortener().tinyurl.short(url)

# Stocks & Price Commands
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

# Main Commands/Functions
@bot.message_handler(commands=["start"])
def start(message):
  bot.reply_to(message, "Hi, I'm @DJ-Fresh's Utilities. What would you like me to do for you?")
  print(message.text)

@bot.message_handler(commands=["commands", "cmds"])
def commands(message):
  bot.reply_to(message, commandsText)
  bot.send_message(message.chat.id, "Ready to use these commands?\n\nWell, you can:\n\n1. Choose & Run any of the commands above.\n2. If you're using a PC, start typing / to see & use any command.\n3. If you're on mobile, press the Menu tab to see & use any command.")

@bot.message_handler(commands=["shortlinks", "shrts"])
def url_shorts(message):
  bot.reply_to(message, shortsText)

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

# Image Commands
@bot.message_handler(commands=["meme"])
def meme(message):
  response = requests.get(imageLink2)
  meme = Image.open(BytesIO(response.content))
  bot.send_photo(message.chat.id, meme)
  print(meme)

@bot.message_handler(commands=["rick"])
def rick(message):
  response = requests.get(imageLink)
  image = Image.open(BytesIO(response.content))
  bot.send_photo(message.chat.id, image)
  print(image)

@bot.message_handler(commands=["morx"])
def mtgimg(message):
  response = requests.get(mtgImgLink)
  mtg = Image.open(BytesIO(response.content))
  bot.send_photo(message.chat.id, mtg)
  bot.send_message(message.chat.id, subToMorxText)
  print(mtg)

# Sticker Commands
@bot.message_handler(commands=["wake"])
def wake(message):
  bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEClttg8fr5P1IP1Bw5LzCzg9bR16odwAACEAADwDZPE-qBiinxHwLoIAQ")

@bot.message_handler(commands=["jump"])
def jump(message):
  bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEClt9g8fxNV33-tFE7hvYAAWv1ijRbSMAAAgEAA8A2TxMYLnMwqz8tUSAE")

# Time Command
@bot.message_handler(commands=["currtime"])
def currentTime(message):
  now = datetime.now()
  date_time = now.strftime("The current time is:\n%d/%m/%y, %H:%M:%S")
  bot.reply_to(message, date_time)
  print(date_time)

# Multifunctional Commands
@bot.message_handler(commands=["say"])
def texttospeech(message):
  text = message.text[5:]
  try:
    bot.reply_to(message, text)
  except Exception:
    bot.reply_to(message, errorText)
  print(text)

@bot.message_handler(commands=["randnum"])
def randnum(message):
  numbers = str(message.text[9:]).split(",")
  numbers[0], numbers[1] = int(numbers[0]), int(numbers[1])
  num = random.randint(numbers[0], numbers[1])
  try:
    bot.reply_to(message, num)
  except Exception:
    bot.reply_to(message, errorText)
  print(num, numbers)

@bot.message_handler(content_types=['photo', 'video', 'document', 'audio'])
def file_sent(message):
  try:
    bot.send_message(message.chat.id, "Save your document with a shortened link:\n" + short(bot.get_file_url(message.document.file_id)))
  except AttributeError:
      try:
        bot.send_message(message.chat.id, "Save your photo with a shortened link:\n" + short(bot.get_file_url(message.photo[0].file_id)))
      except AttributeError:
          try:
            bot.send_message(message.chat.id, "Save your video with a shortened link:\n" + short(bot.get_file_url(message.video.file_id)))
          except AttributeError:
            try:
              bot.send_message(message.chat.id, "Save your audio with a shortened link:\n" + short(bot.get_file_url(message.audio.file_id)))
            except Exception:
              bot.send_message(message.chat.id, "Failed to generate a shortened link for your file. Please try again.")

@bot.message_handler(commands=["random"])
def randum(message):
  completely_rand = random.random()
  bot.reply_to(message, completely_rand)
  print(completely_rand)

@bot.message_handler(commands=["evorod"])
def evorod(message):
  even_or_odd = int(message.text[8:])
  if even_or_odd % 3 != 0:
    bot.reply_to(message, "That number is even.")
  else:
    bot.reply_to(message, "That number is odd.")
  print(even_or_odd)

@bot.message_handler(commands=["spam"])
def spam(message):
  spam_text = str(message.text[6:-2])
  spam_amount = int(message.text[-2:])
  for num in range(spam_amount):
    try:
      bot.reply_to(message, spam_text)
    except Exception:
      bot.reply_to(message, errorText)
  print(spam_text, spam_amount)

@bot.message_handler(commands=["morespam"])
def morespam(message):
  text = str(message.text[10:-4])
  num_range = int(message.text[-4:])
  print(text)
  print(num_range)
  for number in range(num_range):
    try:
      bot.reply_to(message, text)
    except Exception:
      bot.reply_to(message, errorText)

@bot.message_handler(commands=["evenmorespam"])
def evenmorespam(message):
  new = str(message.text[14:-6])
  the_num = int(message.text[-6:])
  print(new)
  print(the_num)
  for x in range(the_num):
    try:
      bot.reply_to(message, new)
    except Exception:
      bot.reply_to(message, errorText)

# Video & Audio Commands
@bot.message_handler(commands=["ytvideo"])
def ytvideo(message):
  link = message.text[9:]
  download_yt_file(link, "ytvideos/")
  for file in os.listdir("ytvideos/"):
    os.rename("ytvideos/" + file, "ytvideos/ytvideo.mp4")
  fi = open("ytvideos/ytvideo.mp4", "rb")
  try:
    bot.send_video(message.chat.id, fi)
  except Exception:
    bot.reply_to(message, errorText)
  print(fi, link)
  for file in os.listdir("ytvideos/"):
    os.remove("ytvideos/" + file)

@bot.message_handler(commands=["ytaudio"])
def ytaudio(message):
  aud = message.text[9:]
  download_yt_file(aud, "ytvideos/")
  for fil in os.listdir("ytvideos/"):
    os.rename("ytvideos/" + fil, "ytvideos/ytaudio.mp3")
  get = open("ytvideos/ytaudio.mp3", "rb")
  try:
    bot.send_audio(message.chat.id, get)
  except Exception:
    bot.reply_to(message, errorText)
    print(aud, get)
  for fil in os.listdir("ytvideos/"):
    os.remove("ytvideos/" + fil)

@bot.message_handler(commands=["memevid", "mvd"])
def memevid(message):
  download_file(videoLink, "botsfiles/mvd.gif")
  vidmeme = open("botsfiles/mvd.gif", "rb")
  bot.send_video(message.chat.id, vidmeme)
  print(vidmeme)

@bot.message_handler(commands=["toastvid", "tvd"])
def toastvid(message):
  download_file(videoLink2, "botsfiles/tvd.gif")
  toavid = open("botsfiles/tvd.gif", "rb")
  bot.send_video(message.chat.id, toavid)
  print(toavid)

@bot.message_handler(commands=["rickroll", "rkr"])
def rickroll(message):
  download_file(videoLink3, "botsfiles/rkr.gif")
  rkrgif = open("botsfiles/rkr.gif", "rb")
  bot.send_video(message.chat.id, rkrgif)
  print(rkrgif)

@bot.message_handler(commands=["ktype", "ktp"])
def ktype(message):
  download_file(audioLink2, "botsfiles/ktype.mp3")
  ktpf = open("botsfiles/ktype.mp3", "rb")
  bot.send_audio(message.chat.id, ktpf)
  print(ktpf)

@bot.message_handler(commands=["burp", "bp"])
def burp(message):
  download_file(audioLink, "botsfiles/burp.mp3")
  bep = open("botsfiles/burp.mp3", "rb")
  bot.send_audio(message.chat.id, bep)
  print(bep)

@bot.message_handler(content_types=["text"])
def save_txt_file(message):
  key = str(random.randrange(100, 1000))
  key_file = "userfiles/file{}.txt"
  if "/save" in message.text:
    txt = message.text[6:]
    with open(key_file.format(key), "w") as f:
      try:
        f.write(txt)
        bot.reply_to(message, f"Your file has been saved. Your file key is {key}.")
      except Exception:
        bot.reply_to(message, "Failed to save text file.")
  elif "/open" in message.text:
    tok = message.text[6:]
    with open(key_file.format(tok), "r") as op:
      try:
        get = op.read()
        bot.reply_to(message, get)
      except Exception:
        bot.reply_to(message, f"No file with the key {tok} exists.")
  elif "/edit" in message.text:
    fid = message.text[6:9]
    msg = message.text[10:]
    with open(key_file.format(fid), "w") as ed:
      try:
        ed.write(msg)
        bot.reply_to(message, "Your saved file has been edited successfully.")
      except Exception:
        bot.reply_to(message, f"Failed to edit file. Please to check if the file exists or if you placed in the text to edit.")
  elif "/del" in message.text:
    toky = message.text[5:]
    if toky:
      os.remove(key_file.format(toky))
      try:
        bot.reply_to(message, "Your saved file has been deleted.")
      except Exception:
        bot.reply_to(message, f"No file with the key: {toky} exists.")
    else:
      bot.reply_to(message, "You didn't specify a file to delete. Please try again.")
  else:
    pass

@bot.message_handler(commands=["stop"])
def stop(message):
  bot.send_message(message.chat.id, "Bot stopped. Use the /start command to start the bot.")
  print(message.text)
  time.sleep(10)

if __name__ == "__main__":
  alive()
  while True:
    try:
      bot.infinity_polling()
    except Exception as exception:
      print(f"{exception}...Taking care of error.")
      time.sleep(10)