#!/usr/bin/env python3
import argparse
import json

parser = argparse.ArgumentParser("oraxen.py")
parser.add_argument("model", help="path to a model file", type=str)
parser.add_argument("--output", help="path to the output model file", type=str)
args = parser.parse_args()

with open(args.model) as model_file:
    content = json.load(model_file)
    elements = content["elements"]
    for element in elements:
        if "__comment" in element:
            del element["__comment"]
    optimized_output = json.dumps(content).replace(" ", "")
    with open(args.model.replace(".json", "") + "_optimized.json", 'w') as output_file:
        output_file.write(optimized_output)