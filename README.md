# OrthoFilter

A script to remove orthogroups with strange species composition, according to a list of labelled species provided by the user. Input files must be in tsv format. <br> <br>
Orthogroups with only one species present or with larger size but heterogeneous species composition will be removed.

## Arguments
Argument    |  Description             
:-------------:|:-----------------------
-i filename | file w/ gene presence/absence matrix
-o filename | directory to write the output file
-t int | maximum orthogroup size to be checked for species composition 
<br>  

<br>
Who<br> 
 Paschalis Natsidis, PhD candidate (p.natsidis@ucl.ac.uk); <br>
<br>
Where<br>
 Telford Lab, UCL;<br>
 ITN IGNITE; 
<br>
<br>
When<br> 
 May 2019; 

