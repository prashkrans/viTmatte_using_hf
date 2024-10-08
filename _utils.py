import os
import json

def get_image_names_with_ext_from_folder(folder_path):
    # List files in the directory
    files = os.listdir(folder_path)
    image_names_with_ext = []

    for file in files:
        # Check if the file is a .jpg or .png file
        if file.lower().endswith(('.jpg', '.png', 'jpeg')):
            image_names_with_ext.append(file)

    return image_names_with_ext

with open('config.json') as file:
    config = json.load(file)

input_dir = config['input_dir']
descaled_dir = config['descaled_dir']
trimap_dir = config['trimap_dir']
alpha_matte_dir = config['alpha_matte_dir']
output_dir = config['output_dir']

os.makedirs(descaled_dir, exist_ok=True)
os.makedirs(trimap_dir, exist_ok=True)
os.makedirs(alpha_matte_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)




def is_image_file(filename):
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp'}
    return os.path.splitext(filename)[1].lower() in image_extensions

def clear_image_files(src_dir):
    for filename in os.listdir(src_dir):
        if is_image_file(filename):
            file_path = os.path.join(src_dir, filename)
            try:
                os.unlink(file_path)
                print(f'Deleted: {file_path}')
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')