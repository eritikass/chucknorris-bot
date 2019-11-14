import requests
import time
import os
import random

SLACK_URL=os.environ['SLACK_URL']
pictures = [
            "https://cdn.dribbble.com/users/1590794/screenshots/6365359/dribbble_shot_hd.png",
            "https://www.clipartmax.com/png/middle/269-2697353_chuck-norris-chuck-norris-birthday-card.png",
            "https://cdn3.movieweb.com/i/article/fOrOnyvPBPzDYIjPJ9Ww48aqSMOtD0/798:50/Chuck-Norris-Photo-Intimidation-Quebec-City-Police-Department.jpg",
            "http://ppcorn.com/us/wp-content/uploads/sites/14/2016/01/Chuck-Norris-art-ppcorn.jpg",
            "https://www.designer-daily.com/wp-content/uploads/2008/03/chuck-norris.jpg",
            "https://mir-s3-cdn-cf.behance.net/project_modules/fs/c56a9621909647.563097c296e05.jpg",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTdl2yIc_B9uiMyJe-lfGUWbqpqJI5erKapm1rQTgCehgy_fvYV",
            "https://images.fineartamerica.com/images-medium-large/chuck-norris-i-counted-to-infinity-twice-yvan-goudard.jpg"
            ]

def get_chucknorris_joke(category=""):
    url = "https://api.chucknorris.io/jokes/random"
    if category != "":
        url = url + "?category=" + category
    response = requests.get(url)
    data = response.json()
    return data


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
        "attachments": [
            {
                "mrkdwn_in": ["text"],
                "color": "#ffc0cb",
                "author_name": "Chuck Bot",
                "author_link": "https://chucknorris.com/",
                "author_icon": "https://cdn.dribbble.com/users/382712/screenshots/4165164/chuck_norris.png",
                "title": "It's this time of the day",
                "title_link": "https://chuck-norris-jokes.com",
                "text": "Prepare your `pants` lads",
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
                #"thumb_url": "https://images02.military.com/sites/default/files/styles/full/public/media/veteran-jobs/content-images/2016/03/chucknorris.jpg?itok=_J3M4O-S",
                "thumb_url":random.choice(pictures),
                "footer": "norris",
                "footer_icon": "http://www.8bit-ninja.de/versinator/images/8bit_chuck_norris_l.gif",
                "ts": int(time.time())
            }
        ]
    }



    requests.post(SLACK_URL, json=data)



jk=get_chucknorris_joke('history')
print(jk['value'])
print(random.choice(pictures))
#print(jk['categories'][0])
send_joke(jk)
