#!/usr/bin/env python3
import argparse
import shutil
import json
import os

parser = argparse.ArgumentParser("oraxen.py")
parser.add_argument("folder", help="path to the input folder", type=str)
args = parser.parse_args()

pack_files = []
for path, subdirs, files in os.walk(args.folder):
    for name in files:
        pack_files.append(name.replace(args.folder, "", 1))

output_folder = "./output"
if os.path.isdir(output_folder):
    shutil.rmtree(output_folder)
os.mkdir(output_folder)

for pack_file in pack_files:
    input_file = os.path.join(args.folder, pack_file)
    new_name = os.path.join(output_folder, pack_file)
    if pack_file.endswith(".json"):
        with open(input_file) as model_file:
            content = json.load(model_file)
            elements = content["elements"]
            for element in elements:
                if "__comment" in element:
                    del element["__comment"]
            optimized_output = json.dumps(content).replace(" ", "")
            with open(new_name, 'w') as output_file:
                output_file.write(optimized_output)
    else:
        os.rename(input_file, new_name)