#!/usr/bin/env python3

'''Fetch info about workshops, airports, etc. from AMY.'''

import sys
import time
import datetime
import urllib.request
import yaml

def main():
    '''
    Fetch information and store in one YAML file.
    '''

    # Controls.
    amy_url = sys.argv[1]
    output_file = sys.argv[2]

    # Get information from AMY.
    config = {
        'timestamp' : time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'badges' : fetch_info(amy_url, 'export/badges.yaml'),
        'airports' : fetch_info(amy_url, 'export/instructors.yaml'),
        'workshops' : fetch_info(amy_url, 'events/published.yaml')
    }

    # Add more data.
    mark_workshops(config['workshops'], datetime.date.today())

    # Coalesce flag information.
    config['flags'] = {
        'workshops': sort_flags(config['workshops']),
        'airports': sort_flags(config['airports'])
    }

    # Save.
    with open(output_file, 'w') as writer:
        yaml.dump(config, writer, encoding='utf-8', allow_unicode=True)


def fetch_info(base_url, url):
    '''Download and save data.'''

    address = base_url + url
    with urllib.request.urlopen(address) as f:
        content = f.read()
    return yaml.load(content.decode('utf-8'))


def mark_workshops(workshops, today):
    '''Mark workshops as past or future.'''

    for w in workshops:
        w['_is_upcoming'] = w['start'] >= today
        w['_is_past'] = not w['_is_upcoming']


def sort_flags(data):
    '''Create sorted list of unique flags, lower-casing as a side effect.'''

    for entry in data:
        entry['country'] = entry['country'].lower()
    return sorted({entry['country'] for entry in data if entry['country']})


if __name__ == '__main__':
    main()
