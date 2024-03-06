import argparse
import subprocess
import os,sys

def bwa(R1,R2,ref,prefix,outdir):
    if os.path.exists("/opt/edico/bin/dragen"):
        pass
        
    else:
        pass








if __name__=="__main__":
    parser=argparse.ArgumentParser("Mapping reference.")
    parser.add_argument("-1","--R1",help="R1 fastq",required=True)
    parser.add_argument("-2","--R2",help="R2 fastq",required=True)
    parser.add_argument("-r","--ref",help="reference fasta",required=True)
    parser.add_argument("-o","--outdir",help="output directory",default=os.getcwd())
    parser.add_argument("-p","--prefix",help="prefix of output")
    args=parser.parse_args()
