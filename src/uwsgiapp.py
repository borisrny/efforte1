import logging

from src.service import create_app
import argparse

from src.util.conf import util_init_config

parser = argparse.ArgumentParser(description='GFE Server.')
parser.add_argument("--config", "-c", help="configuration file")
args = parser.parse_args()
cnf = util_init_config(args.config)
app = create_app()

