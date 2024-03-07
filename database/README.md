# Downlaod database

## stepo1:

    python3 download_database.py -d /path/to/database/

    Database list:
    Nextclade:https://clades.nextstrain.org/dataset)

        Influenza A
                h3n2
                h1n1pdm
        Influenza B
                vic
        rsv
                a
                b
        mpox
    human k-mer database used by the NCBI SRA Human Read Removal Tool:https://ftp.ncbi.nlm.nih.gov/sra/dbs/human_filter/

## step2: fix Dockerfile and build pangolin
    
    docker build -t covlineages/pangolin ./

