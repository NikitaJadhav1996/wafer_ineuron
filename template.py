import os

dirs=[
    os.path.join('data','raw'),
    os.path.join('data','processed'),
    'notebooks',
    'models',
    'src'
]

for i in dirs:
    os.makedirs(i,exist_ok=True)
    with open(os.path.join(i,'.gitkeep'),'w') as ff:
        pass

files=[
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join('src','__init__.py')
]

for j in files:
    with open(j,'w') as w:
        pass
