import subprocess
import argparse
import os

def megahit(R1,R2,prefix,outdir):
    if os.path.exists(outdir):
        subprocess.check_call("rm -rf %s"%(outdir),shell=True)
    out=outdir+"/"+prefix
    cmd = ("/software/MEGAHIT-1.2.9-Linux-x86_64-static/bin/megahit -1 %s -2 %s --min-contig-len 500 --out-dir %s --out-prefix %s && "
               "/software/Python-v3.11.0/bin/python3 /software/quast-5.2.0/quast.py --output-dir %s %s.contigs.fa") % (R1, R2, outdir,prefix,outdir,out)
    subprocess.check_call(cmd, shell=True)

if __name__=="__main__":
    parser = argparse.ArgumentParser("MEGAHIT is used to perform de novo assembly.")
    parser.add_argument("-1", "--R1", help="sort bam file", required=True)
    parser.add_argument("-2", "--R2", help="reference fasta", required=True)
    parser.add_argument("-p","--prefix",help="prefix of output",required=True)
    parser.add_argument("-o", "--outdir", help="output directory", required=True)
    args = parser.parse_args()
    megahit(args.R1, args.R2, args.outdir,args.prefix)
