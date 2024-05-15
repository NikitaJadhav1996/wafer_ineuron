import os

dirs=[
    'data_prep',
    'models',
    'tests'
]

for i in dirs:
    os.makedirs(i,exist_ok=True)
    try:
        with open(os.path.join(i,'.gitkeep'),'w') as f:
            pass
    except FileNotFoundError as e:
        print(f'FILE ERROR:---{e}')

files=[
    'setup.py',
    'dvc.yaml',
    '.gitignore',
    os.path.join('data_prep','__init__.py')
]

for f in files:
    try:
        with open(f,'w') as f:
            pass
    except FileNotFoundError as fe:
        print(fe)