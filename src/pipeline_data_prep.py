import os
import argparse
import yaml
import logging


if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config',default='default')
    args.add_argument('--arg1',default=None)

    parser=args.parse_args()
    print(parser.arg1, parser.config)