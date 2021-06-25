import sys
import os
sys.path.append(os.getcwd())
import argparse
import json
from evaluation import evaluation



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--SUBMISSIONID', required=False, type=str, help='shakey where data is dumped')
    parser.add_argument('--CHALLENGEID', required=False, type=str, help='ID of the Benchmark')
    parser.add_argument('--GTFOLDER', required=False, type=str, help="GT folder")
    parser.add_argument('--UPLOADFOLDER', required=False, type=str, help="Upload folder")
    parser.add_argument('--SEQUENCEIDS', required=False, type=str, help="Sequences to eval")
    parser.add_argument('--PYTHONPATH', required=False, type=str, help="Sequences to eval")

    args = parser.parse_args().__dict__
    # submission_id = args["SUBMISSIONID"]
    # challenge_id = args["CHALLENGEID"]
    # gt_folder = args["GTFOLDER"]
    # sequence_ids = args["SEQUENCEIDS"].replace(",", " ")
    upload_folder = args["UPLOADFOLDER"]
    # python_path = args["PYTHONPATH"]
    
    evaluation = evaluation(upload_folder)
    

