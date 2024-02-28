import subprocess
import os
import argparse


def pangolin(fasta,db,prefix,outdir=os.getcwd()):
    # Calculation of the consensus sequence is used to determine the predominant lineage
    cmd = ("pangolin --alignment %s --threads 2 --outdir %s --outfile %s.lineage_report.csv --alignment-file %s.alignment.fasta"
           % (fasta,outdir, prefix,prefix))
    print(cmd)
    subprocess.check_call(cmd, shell=True)

