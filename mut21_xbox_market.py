# MUTHEAD WEB SCRAPPER
# SCRIPT TO GET CHEAPEST CARDS AT BEST RATES

import requests

from bs4 import BeautifulSoup

xbox_80 = 'https://www.muthead.com/21/players/?overall__gte=80&overall__lte=80&price_platform=1&sort_by=summary_price'
xbox_81 = 'https://www.muthead.com/21/players/?overall__gte=81&overall__lte=81&price_platform=1&sort_by=summary_price'
xbox_82 = 'https://www.muthead.com/21/players/?overall__gte=82&overall__lte=82&price_platform=1&sort_by=summary_price'
xbox_83 = 'https://www.muthead.com/21/players/?overall__gte=83&overall__lte=83&price_platform=1&sort_by=summary_price'
xbox_84 = 'https://www.muthead.com/21/players/?overall__gte=84&overall__lte=84&price_platform=1&sort_by=summary_price'
xbox_85 = 'https://www.muthead.com/21/players/?overall__gte=85&overall__lte=85&price_platform=1&sort_by=summary_price'
xbox_86 = 'https://www.muthead.com/21/players/?overall__gte=86&overall__lte=86&price_platform=1&sort_by=summary_price'
xbox_87 = 'https://www.muthead.com/21/players/?overall__gte=87&overall__lte=87&price_platform=1&sort_by=summary_price'
xbox_88 = 'https://www.muthead.com/21/players/?overall__gte=88&overall__lte=88&price_platform=1&sort_by=summary_price'
xbox_89 = 'https://www.muthead.com/21/players/?overall__gte=89&overall__lte=89&price_platform=1&sort_by=summary_price'


print("Search in progress...")

# Xbox Elite Cards

def getRequest(cardOvr, ovr):
    response_card = requests.get(cardOvr)
    player_text_html = BeautifulSoup(response_card.text, "html.parser")

    cheapest_player_price = player_text_html.find("div", {"class": "player-listing__price-value"})
    cheapest_player_name = player_text_html.find("div", {"class": "list-info-player__player-name"})
    cheapest_player_info = player_text_html.find("div", {"class": "list-info-player__player-info"})

    print(str(ovr) + "-> " + cheapest_player_name.string + " \t" + cheapest_player_price.string + " " + cheapest_player_info.string)


getRequest(xbox_80, 80)
getRequest(xbox_81, 81)
# getRequest(xbox_82, 82)
getRequest(xbox_83, 83)
getRequest(xbox_84, 84)
getRequest(xbox_85, 85)
getRequest(xbox_86, 86)
# getRequest(xbox_87, 87)
getRequest(xbox_88, 88)
getRequest(xbox_89, 89)