import hashlib
import argparse

print('''
 _    _           _     _        _______ _     _             
| |  | |         | |   (_)      |__   __| |   (_)            
| |__| | __ _ ___| |__  _ _ __      | |  | |__  _ _ __   __ _ 
|  __  |/ _` / __| '_ \| | '_ \     | |  | '_ \| | '_ \ / _` |
| |  | | (_| \__ \ | | | | | | |    | |  | | | | | | | | (_| |
|_|  |_|\__,_|___/_| |_|_|_| |_|    |_|  |_| |_|_|_| |_|\__, |
                                                         __/ |
                                                        |___/ 
By Maik Jeschke
''')

def calculate_md5(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        return hashlib.md5(data).hexdigest()

def is_md5_matching(file_path, md5_to_check):
    calculated_md5 = calculate_md5(file_path)
    return calculated_md5 == md5_to_check

parser = argparse.ArgumentParser(description='Check if the MD5 hash of a file matches a given hash.')
parser.add_argument('file_path', type=str, help='The path to the file to check.')
parser.add_argument('md5_to_check', type=str, help='The MD5 hash to check against.')

args = parser.parse_args()

if is_md5_matching(args.file_path, args.md5_to_check):
    print('The MD5 hash of the file matches the provided hash.')
else:
    print('The MD5 hash of the file does not match the provided hash.')
