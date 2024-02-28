import os
import subprocess
import argparse

parser=argparse.ArgumentParser("Download Database which target_micro need.")
parser.add_argument("-d","--database",help="output directory",required=True,default=os.getcwd())
args=parser.parse_args()

args.datbase=os.path.abspath(args.datbase)
if not os.path.exists(args.database):
    os.mkdir(args.database)

docker="docker run -v %s:/database/ target_micro /software/Miniconda3/bin/nextclade dataset get "%(args.datbase)

name="nextstrain/sars-cov-2"
os.mkdir("%s/%s"%(args.datbase,name))
cmd=docker+"--name \'%s\' --output-dir \'/database/nextstrain/sars-cov-2\'"%(name)
subprocess.check_call(cmd,shell=True)

name="nextstrain/flu/h3n2"#Influenza A
os.mkdir("%s/fluA/%s"%(args.datbase,name))
cmd=docker+"--name \'%s\' --output-dir \'/database/nextstrain/fluA/h3n2\'"%(name)
subprocess.check_call(cmd,shell=True)

name="nextstrain/flu/h1n1pdm"#Influenza A
os.mkdir("%s/fluA/%s"%(args.datbase,name))
cmd=docker+"--name \'%s\' --output-dir \'/database/nextstrain/fluA/h1n1/\'"%(name)
subprocess.check_call(cmd,shell=True)

name="nextstrain/flu/vic/"#Influenza B
os.mkdir("%s/fluB/%s"%(args.datbase,name))
cmd=docker+"--name \'%s\' --output-dir \'/database/nextstrain/fluB/vic\'"%(name)
subprocess.check_call(cmd,shell=True)

name="nextstrain/rsv/b/"
os.mkdir("%s/%s"%(args.datbase,name))
cmd=docker+"--name \'%s\' --output-dir \'/database/%s\'"%(name,name)
subprocess.check_call(cmd,shell=True)

name="nextstrain/rsv/a/"
os.mkdir("%s/%s"%(args.datbase,name))
cmd=docker+"--name \'%s\' --output-dir \'/database/%s\'"%(name,name)
subprocess.check_call(cmd,shell=True)

name="nextstrain/mpox"
os.mkdir("%s/%s"%(args.datbase,name))
cmd=docker+"--name \'%s\' --output-dir \'/database/%s\'"%(name,name)
subprocess.check_call(cmd,shell=True)

###############
cmd=("mkdir -p %s/sra-human-scrubber && "
     "wget https://ftp.ncbi.nlm.nih.gov/sra/dbs/human_filter/human_filter.db.20231218v2 && "
     "mv human_filter.db.20231218v2 %s/human_filter.db")%(args.datbase,args.datbase)
subprocess.check_call(cmd,shell=True)
