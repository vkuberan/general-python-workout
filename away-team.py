teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print("[Home Team: {} (vs) Away Team: {} ]".format(
                home_team, away_team))
