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
        pack_files.append(os.path.join(path, name).replace(args.folder, "", 1))

output_folder = "./output"
if os.path.isdir(output_folder):
    shutil.rmtree(output_folder)
os.mkdir(output_folder)

for pack_file in pack_files:
    input_file = args.folder + pack_file
    new_name = output_folder + pack_file

    if not os.path.exists(os.path.dirname(new_name)):
        try:
            os.makedirs(os.path.dirname(new_name))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    if pack_file.endswith(".json"):
        with open(input_file) as model_file:
            content = json.load(model_file)
            if "elements" in content:
                elements = content["elements"]
                for element in elements:
                    if "__comment" in element:
                        del element["__comment"]
            optimized_output = json.dumps(content).replace(" ", "")
            with open(new_name, 'w') as output_file:
                output_file.write(optimized_output)
    else:
        shutil.copyfile(input_file, new_name)