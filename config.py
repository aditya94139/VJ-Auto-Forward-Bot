from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "93e1b0c387cabe34a3ccfa1724ae8527")
      API_ID = int(getenv("API_ID", "22946135"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6853274200:AAHZKnGn8fH00163zSVsdnFyZ8BQcVLWLos")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002103073685:-1002049432464").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
