import json
import os

files = os.listdir('games/ncb/boxscore')

out_file = open('game_data.csv', 'w')
columns = ['gameid','date','team1id','team1name','team1fgm', 'team1fga','team13pm','team13pa','team1ftm','team1fta','team1oreb','team1dreb','team1ast','team1stl','team1blk','team1to','team1fls','team2id','team2name','team2fgm','team2fga','team23pm','team23pa','team2ftm','team2fta','team2oreb','team2dreb','team2ast','team2stl','team2blk','team2to','team2fls',]
out_file.write(','.join(columns))
out_file.write('\n')

for file in files:
    with open('games/ncb/boxscore/' + file, 'r') as f:
        data = json.load(f)

    gameid = str(data['gameId'])

    data = data['gamepackageJSON']['boxscore']

    team1info = data['teams'][0]['team']
    team2info = data['teams'][1]['team']
    team1stats = data['teams'][0]['statistics']
    team2stats = data['teams'][1]['statistics']
    # print(team1stats)s

    if len(team1stats) > 0:
        team1id = team1info['id']
        team1name = team1info['slug']
        team1fg = team1stats[0]['displayValue']
        team1fgm, team1fga = team1fg.split('-')[0], team1fg.split('-')[1]
        team13p = team1stats[2]['displayValue']
        team13pm, team13pa = team13p.split('-')[0], team13p.split('-')[1]
        team1ft = team1stats[4]['displayValue']
        team1ftm, team1fta = team1ft.split('-')[0], team1ft.split('-')[1]
        team1oreb = team1stats[7]['displayValue']
        team1dreb = team1stats[8]['displayValue']
        team1ast = team1stats[10]['displayValue']
        team1stl = team1stats[11]['displayValue']
        team1blk = team1stats[12]['displayValue']
        team1to = team1stats[15]['displayValue']
        team1fls = team1stats[19]['displayValue']

        team2id = team2info['id']
        team2name = team2info['slug']
        team2fg = team2stats[0]['displayValue']
        team23p = team2stats[2]['displayValue']
        team2ft = team2stats[4]['displayValue']
        team2fgm, team2fga = team2fg.split('-')[0], team2fg.split('-')[1]
        team23pm, team23pa = team23p.split('-')[0], team23p.split('-')[1]
        team2ftm, team2fta = team2ft.split('-')[0], team2ft.split('-')[1]
        team2oreb = team2stats[7]['displayValue']
        team2dreb = team2stats[8]['displayValue']
        team2ast = team2stats[10]['displayValue']
        team2stl = team2stats[11]['displayValue']
        team2blk = team2stats[12]['displayValue']
        team2to = team2stats[15]['displayValue']
        team2fls = team2stats[19]['displayValue']

        info = [gameid,team1id,team1name,team1fgm,team1fga,team13pm,team13pa,team1ftm,team1fta,team1oreb,team1dreb,team1ast,team1stl,team1blk,team1to,team1fls,team2id,team2name,team2fg,team23p,team2ft,team2oreb,team2dreb,team2ast,team2stl,team2blk,team2to,team2fls,]
    else:
        info = [gameid]

    out_file.write(','.join(info) + '\n')

out_file.close()