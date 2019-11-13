import requests
import time
import os

SLACK_URL=os.environ['SLACK_URL']

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
                "thumb_url": "https://images02.military.com/sites/default/files/styles/full/public/media/veteran-jobs/content-images/2016/03/chucknorris.jpg?itok=_J3M4O-S",
                "footer": "norris",
                "footer_icon": "http://www.8bit-ninja.de/versinator/images/8bit_chuck_norris_l.gif",
                "ts": int(time.time())
            }
        ]
    }



    requests.post(SLACK_URL, json=data)



jk=get_chucknorris_joke()
print(jk['value'])
#print(jk['categories'][0])
send_joke(jk)
