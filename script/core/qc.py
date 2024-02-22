import subprocess
import argparse

def trimmomatic(R1,R2,prefix,outdir):
    out=outdir+"/"+prefix
    cmd=("java -jar /software/Trimmomatic-0.39/trimmomatic-0.39.jar "
         "PE %s %s %s_R1.fq.gz %s_R1_unpaired.fq.gz %s_R2.fq.gz %s_R2_unpaired.fq.gz "
         "LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36")%(R1,R2,out,out,out,out)
    subprocess.check_call(cmd,shell=True)


if __name__=="__main__":
    parser = argparse.ArgumentParser("Human reads are removed with a modified version of the SRA Human Read Scrubber tool.")
    parser.add_argument("-1", "--R1", help="sort bam file", required=True)
    parser.add_argument("-2", "--R2", help="reference fasta", required=True)
    parser.add_argument("-d","--database",help="human k-mer database used by the NCBI SRA Human Read Removal Tool",required=True)
    parser.add_argument("-o", "--outdir", help="output directory", required=True)
    parser.add_argument("-p","--prefix",help="prefix of output",required=True)
    args=parser.parse_args()
    scrub(args.R1,args.R2,args.database,args.prefix,args.outdir)