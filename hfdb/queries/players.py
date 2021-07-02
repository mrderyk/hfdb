import datetime as dt
from peewee import fn
from .. models import Player

def get_player_data(player_keys=[]):
  return Player.select().where(Player.key << player_keys)

def get_players_by_search_string(str):
  return Player.select() \
    .where(
      Player.searchable_tokens.contains(str)
    )

