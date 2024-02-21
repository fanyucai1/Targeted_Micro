FROM fanyucai1/base

RUN cd /software/&& git clone https://github.com/ndaniel/fastqtk.git && cd fastqtk && make

RUN cd /software/ &&  \
    wget https://github.com/voutcn/megahit/releases/download/v1.2.9/MEGAHIT-1.2.9-Linux-x86_64-static.tar.gz &&  \
    tar xzvf MEGAHIT-1.2.9-Linux-x86_64-static.tar.gz

RUN cd /software/ && wget https://github.com/lh3/minimap2/releases/download/v2.26/minimap2-2.26_x64-linux.tar.bz2 && \
    tar xjvf minimap2-2.26_x64-linux.tar.bz2

RUN cd /software/ && wget https://github.com/weizhongli/cdhit/releases/download/V4.8.1/cd-hit-v4.8.1-2019-0228.tar.gz &&  \
    tar xzvf cd-hit-v4.8.1-2019-0228.tar.gz && cd cd-hit-v4.8.1-2019-0228 && make

RUN cd /software/ && wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.39.zip && unzip Trimmomatic-0.39.zip

RUN cd /software/ && wget https://github.com/ncbi/sra-human-scrubber/releases/download/2.2.1/sra-human-scrubber-2.2.1.tar.gz && \
    tar xzvf sra-human-scrubber-2.2.1.tar.gz

RUN cd /software/ && /software/Python-v3.11.0/bin/pip3 install quast seaborn matplotlib numpy pysam pandas

RUN cd /software/ && wget --no-check-certificate https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh &&  \
    bash Miniconda3-latest-Linux-x86_64.sh -bfp /software/Miniconda3

RUN /software/Miniconda3/bin/conda install -c bioconda ivar pyvcf nextclade kraken2 krakentools bedtools samtools bwa fastp seqtk bbmap
