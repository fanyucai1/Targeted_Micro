import subprocess
import argparse
import os

def megahit(R1,R2,outdir,prefix):
    if os.path.exists(outdir):
        cmd = "/software/MEGAHIT-1.2.9-Linux-x86_64-static/bin/megahit -1 %s -2 %s --min-contig-len 500 --out-dir %s/megahit/ --out-prefix %s" % (R1, R2, outdir,prefix)
    else:
        cmd = "/software/MEGAHIT-1.2.9-Linux-x86_64-static/bin/megahit -1 %s -2 %s --min-contig-len 500 --out-dir %s/ --out-prefix %s" % (R1, R2, outdir,prefix)
    subprocess.check_call(cmd, shell=True)

if __name__=="__main__":
    parser = argparse.ArgumentParser("MEGAHIT is used to perform de novo assembly.")
    parser.add_argument("-1", "--R1", help="sort bam file", required=True)
    parser.add_argument("-2", "--R2", help="reference fasta", required=True)
    parser.add_argument("-p","--prefix",help="prefix of output",required=True)
    parser.add_argument("-o", "--outdir", help="output directory", required=True)
    args = parser.parse_args()
    megahit(args.R1, args.R2, args.outdir,args.prefix)
