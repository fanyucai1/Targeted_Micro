import subprocess
import argparse

def ivar(bam,bed,outdir,prefix):
    out=outdir+"/"+prefix
    cmd = "/software/Miniconda3/bin/ivar trim -e -i %s -b %s -p %s.trim_primer | tee %s.ivar.stdout" % (bam, bed, out, out)
    subprocess.check_call(cmd, shell=True)
    cmd = "/software/samtools/bin/samtools sort %s.trim_primer.bam -o %s.trim_primer.sort.bam && rm -rf %s.trim_primer.bam" % (out, out,out)
    subprocess.check_call(cmd, shell=True)
    cmd = ("/software/openlogic-openjdk-jre-8u392-b08-linux-x64/bin/java -jar /software//jvarkit/jvarkit.jar biostar84452 "
           "--samoutputformat BAM %s.trim_primer.sort.bam |/software/samtools/bin/samtools sort -n >%s.trimmed.bam && rm -rf %s.trim_primer.sort.bam") % (
    out, out,out)
    subprocess.check_call(cmd, shell=True)
    cmd = ("/software/samtools/bin/samtools fastq -1 %s_no_primer.R1.fq -2 %s_no_primer.R2.fq -s %s.singleton.fastq %s.trimmed.bam &>%s.bam2fastq.stdout"
           % (out, out, out, out, out))
    subprocess.check_call(cmd, shell=True)

if __name__=="__main__":
    parser = argparse.ArgumentParser("Trim primers with ivar.")
    parser.add_argument("-m","--bam", help="sort bam file", required=True)
    parser.add_argument( "-b","--bed", help="reference fasta", required=True)
    parser.add_argument("-o","--outdir", help="output directory", required=True)
    parser.add_argument("-p","--prefix", help="prefix of output", required=True)
    args = parser.parse_args()
    ivar(args.bam, args.bed, args.outdir, args.prefix)
