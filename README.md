# OrthoFilter

A script to remove orthogroups with strange species composition, according to a list of labelled species provided by the user. Input files must be in tsv format. <br> <br>
Orthogroups with only one species present or with larger size but heterogeneous species composition will be removed.

## Arguments
Argument    |  Description             
:-------------:|:-----------------------
-i filename | file w/ gene presence/absence matrix
-l filename | file w/ species and their labels
-o filename | directory to write the output file
-t int | maximum orthogroup size to be checked for species composition 
<br>  
## Example usage

```
python OrthoFilter.py -i /Users/pnatsi/orthology/ortho_matrix.tsv -l /Users/pnatsi/orthology/labels.tsv -o /Users/pnatsi/orthology/ -t 10
```
Will check all orthogroups containing 10 or less species, and keep only the ones which all its species have the same label.

**Careful! Only full paths to the input files are currently supported**

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

