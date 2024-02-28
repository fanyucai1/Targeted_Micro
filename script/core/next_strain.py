import os
import subprocess
import argparse
import re

def nextclade(fasta,db,name,outdir=os.getcwd()):
    db =db+"/"+"nextstrain/"
    if re.search(r'h1n1',name):
        db=db+"/fluA/h1n1/"

    if re.search(r'sars-cov-2',name):
        db=db+"/sars-cov-2/"

    if re.search(r'fluB',name) or re.search(r'vic',name):
        db=db+"/fluB/vic"

    if re.search(r'rsv_a',name):
        db=db+"/rsv/a"

    if re.search(r'rsv_b', name):
        db = db+"/rsv/b"

    if re.search(r'mpox', name):
        db = db+"/mpox/"

    clade_cmd="/software/Miniconda3/bin/nextclade run --input-dataset %s --output-all=%s %s"%(db,outdir,fasta)
    subprocess.check_call(clade_cmd,shell=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser("Performs alignment, mutation calling, clade assignment, phylogenetic placement and quality control checks and displays the results in tabular form and as a phylogenetic tree. ")
    parser.add_argument("-c","--consensus",help='consensus fasta sequence',required=True)
    parser.add_argument("-o","--outdir",help="output directory",default=os.getcwd())
    parser.add_argument("-d","--db",help="database directory",required=True)
    parser.add_argument("-n","--name",help="strain name",choices=['fluA_h1n1','fluA_h3n2'
        ,'fluB_vic','mpox','rsv_a','rsv_b','sars-cov-2'],required=True)
    args=parser.parse_args()
    nextclade(args.consensus,args.name,args.outdir)