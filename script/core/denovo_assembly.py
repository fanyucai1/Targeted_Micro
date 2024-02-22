import subprocess
import argparse

def megahit(R1,R2,outdir):
    cmd = "/software/MEGAHIT-1.2.9-Linux-x86_64-static/bin/megahit -1 %s -2 %s -o %s" % (R1, R2, outdir)
    subprocess.check_call(cmd, shell=True)

if __name__=="__main__":
    parser = argparse.ArgumentParser("MEGAHIT is used to perform de novo assembly.")
    parser.add_argument("-1", "--R1", help="sort bam file", required=True)
    parser.add_argument("-2", "--R2", help="reference fasta", required=True)
    parser.add_argument("-o", "--outdir", help="output directory", required=True)
    args = parser.parse_args()
    megahit(args.R1, args.R2, args.outdir)
