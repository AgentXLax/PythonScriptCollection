import requests
import json

#scrape data from nhl's stats api to obtain scores for all games

##todaysDate = '2018-10-28'    

##url = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate={0}&endDate={0}'.format(todaysDate)
##statsDict = requests.get(url).text
##statsDict = json.loads(statsDict)
##gamesList = statsDict['dates'][0]['games']
##
##totalHomes = 0
##totalAways = 0
##for i in range(len(gamesList)):
##    homeScore = gamesList[i]['teams']['home']['score']
##    awayScore = gamesList[i]['teams']['away']['score']
##    totalHomes += homeScore
##    totalAways += awayScore
##    teamNameHome = gamesList[i]['teams']['home']['team']['name']
##    teamNameAway = gamesList[i]['teams']['away']['team']['name']
##    print('game',i+1,teamNameHome+':', homeScore,teamNameAway+':',awayScore)
##print (totalHomes, totalAways, totalHomes + totalAways, totalHomes-totalAways)

##Turn the above into a method for a class, make this a full-fledged
##settlement calculator

class Settlements():

    def __init__(self, date):
        self.date = date
        self.url = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate={0}&endDate={0}'.format(date)
        self.statsDict = json.loads(requests.get(self.url).text)
        gamesList = self.statsDict['dates'][0]['games']
        self.homesList = []
        self.awaysList = []
        self.gameState = []
        for i in range(len(gamesList)):
            homeDetails = gamesList[i]['teams']['home']
            awayDetails = gamesList[i]['teams']['away']

            homeDetails.pop('leagueRecord')
            awayDetails.pop('leagueRecord')
            
            self.homesList.append(homeDetails)
            self.awaysList.append(awayDetails)
            
            self.gameState.append(gamesList[i]['status']['abstractGameState'])
            
        self.gamesList = zip(zip(self.homesList,self.awaysList),self.gameState)

##Something that settles the score of individual games
        
    def __repr__(self):
        aStr = 'Games That Were Played on {}:\n'.format(self.date)
##        for i in range(len(self.awaysList)):
##            aStr +='{} at {} status: {}\n'\
##            .format(self.awaysList[i]['team']['name'],\
##                    self.homesList[i]['team']['name'],\
##                    self.gameState[i])
        for i, item in enumerate(self.gamesList):
            ##item[1] is the game state
            ##item[0][0] = home team directory, item[0][1] = away team directory
            aStr += '{} vs. {} score: {}-{} Game Status: {}\n'.format(item[0][0]['team']['name'],item[0][1]['team']['name'],item[0][0]['score'],item[0][1]['score'],item[1])
        return aStr

print(Settlements('2018-10-28'))
        
