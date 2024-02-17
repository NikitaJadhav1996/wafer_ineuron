import os
import argparse
import yaml
import logging

def read_args(config_path):
    with open(config_path) as yamlfile:
        config_arg= yaml.safe_load(yamlfile)
    return config_arg

def main(config_path,data_source):
    config=read_args(config_path)
    print(config)

if __name__=='__main__':
    args=argparse.ArgumentParser()
    default_config_path=os.path.join('config','params.yaml')
    args.add_argument('--config',default=default_config_path)
    args.add_argument('--data_source',default=None)

    parser=args.parse_args()
    main(config_path=parser.config,data_source=parser.data_source)