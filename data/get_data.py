# read params
# process
# returns the dataframe

import os
import yaml
import pandas as pd
import argparse

def args_yaml(config_file_name):
    with open(config_file_name) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config

def load_args(config_file_name):
    params=args_yaml(config_file_name)
    data_path=params['data_source']['s3_source']
    data=pd.read_csv(data_path,sep=',',encoding='utf-8')
    return data


        
if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    config_file_name=args.parse_args()
    print(str(config_file_name))
    read_params=args_yaml(config_file_name.config)
    load_arguments=load_args(config_file_name.config)
    print(load_arguments)