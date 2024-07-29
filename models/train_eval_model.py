import os
import argparse
import numpy as np
import pandas as pd
import json
import joblib
import warnings 
import sys

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet

sys.path.append(r'C:\Users\Nikita\MLOPS_PYTHON')

from data.get_data import args_yaml

def eval_model_metrics(actual,pred):
    rmse=np.sqrt(mean_squared_error(actual,pred))
    mae=mean_absolute_error(actual,pred)
    r2=r2_score(actual,pred)
    return rmse,mae,r2


def train_model(config_name):
    config=args_yaml(config_name)
    train_path=config['split_data']['train_path']
    test_path=config['split_data']['test_path']
    
    model_dir=config['model_dir']
    alpha=config['estimators']['ElasticNet']['params']['alpha']
    l1_ratio=config['estimators']['ElasticNet']['params']['l1_ratio']
    random_state=config['base']['random_state']

    params=config['reports']['params']
    scores=config['reports']['scores']
    target=config['base']['target_col']

    train=pd.read_csv(train_path,sep=',',encoding='utf-8')
    test=pd.read_csv(test_path,sep=',',encoding='utf-8')
    
    train_y=train[target]
    test_y=test[target]

    train_x=train.drop(target,axis=1)
    test_x=test.drop(target,axis=1)

    model_en=ElasticNet(
        alpha=alpha,
        l1_ratio=l1_ratio,
        random_state=random_state
    )

    model_en.fit(train_x,train_y)

    pred=model_en.predict(test_x)

    (rmse,mae,r2)=eval_model_metrics(test_y,pred)

    print(rmse,mae,r2)

    os.makedirs(os.path.join('models','reports'),exist_ok=True)
    scores_path=os.path.join('models','reports',scores)
    params_path=os.path.join('models','reports',params)

    with open(scores_path,'w') as f:
        scores={
            'rmse':rmse,
            'mae':mae,
            'r2':r2
        }
        json.dump(scores,f,indent=4)

    with open(params_path,'w') as f:
        params={
            'l1_ratio':l1_ratio,
            'alpha':alpha
        }
        json.dump(params,f,indent=4)

    os.makedirs(model_dir,exist_ok=True)
    model_path=os.path.join(model_dir,'model.joblib')

    joblib.dump(model_en,model_path)


if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    parsed_args=args.parse_args()
    training=train_model(parsed_args.config)
  #  print(training)
        