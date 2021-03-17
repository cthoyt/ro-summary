# -*- coding: utf-8 -*-

"""Generates summaries of the relation ontology."""

import datetime
import os
from operator import itemgetter

import requests
import yaml
from tabulate import tabulate
from tqdm import tqdm

HERE = os.path.abspath(os.path.dirname(__file__))
DIRECTORY = os.path.join(HERE, 'docs', '_data')
os.makedirs(DIRECTORY, exist_ok=True)
TSV_PATH = os.path.join(HERE, 'summary.tsv')
YML_PATH = os.path.join(DIRECTORY, 'summary.yml')

# URL for the Wikidata SPARQL service
URL = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'

Q1 = '''
SELECT ?prop ?propLabel ?ro_id
WHERE  {
    ?prop wdt:P3590 ?ro_id .
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
'''


def get_query(query, base: str = URL):
    res = requests.get(
        base,
        params={'query': query, 'format': 'json'},
        headers={'User-Agent': f'ro-summary/1.0.0 (cthoyt@gmail.com)'},
    )
    res.raise_for_status()
    res_json = res.json()
    return res_json['results']['bindings']


header = ['wd', 'label', 'ro', 'count']


def main():
    results = get_query(Q1)

    rows = []
    for row in tqdm(results):
        wd_property = row['prop']['value'][len('http://www.wikidata.org/entity/'):]
        wd_property_label = row['propLabel']['value']
        ro_id = row['ro_id']['value']
        q2 = f'''
            SELECT (COUNT(*) as ?count)
            WHERE {{ ?sub wdt:{wd_property} ?obj }}
        '''
        triples_count_result = get_query(q2)
        triples_count = int(triples_count_result[0]['count']['value'])
        rows.append((wd_property, wd_property_label, ro_id, triples_count))

    # Sort descending
    rows = sorted(rows, key=itemgetter(3), reverse=True)

    total = sum(row[3] for row in rows)

    with open(TSV_PATH, 'w') as file:
        print(*header, sep='\t', file=file)
        for row in rows:
            print(*row, sep='\t', file=file)

    with open(YML_PATH, 'w') as file:
        yaml.safe_dump(
            {
                'total': total,
                'date': datetime.datetime.now().strftime('%Y-%m-%d'),
                'rows': [
                    dict(zip(header, row))
                    for row in rows
                ],
            },
            file,
        )

    print('Total RO annotations', total)
    print(tabulate(rows, headers=header))


if __name__ == '__main__':
    main()
