import subprocess

cmd="wget https://github.com/cov-lineages/pangolin/archive/refs/heads/master.zip && "
cmd+="unzip master.zip && "
cmd+="docker rmi -f covlineages/pangolin && docker build -t covlineages/pangolin pangolin-master/"
subprocess.check_call(cmd,shell=True)