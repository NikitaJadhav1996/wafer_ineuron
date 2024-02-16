import subprocess
from glob import glob

data_dirs=['Training_Batch_Files','Prediction_Batch_Files']

for files in data_dirs:
    correct_files=glob(files + r"/*.csv")
  #  print(correct_files)
    for file_path in correct_files:
        dvc_add_command=['dvc','add',file_path]
        subprocess.run(dvc_add_command,shell=True)
       # formatted_file_path = file_path.replace("\", "\\")
       # print(file_path)
     #   os.system(f'dvc add{file_path}')

print("\n #### all files added to dvc ####")