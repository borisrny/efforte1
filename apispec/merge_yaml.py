#!/usr/bin/env python3
import yaml


def merge_dict(source, destination):
    for key, value in list(source.items()):
        if isinstance(value, dict):
            # get node or create one
            node = destination.setdefault(key, {})
            merge_dict(value, node)
        else:
            destination[key] = value

    return destination


def load_config(fn):
    with open(fn, 'r') as ymlfile:
        cnf = yaml.load(ymlfile)
    for inc in cnf.get('include', []):
        print('Appending: {}'.format(inc))
        cnf = merge_dict(cnf, yaml.load(open(inc)))
    return cnf


if __name__ == '__main__':
    cnf = load_config('base.yaml')
    with open('swagger.yaml', 'w') as ymlfile:
        yaml.dump(cnf, ymlfile)

