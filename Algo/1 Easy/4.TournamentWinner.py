def tournamentWinner(competitions, results):
    scores = {}
    for i in range(len(competitions)):
        home_team, away_team = competitions[i]
        result = results[i]
        winning_team = home_team if result == 1 else away_team

        if winning_team not in scores:
            scores[winning_team] = 0
        scores[winning_team] += 3

    winner = max(scores, key=scores.get)
    return winner

def tournamentWinner2(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for i in range(len(competitions)):
        home_team, away_team = competitions[i]
        result = results[i]
        winning_team = home_team if result == 1 else away_team

        if winning_team not in scores:
            scores[winning_team] = 0
        scores[winning_team] += 3

        if scores[winning_team] > scores[currentBestTeam]:
            currentBestTeam = winning_team

    return currentBestTeam