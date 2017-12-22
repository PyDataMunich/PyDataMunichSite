import requests
import bs4
url = 'https://api.meetup.com/SuperPythonTalks/events?&sign=true&photo-host=public&page=200&status=past'
r = requests.get(url)

article_template = """title: {title}
slug: {slug}
category: general
date: {date}
modified: {date}

{description}

Total Attendees: {count}
Event Link: {link}

"""


if r.ok:
    events = r.json()
    for idx, event in enumerate(events):

        try:
            slug = event['name'].split(':')[1].replace(' ', '_').replace('"', '').lower()[1:]
        except:
            slug = 'event{}'.format(idx)

        with open('testcontent/page{}.md'.format(idx), 'w') as f:
            f.write(article_template.format(title=event['name'],
            slug=slug,
            description='\n\n'.join(bs4.BeautifulSoup(event['description']).stripped_strings),
            link=event['link'],
            count=event['yes_rsvp_count'],
            date=event['local_date'],
            ))
        print(event)
