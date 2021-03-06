# -*- coding: utf-8 -*-

"""Save the relation ontology (RO) names as a TSV for lookup.

Since this script depends on PyOBO and downloading data, it's currently not included
in the GitHub action.
"""

import os

import pyobo

HERE = os.path.abspath(os.path.dirname(__file__))
PATH = os.path.join(HERE, 'names.tsv')


def main():
    id_name = pyobo.get_typedef_id_name_mapping('ro')
    with open(PATH, 'w') as file:
        print('id', 'name', sep='\t', file=file)
        print('BFO_0000050', 'part of', sep='\t', file=file)
        print('BFO_0000051', 'has part', sep='\t', file=file)
        for identifier, name in sorted(id_name.items()):
            print(f'RO_{identifier}', name, sep='\t', file=file)


if __name__ == '__main__':
    main()
