import argparse
parser = argparse.ArgumentParser(description="our example parser.")
parser.add_argument("--filename","-f",required=True)
parser.add_argument("--medals",action="store_true",required=False)
parser.add_argument("--output","-o",required=False)
parser.add_argument("--total","-t",required=False)
parser.add_argument("--year","-y",required=False)
parser.add_argument("--team",required=False)

args=parser.parse_args()

filename = args['filename']
medals = args['medals']
output = args['output']
total = args['total']
overall = args['overall']
interactive = args['interactive']
file= open("filename","r")

def part1(filename,country,year,output):
    zoloto=0
    serebro=0
    bronz=0
    i=0
    x=''
    while True:
        line=file.readline()
        if not line:
            break
        id=line.split("\t")
        year1=id[]
