import os
import re
import shutil




for file in os.scandir('.'):
    
    if file.is_dir():
        print(file.path)
        with open(f'{file.path}/model.config', 'r') as f:
            sdf = f.read()

        with open(f'{file.path}/model.config', 'w') as f:
            f.write(
                sdf.replace('X1-Y1-Z2', file.path[2:])
            )


'''
for file in os.scandir('.'):
    
    if file.is_file() and '.stl' in file.path :
        block_name = file.path[2:-4].lower()
        
        os.mkdir(block_name)
        os.mkdir(f'{block_name}/meshes')

        shutil.copyfile(file.path, f'{block_name}/meshes/{block_name.upper()}.stl')

        with open('./x1-y1-z2/model.config', 'r') as f:

            with open(f'{block_name}/model.config', 'w+') as model:
                model.write(f.read().replace('X1-Y1-Z2', block_name.upper()))

        with open('./x1-y1-z2/model.sdf', 'r') as f:
            
            
            with open(f'{block_name}/model.sdf', 'w+') as model:
                model.write(f.read().replace('{{GEOMETRY}}', f
                
<geometry>
    <mesh>
        <uri>model://{block_name}/meshes/{block_name.upper()}.stl</uri>
    </mesh>
</geometry>
                
                ))'''
            
