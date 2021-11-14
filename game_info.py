import espn_scraper as espn
import pickle as pck

with open('march_madness/games/pck/game_ids.pck', 'rb') as f:
    data = pck.load(f)

DATA_TYPE = 'boxscore'


for game_id in data:
    url = espn.get_game_url(DATA_TYPE, 'ncb', game_id)
    game_data = espn.get_url(url, cached_path="games")
