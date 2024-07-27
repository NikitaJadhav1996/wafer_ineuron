import os
import argparse
import pandas as pd
from get_data import args_yaml, load_args

def preprocess_data(config_name):
    config=args_yaml(config_name)
    data=load_args(config_name)
    cols=[cols.replace(' ','_') for cols in data.columns]
    raw_path=config['load_data']['raw_dataset_csv']
    data.to_csv(raw_path,header=cols,sep=',')
 #   print(data.head())


if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    parsed_args=args.parse_args()
    data_prep=preprocess_data(parsed_args.config)
    #print(data_prep)
