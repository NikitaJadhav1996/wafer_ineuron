import os
import pandas as pd
from sklearn.model_selection import train_test_split
import argparse
from data.get_data import args_yaml

def train_test_splits(config_name):
    config=args_yaml(config_name)

    raw_data_path=config['load_data']['raw_dataset_csv']
    split_size=config['split_data']['test_size']
    train_path=config['split_data']['train_path']
    test_path=config['split_data']['test_path']
    random_state=config['base']['random_state']

    data=pd.read_csv(raw_data_path,sep=',',encoding='utf-8')
    train,test=train_test_split(
        data,
        test_size=split_size,
        random_state=random_state,
    )

    train.to_csv(train_path,header=True,sep=',',encoding='utf-8')
    test.to_csv(test_path,header=True,sep=',',encoding='utf-8')
   # print(train.head())
   # print(test.shape)

if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    parsed_args=args.parse_args()
    train_test=train_test_splits(parsed_args.config)
    