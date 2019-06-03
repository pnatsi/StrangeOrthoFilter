# StrangeOrthoRemover

A script to remove orthogroups with strange species composition, according to a list of labelled (by the user) species. <br>
For example, an orthogroup with one protostome and one ctenophore gene makes no sense biologically, thus it should be dismissed from further analysis. 

## Arguments
Argument    |  Description             
:-------------:|:-----------------------
-i filename | file w/ gene presence/absence matrix (tsv format)
-o filename | directory to write the output file
-t int | maximum orthogroup size to be checked for species composition heterogeneity
<br>  

For example, `-t 10` will check all groups containing up to 10 species, and will keep only the groups with all species from the same user-defined group (e.g. a group with 8 species, all Deuterostomes)
