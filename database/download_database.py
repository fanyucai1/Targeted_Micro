import os
import subprocess
import argparse

parser=argparse.ArgumentParser("Download Database which target_micro need.")
parser.add_argument("-d","--database",help="output directory",required=True,default=os.getcwd())
args=parser.parse_args()

args.datbase=os.path.abspath(args.database)
os.removedirs(args.datbase)
os.mkdir(args.database)

docker="docker run -v %s:/database/ target_micro nextclade dataset get "%(args.datbase)
name="nextstrain/sars-cov-2"
os.makedirs("%s/%s"%(args.database,name))
cmd=docker+"--name \'%s\' --output-dir \'/database/nextstrain/sars-cov-2\'"%(name)
subprocess.check_call(cmd,shell=True)

name="nextstrain/flu/h3n2"#Influenza A

os.makedirs("%s/nextstrain/fluA/h3n2"%(args.database))

cmd=docker+"--name \'%s\' --output-dir \'/database/nextstrain/fluA/h3n2\'"%(name)
subprocess.check_call(cmd,shell=True)

name="nextstrain/flu/h1n1pdm"#Influenza A
os.makedirs("%s/nextstrain/fluA/h1n1/"%(args.database))
cmd=docker+"--name \'%s\' --output-dir \'/database/nextstrain/fluA/h1n1/\'"%(name)
subprocess.check_call(cmd,shell=True)

name="nextstrain/flu/vic"#Influenza B
os.makedirs("%s/nextstrain/fluB/vic"%(args.database))
cmd=docker+"--name \'%s\' --output-dir \'/database/nextstrain/fluB/vic\'"%(name)
subprocess.check_call(cmd,shell=True)

name="nextstrain/rsv/b"
os.makedirs("%s/%s"%(args.database,name))
cmd=docker+"--name \'%s\' --output-dir \'/database/%s\'"%(name,name)
subprocess.check_call(cmd,shell=True)

name="nextstrain/rsv/a"
os.makedirs("%s/%s"%(args.database,name))
cmd=docker+"--name \'%s\' --output-dir \'/database/%s\'"%(name,name)
subprocess.check_call(cmd,shell=True)

name="nextstrain/mpox"
os.makedirs("%s/%s"%(args.database,name))
cmd=docker+"--name \'%s\' --output-dir \'/database/%s\'"%(name,name)
subprocess.check_call(cmd,shell=True)

###############sra-human-scrubber
cmd=("mkdir -p %s/sra-human-scrubber && "
     "wget https://ftp.ncbi.nlm.nih.gov/sra/dbs/human_filter/human_filter.db.20231218v2 && "
     "mv human_filter.db.20231218v2 %s/sra-human-scrubber/human_filter.db")%(args.datbase,args.datbase)
subprocess.check_call(cmd,shell=True)

