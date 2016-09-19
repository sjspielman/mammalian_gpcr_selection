## Repository for Data in ["Membrane environment imposes unique selection pressures on transmembrane domains of G-protein coupled receptors"](http://link.springer.com/article/10.1007/s00239-012-9538-8)

### Contents of repository

Of primary interest are alignments and trees:
* `guidance_aln_nuc/` and `guidance_aln_prot/` contain respectively codon and amino-acid alignments (they correspond), with sites filtered based on Guidance algorithm
* `unaligned_sequences/` contain raw sequences (unaligned fasta files) for each ortholog
* `trees/` contains all RAxML-inferred trees. All files "*bl\_bs.tre" contain bootstrap and branch lengths, whereas other files are just topology
* `structures/` contains transmembrane predictions for GPCRHMM

* `partitioned_alignments/` contains same data as in `guidance_aln_nuc/` except partitioned into extramembrane and transmembrane, based on predictions found in `structures/`. Files named as:
   * `*_extra.fasta` are extramembrane (intra and extracellular) domains
   * `*_inner.fasta` are intracellular domains
   * `*_outer.fasta` are extracellular domains
   * `*_trans.fasta` are transmembrane domains
   * `*_genome.fasta` are full sequences (ie unpartitioned)

Other contents:
* `InitialGeneSet/` contains Ensembl and GO annotations for original data collection. Note, many of these sequences end up not being used because they were not GPCRs.
* `dssp_files/` contains structural information predicted with DSSP for known GPCR structures in this study
* `hyphy/` contains results summaries for models tested, including AIC for no partitioning (null\_results.txt), AIC for 2 vs 3 partition schemes (2vs3\_partitions\_results.txt) and mean evo rates using best model (rel\_results.txt)
