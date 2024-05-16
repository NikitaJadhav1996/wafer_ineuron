import yaml
import pandas as pd
import argparse

class get_data:

    def __init__(self):
        pass
    
    def read_yaml(self,config_path):
        with open(config_path,'r') as config_file:
            config=yaml.safe_load(config_file)
        return config

    def get_data(self,config):
        data_path=config['data_source']['s3_source']
        data=pd.read_csv(data_path,sep=',',encoding='utf-8')
        return data

if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    arg_parse=args.parse_args()
    retrieve_data=get_data()
    config=retrieve_data.read_yaml(arg_parse.config)
    data=retrieve_data.get_data(config)
    print(data)
    