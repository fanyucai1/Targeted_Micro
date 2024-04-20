import os
import sys
import subprocess
import argparse

def run(ref,outdir,prefix):
    ref=os.path.abspath(ref)
    data_dir=os.path.dirname(ref)
    file_name=ref.split("/")[-1]
    docker = "docker run -v %s:/database/ fanyucai1/target_micro "%(data_dir)

    bowtie2=docker+"cd /database/ && /software/bowtie2-2.5.3-linux-x86_64/bowtie2-build /database/%s %s"%(file_name,prefix)
    subprocess.check_call(bowtie2,shell=True)

    samtools=docker+"cd /database/ && /software/samtools/bin/samtools faidx %s"%(file_name)
    subprocess.check_call(samtools,shell=True)

    bwa=docker+"cd /database/ && /software/bwa/bwa index %s"%(file_name)
    subprocess.check_call(bwa,shell=True)

if __name__=="__main__":
    parser=argparse.ArgumentParser("Build bowtie2、bwa and samtools index reference genome.")
    parser.add_argument("-r","--ref",help="reference fasta",required=True)
    parser.add_argument("-o","--outdir",help="output directory",required=True)
    parser.add_argument("-p","--prefix",help="prefix of output",required=True)
    args=parser.parse_args()
    run(args.ref,args.outdir,args.prefix)