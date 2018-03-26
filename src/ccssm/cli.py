import argparse
import snakemake
import pkg_resources

def main():
    """Main function of the program."""
    parser = argparse.ArgumentParser(
        description= "")
    parser.add_argument(
        "--ref-genome",
        required = True,
        help = "Path to the reference genome and bowtie index")
    parser.add_argument(
        "--fastq",
        required = True,
        help = "Path to the FastQ file"
    )
    args = parser.parse_args()
    snakefile = pkg_resources.resource_filename(__name__, "Snakefile")
    snakemake.snakemake(snakefile, config={"REFGEN": args.ref_genome, "FASTQ": args.fastq})