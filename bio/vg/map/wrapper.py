__author__ = "Ali Ghaffaari"
__copyright__ = "Copyright 2017, Ali Ghaffaari"
__email__ = "ghaffari@mpi-inf.mpg.de"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False)

shell(
    "(vg map {snakemake.params} --threads {snakemake.threads}"
    " -x {snakemake.input.graph} > {snakemake.output.align}) {log}"
)
