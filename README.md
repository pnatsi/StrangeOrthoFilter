# StrangeOrthoRemover

A script to remove orthogroups with strange species composition, according to a list of labelled (by the user) species. <br>
Orthogroups with only one species present or with a larger size but with heterogeneous composition will be removed.

## Arguments
Argument    |  Description             
:-------------:|:-----------------------
-i filename | file w/ gene presence/absence matrix (tsv format)
-o filename | directory to write the output file
-t int | maximum orthogroup size to be checked for species composition 
<br>  


