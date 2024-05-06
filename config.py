from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "410f922c49c8867b5c8e28d624581b02")
      API_ID = int(getenv("API_ID", "26558850"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6856319965:AAGumAO4K6bPb0TwLs6LqX4Hp03TshbLZA0")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002014583516:-1002039595984").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
