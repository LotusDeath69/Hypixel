import requests
import datetime
from secrets import api
name = 'ThatBananaKing'


def uuid(ign):
    try:
        data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}').json()
        return data['id']
    except ValueError:
        print('Invalid username \nPlease try again')
        exit()


def stats(ign, key):
    if ign.lower() == 'thatbananaking':
        return ThatBananaKing()
    data = requests.get(f'https://api.hypixel.net/player?key={key}&uuid={uuid(ign)}').json()
    unix_time_first_joined = data['player']['firstLogin']
    normal_time_first_joined = datetime.datetime.fromtimestamp(unix_time_first_joined/1000.0)
    unix_time_last_joined = data['player']['lastLogin']
    normal_time_last_joined = datetime.datetime.fromtimestamp(unix_time_last_joined/1000.0)

    achievement_points =  data['player']['achievementPoints']
    karma = data['player']['karma']
    rank = getRank(data)
    current_level = getLevel(data['player']['networkExp'])
    current_guild = getGuild(ign, key)
    friend = getFriend(ign, key)
    status = getStatus(ign, key)
    return f'Rank: {rank} Guild: {current_guild} Status: {status} Friends: {friend} Level: {current_level} Achievement Point: {achievement_points} Karma: {karma} '\
    f'First Join: {normal_time_first_joined} Last Joined: {normal_time_last_joined}'


def getRank(data):
    try:
        if data['player']['monthlyPackageRank'] == 'none':
            rank = data['player']['newPackageRank']
    
        else: 
            rank = data['player']['monthlyPackageRank']
    except KeyError:
        return 'non'
    
    if rank == 'SUPERSTAR':
        return 'MVP ++'
    if rank == 'MVP_PLUS':
        return 'MVP +'
    if rank == 'VIP_PLUS':
        return 'VIP +'
    return rank


def getLevel(exp):
    next_level = 10_000
    level = 1
    for _ in range(1000):
        if exp < next_level:
            return level
        else:
            exp -= next_level
            next_level += 2_500
            level += 1


def getGuild(ign, key):
    try:
        data = requests.get(f'https://api.hypixel.net/findGuild?key={key}&byUuid={uuid(ign)}').json()
        guild = requests.get(f'https://api.hypixel.net/guild?key={key}&id={data["guild"]}').json()
        return guild['guild']['name']
    except KeyError:
        return f'{ign} is not currently in a guild.'


def getFriend(ign, key):
    data = requests.get(f'https://api.hypixel.net/friends?key={key}&uuid={uuid(ign)}').json()
    return len(data['records'])


def getStatus(ign, key):
    data = requests.get(f'https://api.hypixel.net/status?key={key}&uuid={uuid(ign)}').json()
    if data['session'] is True:
        return 'online'
    else:
        return 'offline'


def ThatBananaKing():
    return 'rank: Banana Guild: Lunar Guard Friends: 45 Level: 420 Achievement Points: 6969 Status: ¯\_(ツ)_/¯'
    

print(stats(name, api))
