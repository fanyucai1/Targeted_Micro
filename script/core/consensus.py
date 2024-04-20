import subprocess
import argparse

def bcftools(bam,ref_fasta,outdir,prefix):
    out=outdir+"/"+prefix
    cmd = "/software/bcftools/bin/bcftools mpileup -Ou -f %s %s | /software/bcftools/bin/bcftools call --ploidy 1 -mv -Oz -o %s.calls.vcf.gz" % (ref_fasta,bam, out)
    cmd += " && /software/bcftools/bin/bcftools index %s.calls.vcf.gz" % (out)
    cmd += " && cat %s | /software/bcftools/bin/bcftools consensus %s.calls.vcf.gz -p %s > %s.consensus.fa" % (ref_fasta, out,prefix, out)
    subprocess.check_call(cmd, shell=True)
    subprocess.check_call('sed -i \'1s/.*/>%s/\' %s.consensus.fa' % (prefix, out), shell=True)

if __name__=="__main__":
    parser=argparse.ArgumentParser("Calculation of the consensus sequence using bcftools.")
    parser.add_argument("-b","--bam",help="sort bam file",required=True)
    parser.add_argument("-r","--ref",help="reference fasta",required=True)
    parser.add_argument("-o","--outdir",help="output directory",required=True)
    parser.add_argument("-p","--prefix",help="prefix of output",required=True)
    args=parser.parse_args()
    bcftools(args.bam,args.ref,args.outdir,args.prefix)
