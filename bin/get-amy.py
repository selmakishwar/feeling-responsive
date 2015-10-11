#!/usr/bin/env python3

'''Fetch info about workshops, airports, etc. from AMY.'''

import sys
import urllib.request
import yaml

def main():
    '''
    Fetch information and store in one YAML file.
    '''

    # Controls.
    amy_url = sys.argv[1]
    output_file = sys.argv[2]

    # Information from AMY.
    config = {
        'badges' : fetch_info(amy_url, 'export/badges.yaml'),
        'airports' : fetch_info(amy_url, 'export/instructors.yaml'),
        'workshops' : fetch_info(amy_url, 'events/published.yaml')
    }

    # Coalesce flag information.
    for a in config['airports']:
        a['country'] = a['country'].lower()
    for w in config['workshops']:
        w['country'] = w['country'].lower()
    config['flags'] = {
        'workshops': sorted({w['country'] for w in config['workshops'] if w['country']}),
        'airports': sorted({a['country'] for a in config['airports'] if a['country']})
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


if __name__ == '__main__':
    main()
