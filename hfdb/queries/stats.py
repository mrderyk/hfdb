from .. models import PlayerStatsRegular


def get_regular_season_stats_by_player_key(player_key):
  return PlayerStatsRegular.select() \
    .where(PlayerStatsRegular.player_key == player_key) \
    .order_by(PlayerStatsRegular.season.asc())
