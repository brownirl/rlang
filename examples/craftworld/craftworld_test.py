import sys, os
sys.path.append(os.path.abspath("./"))

import torch  
import argparse

import vocab 

parser = argparse.ArgumentParser(description='Craftworld-RLang Arguments', add_help=False)
parser.add_argument('--device', type=str, default='cpu', help='Device to run: cpu or cuda')

args = parser.parse_args()
vocab.main(args.device)