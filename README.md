# Analysis Pipeline 

    1.Reads are trimmed and filtered using Trimmomatic with the following parameters: LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36.
    
    2.Human reads are removed with a modified version of the SRA Human Read Scrubber tool.

    3.MEGAHIT is used to perform de novo assembly on the scrubbed reads.

    4.CD-HIT-EST is used to cluster similar contigs to reduce redundancy.
    
    5.The resulting contigs are mapped to a set of reference genomes using minimap2.
    
    6.The best matching reference for each contig is selected for short read mapping.
    
    7.The scrubbed reads from step 3 are aligned to the selected reference genomes using [DRAGEN v4.0.3]
    
    8.Sequence variants are called from the alignments using DRAGEN Somatic v4.0.3 and applied to the corresponding reference sequences to create consensus sequences.
    
    9.If applicable, Pangolin and/or Nextclade are run on the consensus sequences.

# Docker image
```{.cs}
docker pull fanyucai1/target_micro
```

# software list
```{.cs}
/usr/local/bin/samtools
/usr/local/bin/bcftools
/software/fastqtk/fastqtk
/software/seqtk/seqtk
/software/bedtools2/bin/bedtools
/software/minimap2/minimap2
/usr/bin/fastp
/software/cd-hit-v4.8.1-2019-0228/cd-hit-est
/software/Trimmomatic-0.39/trimmomatic-0.39.jar
/software/quast-5.2.0/quast.py
/software/bwa/bwa
/software/sra-human-scrubber/scripts/scrub.sh
/software/MEGAHIT-1.2.9-Linux-x86_64-static/bin/megahit
/software/Miniconda3/bin/bbmap.sh
/software/Miniconda3/bin/ivar
/software/Miniconda3/bin/kraken2
/software/Miniconda3/bin/mafft
/software/Miniconda3/bin/pangolin
/software/Miniconda3/bin/nextclade
/software/Python-v3.11.0/bin/freyja
/software/Python-v3.11.0/bin/freyja_plot
```

# Database

 1. Download Currently version:human k-mer database used by the NCBI SRA Human Read Removal Tool



        mkdir -p /path/to/database/sra-human-scrubber/data
        cd /path/to/database/sra-human-scrubber/data
        wget https://ftp.ncbi.nlm.nih.gov/sra/dbs/human_filter/human_filter.db.20231218v2