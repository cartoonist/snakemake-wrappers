__author__ = "Ali Ghaffaari"
__copyright__ = "Copyright 2018, Ali Ghaffaari"
__email__ = "ghaffari@mpi-inf.mpg.de"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell()

shell(
    "(seq2any {snakemake.params} {snakemake.input.seq}"
    " {snakemake.output.seq}) {log}"
)
