import espn_scraper as espn
import time
import pickle as pck

LEAGUE = "ncb"
YEARS = list(range(2001,2022))

game_ids = []
for year in YEARS:
    start = time.perf_counter()
    scoreboard_urls = espn.get_all_scoreboard_urls(LEAGUE, year)
    for url in scoreboard_urls:
        try:
            data = espn.get_url(url, cached_path="games")
            for event in data['content']['sbData']['events']:
                if event['id'] not in game_ids:
                    game_ids.append(event['id'])
        except:
            print("Found error")
    end = time.perf_counter()

    print(f"Year {year} finished in {round(end - start, 3)} seconds.")


pck.dump(game_ids, "march_madness/games/pck/game_ids.pck")