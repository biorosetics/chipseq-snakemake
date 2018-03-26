# chipseq-snakemake

Snakemake version of ChipSeq analysis pipeline used by Candihub.

The Snakemake workflow management system is a tool to create reproducible and scalable data analyses.

When using Snakemake for a publication, **please cite the following article** in your paper:

`KÃ¶ster, Johannes and Rahmann, Sven. "Snakemake - A scalable bioinformatics workflow engine". Bioinformatics 2012. <http://bioinformatics.oxfordjournals.org/content/28/19/2520>`_

# Installation dependencies with Conda (bioconda)

```
conda install -y bowtie cutadapt samtools fastqc bedtools
conda install -c bioconda snakemake
python3 -venv test
cd test
source bin/activate 
```

## How does it work ?

The package ```ccssm``` is a simple wrapper to the Snakemake API. The package entry point parses the command line and construct on the fly a dictionary with two keys: 

1. REFGEN that corresponds to the reference genome file (fasta) and prefix of the bowtie index. This must be a qualified path.
2. FASTQ the input FastQ file path

This dictionary is processed by the Snakemake API call:

``` python
snakemake.snakemake(snakefile, config={"REFGEN": args.ref_genome, "FASTQ": args.fastq})
```

Of course, you can use the Snakemake file directly without installing the `ccssm` python library.

```
snakemake --config REFGEN=... 
```

## Use the command line

Command line:

```
ccssm --ref-genome my/path/to/reference/genome_and_bowtie_index --fastq my/path/to/my/fastq
```

This command will generate in the current directory this files tree:

```
analysis
├── GenomeCoverage.txt # final result
├── bowtie # bowting alignment and conversion sam -> bam -> sorted
│   ├── mapping.bam
│   ├── mapping.sam
│   ├── mapping.txt
│   └── mapping_sorted.bam
├── cutadapt
│   ├── cutadapt.fastq
│   ├── cutadapt.txt
│   ├── cutadapt_fastqc.html
│   ├── cutadapt_fastqc.zip
│   ├── fastqc_cutadapt.err
│   └── fastqc_cutadapt.log
├── fastqc_on_cutadapt.done
├── fastqc_on_raw.done
├── fastqc_raw.err
└── fastqc_raw.log
```