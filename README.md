# Analysis Pipeline


**0. Build docker image**
```{.cs}
docker rmi -f covlineages/pangolin:latest
docker build https://github.com/cov-lineages/pangolin.git -t covlineages/pangolin:latest
docker pull fanyucai1/target_micro
```

**1. Reads are trimmed and filtered using Trimmomatic.**
```{.cs}
docker run -v /staging4/fanyucai/target_micro/raw_data:/raw_data/ \
-v /staging4/fanyucai/target_micro/script/:/script/ \
-v /staging4/fanyucai/target_micro/outdir:/outdir/ \
-v /staging4/fanyucai/target_micro/database/:/database/ \
fanyucai1/target_micro \
/software/Python-v3.11.0/bin/python3 /script/core/qc.py \
-1 /outdir/SRR20696400.R1.scrub.fq -2 /outdir/SRR20696400.R2.scrub.fq \
-o /outdir/ -p SRR20696400
```
**2. human k-mer database used by the NCBI SRA Human Read Removal Tool**
```{.cs}
docker run -v /staging4/fanyucai/target_micro/raw_data:/raw_data/ \
-v /staging4/fanyucai/target_micro/script/:/script/ \
-v /staging4/fanyucai/target_micro/outdir:/outdir/ \
-v /staging4/fanyucai/target_micro/database/:/database/ \
fanyucai1/target_micro \
/software/Python-v3.11.0/bin/python3 /script/core/filter_host_human.py \
-1 /raw_data/SRR20696400_1.fastq.gz -2 /raw_data/SRR20696400_2.fastq.gz \
-d /database/ -o /outdir/ -p SRR20696400
```
**3. MEGAHIT is used to perform de novo assembly on the scrubbed reads.**
```{.cs}
docker run -v /staging4/fanyucai/target_micro/raw_data:/raw_data/ \
-v /staging4/fanyucai/target_micro/script/:/script/ \
-v /staging4/fanyucai/target_micro/outdir:/outdir/ \
-v /staging4/fanyucai/target_micro/database/:/database/ \
fanyucai1/target_micro \
/software/Python-v3.11.0/bin/python3 /script/core/denovo_assembly.py \
-1 /outdir/SRR20696400.clean_R1.fq.gz -2 /outdir/SRR20696400.clean_R2.fq.gz \
-p SRR20696400 -o /outdir/
```
**4. CD-HIT-EST is used to cluster similar contigs to reduce redundancy.**
```{.cs}
docker run -v /staging4/fanyucai/target_micro/raw_data:/raw_data/ \
-v /staging4/fanyucai/target_micro/script/:/script/ \
-v /staging4/fanyucai/target_micro/outdir:/outdir/ \
-v /staging4/fanyucai/target_micro/database/:/database/ \
fanyucai1/target_micro \
/software/Python-v3.11.0/bin/python3 /script/core/reduce_redundancy.py \
-f /outdir/SRR20696400.assembly/SRR20696400.contigs.fa -o /outdir/ -p SRR20696400
```
**5. create consensus sequences**
```{.cs}
docker run -v /staging4/fanyucai/target_micro/raw_data:/raw_data/ \
-v /staging4/fanyucai/target_micro/script/:/script/ \
-v /staging4/fanyucai/target_micro/outdir:/outdir/ \
-v /staging4/fanyucai/target_micro/database/:/database/ \
fanyucai1/target_micro \
/software/Python-v3.11.0/bin/python3 
```