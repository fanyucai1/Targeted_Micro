import subprocess
import argparse

def trimmomatic(R1,R2,prefix,outdir):
    out=outdir+"/"+prefix
    cmd=("java -jar /software/Trimmomatic-0.39/trimmomatic-0.39.jar "
         "PE %s %s %s.clean_R1.fq.gz %s_R1_unpaired.fq.gz %s.clean_R2.fq.gz %s_R2_unpaired.fq.gz "
         "LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36")%(R1,R2,out,out,out,out)
    subprocess.check_call(cmd,shell=True)
    subprocess.check_call('cd %s && rm -rf *unpaired*'%(outdir),shell=True)


if __name__=="__main__":
    parser = argparse.ArgumentParser("Reads are trimmed and filtered using Trimmomatic.")
    parser.add_argument("-1", "--R1", help="sort bam file", required=True)
    parser.add_argument("-2", "--R2", help="reference fasta", required=True)
    parser.add_argument("-o", "--outdir", help="output directory", required=True)
    parser.add_argument("-p","--prefix",help="prefix of output",required=True)
    args=parser.parse_args()
    trimmomatic(args.R1,args.R2,args.prefix,args.outdir)