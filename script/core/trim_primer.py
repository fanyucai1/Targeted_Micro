import subprocess

def ivar(bam,bed,outdir,prefix):
    out=outdir+"/"+prefix
    cmd = "/software/Miniconda3/bin/ivar trim -e -i %s -b %s -p %s.trim_primer | tee %s.ivar.stdout" % (bam, bed, out, out)
    print(cmd)
    subprocess.check_call(cmd, shell=True)
    cmd = "samtools sort %s.trim_primer.bam -o %s.trim_primer.sort.bam && rm -rf %s.trim_primer.bam" % (out, out,out)
    print(cmd)
    subprocess.check_call(cmd, shell=True)
    cmd = "java -jar /software/jvarkit.jar biostar84452 --samoutputformat BAM %s.soft.clipped.sort.bam |samtools sort -n >%s.trimmed.bam" % (
    out, out)
    print(cmd)
    subprocess.check_call(cmd, shell=True)
