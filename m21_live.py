from datetime import datetime
import webbrowser

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

today6a = now.replace(hour=6, minute=0, second=0, microsecond=0)
today730a = now.replace(hour=7, minute=30, second=0, microsecond=0)
today8a = now.replace(hour=8, minute=0, second=0, microsecond=0)
today9a = now.replace(hour=9, minute=0, second=0, microsecond=0)
today10a = now.replace(hour=10, minute=00, second=0, microsecond=0)
today12p = now.replace(hour=12, minute=00, second=0, microsecond=0)
today2p = now.replace(hour=14, minute=00, second=0, microsecond=0)
today3p = now.replace(hour=15, minute=00, second=0, microsecond=0)
today4p = now.replace(hour=16, minute=00, second=0, microsecond=0)
today5p = now.replace(hour=17, minute=00, second=0, microsecond=0)
today6p = now.replace(hour=18, minute=00, second=0, microsecond=0)
today8p = now.replace(hour=20, minute=00, second=0, microsecond=0)
today9p = now.replace(hour=21, minute=00, second=0, microsecond=0)

day = datetime.today().weekday()
print("Day of Week =", day)

# Monday
if(day == 0):
    if(now >= today730a and now <= today8a):
        # 7:30-8:00a
        webbrowser.open('https://twitch.tv/eamaddennfl')
    elif(now >= today8a and now <= today10a):
        # 8-10a
        webbrowser.open('https://twitch.tv/')
    elif(now >= today4p and now <= today6p):
        # 4-6p
        webbrowser.open('https://twitch.tv/')
    elif(now >= today6p and now <= today8p):
        # 6-8p
        webbrowser.open('https://twitch.tv/')

# Tuesday
if(day == 1):
    if(now >= today730a and now <= today8a):
        # 7:30-8:00
        webbrowser.open('https://twitch.tv/eamaddennfl')   
    elif(now >= today8a and now <= today10a):
        # 8-10a
        webbrowser.open('https://twitch.tv')
    elif(now >= today3p and now <= today5p):
        # 3-5p
        webbrowser.open('https://twitch.tv/')
    elif(now >= today5p and now <= today8p):
        # 5-8p Derwin vs the world
        webbrowser.open('https://twitch.tv/eamaddennfl')

# Wednesday
if(day == 2):
    if(now >= today730a and now <= today8a):
        # 7:30-8:00
        webbrowser.open('https://twitch.tv/eamaddennfl')
    elif(now >= today8a and now <= today10a):
        # 8-10a
        webbrowser.open('https://twitch.tv/')
    elif(now >= today4p and now <= today6p):
        # 4-6p
        webbrowser.open('https://twitch.tv/')
    elif(now >= today6p and now <= today8p):
        # 6-8p
        webbrowser.open('https://twitch.tv/')

# Thursday
if(day == 3):
    if(now >= today730a and now <= today8a):
        # 7:30-8:00a
        webbrowser.open('https://twitch.tv/eamaddennfl')
    elif(now >= today8a and now <= today10a):
        # 8-10a
        webbrowser.open('https://twitch.tv/')
    elif(now >= today4p and now <= today6p):
        # 4-6p
        webbrowser.open('https://twitch.tv/')
    elif(now >= today6p and now <= today8p):
        # 6-8p
        webbrowser.open('https://twitch.tv/')

# Friday
if(day == 4):
    if(now >= today730a and now <= today8a):
        # 7:30-8:00a
        webbrowser.open('https://twitch.tv/eamaddennfl')
    elif(now >= today8a and now <= today10a):
        # 8-10a
        webbrowser.open('https://twitch.tv/zanmadden')
        webbrowser.open('https://twitch.tv/chewbaccal')
    elif(now >= today10a and now <= today12p):
        # 10-12p
        webbrowser.open('https://twitch.tv/digitalchampion')
        webbrowser.open('https://twitch.tv/dgrizzletv')
    elif(now >= today12p and now <= today2p):
        #12-2p
        webbrowser.open('https://twitch.tv/cjsaucee')
        webbrowser.open('https://twitch.tv/trumpetmonkey')
    elif(now >= today2p and now <= today4p):
        #2-4p
        webbrowser.open('https://twitch.tv/shopmastertv')
        webbrowser.open('https://twitch.tv/drsteinman')
    elif(now >= today4p and now <= today6p):
        #4-6p
        webbrowser.open('https://twitch.tv/jayduhbb')
        webbrowser.open('https://twitch.tv/kmac')
    elif(now >= today6p and now <= today9p):
        #6-9p
        webbrowser.open('https://twitch.tv/ryno')
        webbrowser.open('https://twitch.tv/wintgoat')

# Saturday
if(day == 5):
    if(now >= today6a and now <= today8a):
        # 6-8a
        webbrowser.open('https://twitch.tv/retroyimmy')
        webbrowser.open('https://twitch.tv/laurenwkr')
    elif(now >= today8a and now <= today10a):
        # 8-10
        webbrowser.open('https://twitch.tv/jayduhbb')
        webbrowser.open('https://twitch.tv/chewbaccal')
    elif(now >= today10a and now <= today12p):
        # 10-12
        webbrowser.open('https://twitch.tv/swain_games')
        webbrowser.open('https://twitch.tv/trumpetmonkey')
    elif(now >= today12p and now <= today2p):
        #12-2
        webbrowser.open('https://twitch.tv/drgrizzletv')
        webbrowser.open('https://twitch.tv/drsteinman')
    elif(now >= today2p and now <= today4p):
        #2-4
        webbrowser.open('https://twitch.tv/buffalokaay')
        webbrowser.open('https://twitch.tv/ryno')
    elif(now >= today4p and now <= today6p):
        #4-6p
        webbrowser.open('https://twitch.tv/fendler')
        webbrowser.open('https://twitch.tv/xpopularstranger')
    elif(now >= today6p and now <= today9p):
        #6-9p
        webbrowser.open('https://twitch.tv/shopmastertv')
        webbrowser.open('https://twitch.tv/dk_nice1')

# Sunday
if(day == 6):
    if( now >= today6a and now <= today8a):
        # 6-8a
        webbrowser.open('https://twitch.tv/thatduded3v')
        webbrowser.open('https://twitch.tv/cjsaucee')
    elif(now >= today8a and now <= today10a):
        # 8-10
        webbrowser.open('https://twitch.tv/stiff')
        webbrowser.open('https://twitch.tv/4thqtrgaming')