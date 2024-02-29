import subprocess
import argparse

def cdhit(fasta,prefix,outdir):## CD-HIT-EST is used to cluster similar contigs to reduce redundancy.
    out = outdir + "/" + prefix
    cmd = "/software/cd-hit-v4.8.1-2019-0228/cd-hit-est -i %s -o %s.no_redundancy.fasta -c 0.95 -n 5 -g 1 -aS 0.8 -T 0"%(fasta,out)
    subprocess.check_call(cmd,shell=True)

if __name__=="__main__":
    parser=argparse.ArgumentParser("CD-HIT-EST is used to cluster similar contigs to reduce redundancy")
    parser.add_argument("-f","--fasta",help="fasta sequence",required=True)
    parser.add_argument("-o", "--outdir", help="output directory", required=True)
    parser.add_argument("-p", "--prefix", help="prefix of output", required=True)
    args = parser.parse_args()
    cdhit(args.fasta,args.outdir,args.prefix)
