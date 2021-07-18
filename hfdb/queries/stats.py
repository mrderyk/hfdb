from .. models import PlayerStatsRegular, PlayerStatsPlayoff


def get_regular_season_stats_by_player_key(player_key):
  return PlayerStatsRegular.select() \
    .where(PlayerStatsRegular.player_key == player_key) \
    .order_by(PlayerStatsRegular.season.asc())


def get_regular_season_stat_by_player_key_and_category(player_key, category, season):
  return PlayerStatsRegular.select(getattr(PlayerStatsRegular, category)) \
    .where(
      (PlayerStatsRegular.player_key == player_key) &
      (PlayerStatsRegular.season == season)
    )


def get_playoff_stats_by_player_key(player_key):
  return PlayerStatsPlayoff.select() \
    .where(PlayerStatsPlayoff.player_key == player_key) \
    .order_by(PlayerStatsPlayoff.season.asc())


def get_playoff_stat_by_player_key_and_category(player_key, category, season):
  return PlayerStatsPlayoff.select(getattr(PlayerStatsPlayoff, category)) \
    .where(
      (PlayerStatsPlayoff.player_key == player_key) &
      (PlayerStatsPlayoff.season == season)
    )