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

# step1: Reads are trimmed and filtered using Trimmomatic
print("step1:Reads are trimmed and filtered using Trimmomatic.")
core.qc.trimmomatic(args.pe1,args.pe2,args.prefix,args.outdir+"/1.qc/")

# step2: human k-mer database used by the NCBI SRA Human Read Removal Tool
print("step2:human k-mer database used by the NCBI SRA Human Read Removal Tool")
core.filter_host_human.scrub(args.outdir+"/1.qc/"+args.prefix+".clean_R2.fq.gz",
                             args.outdir+"/1.qc/"+args.prefix+".clean_R2.fq.gz",
                             args.database+"/sra-human-scrubber/human_filter.db",
                             args.prefix,
                             args.outdir+"/2.filter_human/")

# step3: MEGAHIT is used to perform de novo assembly on the scrubbed reads
print("step3:MEGAHIT is used to perform de novo assembly on the scrubbed reads")
core.denovo_assembly.megahit(args.outdir+"/2.filter_human/"+args.prefix+".R1.scrub.fq",
                             args.outdir+"/2.filter_human/"+args.prefix+".R2.scrub.fq",
                             args.prefix,
                             args.outdir+"/3.assembly/")

# step4: CD-HIT-EST is used to cluster similar contigs to reduce redundancy
print("step4:CD-HIT-EST is used to cluster similar contigs to reduce redundancy")
core.reduce_redundancy.cdhit(args.outdir+"/3.assembly/"+args.prefix+".contigs.fa",args.prefix,args.outdir+"/4.reduce_redundancy")

# step5: create consensus sequences
print("step5:create consensus sequences")
core.consensus.bcftools()


