import os
import sys
import argparse
import time
import subprocess

Docker_name=""
parse=argparse.ArgumentParser("")
parse.add_argument("-p1","--pe1",help="R1 reads,required",required=True)
parse.add_argument("-p2","--pe2",help="R2 reads")
parse.add_argument("-p","--prefix",help="prefix of output",default="")
parse.add_argument("-o","--outdir",help="output directory",default=os.getcwd())
args=parse.parse_args()

args.outdir=os.path.abspath(args.outdir)
if not os.path.exists(args.outdir):
    subprocess.check_call("mkdir -p %s"%(args.outdir),shell=True)


# step1:
subprocess.check_call("mkdir -p %s/1.qc"%(args.outdir),shell=True)
outdir_1=args.outdir+"/1.qc/"+args.prefix
#Reads are trimmed and filtered using Trimmomatic
cmd=("java -jar /software/trimmomatic-0.39.jar PE %s %s "
     "%s_R1.fq.gz %s_R1_unpaired.fq.gz %s_R2.fq.gz %s_R2_unpaired.fq.gz "
     "LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36")%(args.pe1,args.pe2,outdir_1,outdir_1)
subprocess.check_call(cmd,shell=True)


# step2:
subprocess.check_call("mkdir -p %s/2.human_removed"%(args.outdir),shell=True)
outdir_2=args.outdir+"/2.human_removed/"+args.prefix
## interleaves two paired-end FASTQ files
cmd="fastqtk interleave %s_R1.fq.gz %s_R1.fq.gz - | gzip > %s.interleave.fq.gz"%(outdir_1,outdir_1,outdir_2)
subprocess.check_call(cmd,shell=True)
## Human reads are removed with a modified version of the SRA Human Read Scrubber tool.
cmd="scrub.sh -s -p 24 -i %s.qc.fq.gz|fastqtk deinterleave - %s.R1.scrub.fq %s.R1.scrub.fq"%(outdir_2,outdir_2,outdir_2)
subprocess.check_call(cmd,shell=True)

# step3:
subprocess.check_call("mkdir -p %s/3.denovo_assembly"%(args.outdir),shell=True)
outdir_3=args.outdir+"/3.denovo_assembly/"
## MEGAHIT is used to perform de novo assembly on the scrubbed reads.
cmd="megahit -1 %s.R1.scrub.fq -2 %s.R2.scrub.fq -o %s"%(outdir_2,outdir_2,outdir_3)
subprocess.check_call(cmd,shell=True)

# step4:
subprocess.check_call("mkdir -p %s/4.reduce_redundancy"%(args.outdir),shell=True)
outdir_4=args.outdir+"/4.reduce_redundancy/"
## CD-HIT-EST is used to cluster similar contigs to reduce redundancy.
cmd=""
subprocess.check_call(cmd,shell=True)

