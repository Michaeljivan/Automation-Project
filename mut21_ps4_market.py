# MUTHEAD WEB SCRAPPER
# SCRIPT TO GET CHEAPEST CARDS AT BEST RATES

import requests

from bs4 import BeautifulSoup

ps4_80 = 'https://www.muthead.com/21/players/?overall__gte=80&overall__lte=80&price_platform=2&sort_by=summary_price'
ps4_81 = 'https://www.muthead.com/21/players/?overall__gte=81&overall__lte=81&price_platform=2&sort_by=summary_price'
ps4_82 = 'https://www.muthead.com/21/players/?overall__gte=82&overall__lte=82&price_platform=2&sort_by=summary_price'
ps4_83 = 'https://www.muthead.com/21/players/?overall__gte=83&overall__lte=83&price_platform=2&sort_by=summary_price'
ps4_84 = 'https://www.muthead.com/21/players/?overall__gte=84&overall__lte=84&price_platform=2&sort_by=summary_price'
ps4_85 = 'https://www.muthead.com/21/players/?overall__gte=85&overall__lte=85&price_platform=2&sort_by=summary_price'
ps4_86 = 'https://www.muthead.com/21/players/?overall__gte=86&overall__lte=86&price_platform=2&sort_by=summary_price'
ps4_87 = 'https://www.muthead.com/21/players/?overall__gte=87&overall__lte=87&price_platform=2&sort_by=summary_price'
ps4_88 = 'https://www.muthead.com/21/players/?overall__gte=88&overall__lte=88&price_platform=2&sort_by=summary_price'
ps4_89 = 'https://www.muthead.com/21/players/?overall__gte=89&overall__lte=89&price_platform=2&sort_by=summary_price'
ps4_90 = 'https://www.muthead.com/21/players/?overall__gte=90&overall__lte=91&price_platform=2&sort_by=summary_price'
ps4_91 = 'https://www.muthead.com/21/players/?overall__gte=91&overall__lte=91&price_platform=2&sort_by=summary_price'
ps4_92 = 'https://www.muthead.com/21/players/?overall__gte=92&overall__lte=92&price_platform=2&sort_by=summary_price'
ps4_93 = 'https://www.muthead.com/21/players/?overall__gte=93&overall__lte=93&price_platform=2&sort_by=summary_price'

most_feared_ = 'https://www.muthead.com/21/players/?overall__gte=85&overall__lte=92&price_platform=2&program=176&sort_by=summary_price'


# print("Search in progress...")

# PS4 Elite Cards

def getRequest(cardOvr, ovr):
    response_card = requests.get(cardOvr)
    player_text_html = BeautifulSoup(response_card.text, "html.parser")

    cheapest_player_price = player_text_html.find("div", {"class": "player-listing__price-value"})
    cheapest_player_name = player_text_html.find("div", {"class": "list-info-player__player-name"})
    cheapest_player_info = player_text_html.find("div", {"class": "list-info-player__player-info"})

    print(str(ovr) + "-> " + cheapest_player_name.string + " \t" + cheapest_player_price.string + " " + cheapest_player_info.string)

ovr_request = input("Enter Ovr or string: ")
print("Finding cheapest " + ovr_request + "\n")
if(ovr_request == 'most feared'):
    getRequest(most_feared_, 0)
elif(ovr_request == '80'):
    getRequest(ps4_80, 80)  
elif(ovr_request == '81'):
    getRequest(ps4_81, 81)
elif(ovr_request == '82'):
    getRequest(ps4_82, 82)
elif(ovr_request == '83'):
    getRequest(ps4_83, 83)
elif(ovr_request == '84'):
    getRequest(ps4_84, 84)
elif(ovr_request == '85'):
    getRequest(ps4_85, 85)
elif(ovr_request == '86'):
    getRequest(ps4_86, 86)
elif(ovr_request == '87'):
    getRequest(ps4_87, 87)
elif(ovr_request == '88'):
    getRequest(ps4_88, 88)
elif(ovr_request == '89'):
    getRequest(ps4_89, 89)
elif(ovr_request == '90'):
    getRequest(ps4_90, 90)
elif(ovr_request == '91'):
    getRequest(ps4_91, 91)
elif(ovr_request == '92'):
    getRequest(ps4_92, 92)
elif(ovr_request == '93'):
    getRequest(ps4_93, 93)
else:
    print("incorrect overall must be in range from 80-93")