import os
from os.path import join
from os import mkdir
from typing import Any

import argparse
import json

def parse_line(line) -> tuple:
    parts = line.split(",")
    return (int(parts[0]), [ parts[1], parts[2], parts[3], parts[4], parts[5] ])

def create_framedata(result_file: "os.PathLike[Any]", output_directory: "os.PathLike[Any]") -> None:
    out_prediction = os.path.join(output_directory, "prediction")
    try:
        os.makedirs(out_prediction)
    except: 
        pass 
        
    with open(result_file, 'r') as file:
        lines = file.readlines()
        lines = map(parse_line, lines)
        current_frame = 0
        current_file = None
        for frame, data in lines:
            if not frame == current_frame:
                current_file = open(join(out_prediction, "{:06d}.framedata".format(frame)), 'a+')
                current_frame = frame
            # else:
            #     current_file.write("\n")
            current_file.write(",".join(data))
            current_file.write("\n")
    config_json = {
    "name": "Prediction",
    "description": "This is the description for Predicitons."
}
    with open(os.path.join(out_prediction, "sample.json"), "w") as outfile: 
        json.dump(config_json, outfile)
        # create json
if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-r", "--FILE", type=str, required=True, help="location of result file")
    parser.add_argument("-o", "--OUT", type=str, required=True, help="directory of output framedata")     
    args = parser.parse_args()                   
    create_framedata(result_file = args.FILE, output_directory = args.OUT)