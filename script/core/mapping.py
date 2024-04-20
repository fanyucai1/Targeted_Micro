import argparse
import subprocess
import os,sys

def bowtie2(R1,R2,ref,prefix,outdir):
    outdir=os.path.abspath(outdir)
    if not os.path.exists(outdir):
        subprocess.check_call("mkdir -p %s"%(args.outdir),shell=True)
    out=outdir+'/'+prefix
    # align reads with bowtie2 and sort bam with samtools
    cmd = (("/software/bowtie2-2.5.3-linux-x86_64/bowtie2 --threads 24 -x %s -1 %s_1.fastq.gz -2 %s_2.fastq.gz |/software/samtools/bin/samtools view -bh |"
           "/software/samtools/bin/samtools sort > %s.bam && /software/samtools/bin/samtools index %s.bam && rm -rf %s_1.fastq.gz %s_2.fastq.gz")
           % (ref,R1, R2, out, out, out, out))
    print(cmd)
    subprocess.check_call(cmd, shell=True)

if __name__=="__main__":
    parser=argparse.ArgumentParser("Mapping reference.")
    parser.add_argument("-1","--R1",help="R1 fastq",required=True)
    parser.add_argument("-2","--R2",help="R2 fastq",required=True)
    parser.add_argument("-r","--ref",help="reference index",required=True)
    parser.add_argument("-o","--outdir",help="output directory",default=os.getcwd())
    parser.add_argument("-p","--prefix",help="prefix of output")
    args=parser.parse_args()
    bowtie2(args.R1,args.R2,args.ref,args.prefix,args.outdir)
