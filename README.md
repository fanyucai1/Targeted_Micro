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

# Docker images software list

    

# Database

 1. Download Currently version:human k-mer database used by the NCBI SRA Human Read Removal Tool

        mkdir -p /path/to/database/sra-human-scrubber/data
        cd /path/to/database/sra-human-scrubber/data
        wget https://ftp.ncbi.nlm.nih.gov/sra/dbs/human_filter/human_filter.db.20231218v2