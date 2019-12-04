import requests
import time
import os
import random 

SLACK_URL=os.environ['SLACK_URL']

SLACK_CHANNEL = "#code_testing"

if SLACK_CHANNEL in os.environ:
    SLACK_CHANNEL = os.environ['SLACK_CHANNEL']

print (SLACK_CHANNEL)

def get_chucknorris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    category_url = "https://api.chucknorris.io/jokes/categories"
    response = requests.get(category_url)
    category_list = response.json()
    category = random.choice(category_list)
    # if category != "":
    url = url + "?category=" + category
    response = requests.get(url)
    data = response.json()
    return data


pictures = [
            "https://cdn.dribbble.com/users/1590794/screenshots/6365359/dribbble_shot_hd.png",
            "https://www.clipartmax.com/png/middle/269-2697353_chuck-norris-chuck-norris-birthday-card.png",
            "https://cdn3.movieweb.com/i/article/fOrOnyvPBPzDYIjPJ9Ww48aqSMOtD0/798:50/Chuck-Norris-Photo-Intimidation-Quebec-City-Police-Department.jpg",
            "http://ppcorn.com/us/wp-content/uploads/sites/14/2016/01/Chuck-Norris-art-ppcorn.jpg",
            "https://www.designer-daily.com/wp-content/uploads/2008/03/chuck-norris.jpg",
            "https://mir-s3-cdn-cf.behance.net/project_modules/fs/c56a9621909647.563097c296e05.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTdl2yIc_B9uiMyJe-lfGUWbqpqJI5erKapm1rQTgCehgy_fvYV",
            "https://images.fineartamerica.com/images-medium-large/chuck-norris-i-counted-to-infinity-twice-yvan-goudard.jpg",
            "https://thumbnails.texastribune.org/vSWj02G-XIofkH6IG6KhfwH6Xuo=/850x570/smart/filters:quality(80)/https://static.texastribune.org/media/images/chuck-norris1.jpg",
            "https://cdn.dribbble.com/users/32658/screenshots/6377976/chuck1.jpg",
            "https://i.kym-cdn.com/photos/images/original/000/166/876/chuck-norris-thumbs-up.jpg"
            ]

def send_joke(joke):



    fields = []
    for categorie in joke["categories"]:
         print(categorie)
         fields.append(
             {
                 "title": "Category",
                 "value": categorie,
                 "short": False
             },
         )
    fields.append(
        {
            "title": "Joke itself",
            "value": joke['value'],
            "short": True
        }
    )
    data = {
         # extas - start
        "channel": SLACK_CHANNEL,
        "username": "Chuck Norris",
        #"icon_emoji": "https://cdn.dribbble.com/users/382712/screenshots/4165164/chuck_norris.png",
        "icon_url": "https://story.projectsemicolon.com/wp-content/uploads/sites/10/2018/11/Cnorris.png",
        # extras - enda
        "attachments": [
            {
                "mrkdwn_in": ["text"],
                "color": "#ffc0cb",
                "author_name": "Chuck Bot",
                "author_link": "https://chucknorris.com/",
                "author_icon": "https://cdn.dribbble.com/users/382712/screenshots/4165164/chuck_norris.png",
            
               
                "fields":fields,



                #"fields": [
                    #{
                        #"title": "Joke category",
                        #"value": joke['categories'][0],
                        #"short": False
                    #},
                    #{
                        #"title": "Joke itself",
                        #"value": joke['value'],
                        #"short": True
                    #}
                #],

                # "thumb_url": "https://images02.military.com/sites/default/files/styles/full/public/media/veteran-jobs/content-images/2016/03/chucknorris.jpg?itok=_J3M4O-S",

                "thumb_url": random.choice(pictures),
                "footer": "norris",
                "footer_icon": "http://www.8bit-ninja.de/versinator/images/8bit_chuck_norris_l.gif",
                "ts": int(time.time())
            }
        ]
    }



    requests.post(SLACK_URL, json=data)



jk=get_chucknorris_joke()
print(jk['value'])
print(random.choice(pictures))
#print(jk['categories'][0])
send_joke(jk)
