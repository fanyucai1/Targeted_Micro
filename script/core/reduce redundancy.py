import subprocess
def cdhit(fasta,outdir,prefix):## CD-HIT-EST is used to cluster similar contigs to reduce redundancy.
    out = outdir + "/" + prefix
    cmd = "/software/cd-hit-v4.8.1-2019-0228/cd-hit-est -i %s -o %s.fasta -c 0.95 -n 5 -g 1 -aS 0.8 -T 0"%(fasta,out)
    subprocess.check_call(cmd,shell=True)