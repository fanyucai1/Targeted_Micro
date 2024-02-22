import os,sys,time
import argparse,subprocess
import core.trim_primer,core.denovo_assembly,core.qc,core.consensus,core.filter_host_human

parser=argparse.ArgumentParser("")
parser.add_argument("-p1","--pe1",help="R1 reads,required",required=True)
parser.add_argument("-p2","--pe2",help="R2 reads")
parser.add_argument("-r","--ref",help="reference fasta")
parser.add_argument("-p","--prefix",help="prefix of output",required=True)
parser.add_argument("-o","--outdir",help="output directory",default=os.getcwd())
parser.add_argument("-b","--bed",help="primer bed file",required=True)
args=parser.parse_args()

args.outdir=os.path.abspath(args.outdir)
if not os.path.exists(args.outdir):
    subprocess.check_call("mkdir -p %s"%(args.outdir),shell=True)

args.pe1=os.path.abspath(args.pe1)
args.pe2=os.path.abspath(args.pe2)
args.ref=os.path.abspath(args.ref)

# step1:
subprocess.check_call("mkdir -p %s/1.qc"%(args.outdir),shell=True)
outdir_1=args.outdir+"/1.qc/"+args.prefix


# step2:
subprocess.check_call("mkdir -p %s/2.human_removed"%(args.outdir),shell=True)
outdir_2=args.outdir+"/2.human_removed/"+args.prefix



# step3:
subprocess.check_call("mkdir -p %s/3.denovo_assembly"%(args.outdir),shell=True)
outdir_3=args.outdir+"/3.denovo_assembly/"


# step4:
subprocess.check_call("mkdir -p %s/4.reduce_redundancy"%(args.outdir),shell=True)
outdir_4=args.outdir+"/4.reduce_redundancy/"


