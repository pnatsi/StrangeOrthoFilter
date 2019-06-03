import argparse

#HERE STARTS THE ARGUMENT DEFINING
usage = "A program to remove orthogroups with strange species composition from a gene presence/absence matrix. \nPlease provide full paths for every input file!"
toolname = "OrthoFilter"
footer = "Who \n Paschalis Natsidis (p.natsidis@ucl.ac.uk); \n \nWhere \n Telford Lab, UCL;\n\
 ITN IGNITE; \n  \nWhen\n June 2019; \n\n"

parser = argparse.ArgumentParser(description = usage, prog = toolname, epilog = footer, formatter_class=argparse.RawDescriptionHelpFormatter,)
parser.add_argument('-i', metavar = 'filename', dest = 'groups_binary', required = True,
                    help = 'file w/ gene presence/absence matrix (tsv format)')
parser.add_argument('-l', metavar = 'filename', dest = 'labels', required = True,
                    help = 'file w/ species and their labels (tsv format)')
parser.add_argument('-o', metavar = 'filename', dest = 'output', required = True,
                    help = 'directory to write the output alignment file')
parser.add_argument('-t', type=int, metavar = 'int', dest = 'user_threshold', required = True,
                    help = 'maximum orthogroup size to be checked for species composition heterogeneity')

#parser.print_help()

args = parser.parse_args()

#READ FILENAMES FROM USER INPUT
groups_binary_file = args.groups_binary
labels_file = args.labels
output_dir = args.output



#LOAD GENE PRESENCE/ABSENCE MATRIX
f = open(groups_binary_file, "r")
lines = f.readlines()
groups_binary_df = [x.strip().split("\t") for x in lines]
#A LIST OF THE SPECIES INCLUDED IN THE INPUT FILE
species = groups_binary_df[0]

#LOAD LABELS
g = open(labels_file, "r")
lines = g.readlines()
labels = [x.strip().split("\t")[1] for x in lines]



#FIND GROUPS ACCORDING TO THRESHOLD
threshold = args.user_threshold
desired_groups = []

print("\nLooking for groups with " + str(threshold) + " or less species present.")

for group in groups_binary_df[1:]:
    if group.count('1') <= threshold :
        desired_groups.append(group)
        
print("\nFound " + str(len(desired_groups)) + "/" + str(len(groups_binary_df)) + " groups." )
print("Will now check the species composition of these groups")



#GET THE LABELS FOR GROUPS THAT PASSED THE THRESHOLD
desired_groups_labels = []        

for group in desired_groups:
    
    group_id = group[0]
    group_labels = []
    group_labels.append(group_id)
    
    to_look = group[1:]
    
    for i in range(len(to_look)):
        if to_look[i] == '1':
            group_labels.append(labels[i])
    
    desired_groups_labels.append(group_labels) 
    
    
    
    
#CHECK THE COMPOSITION OF LABELS FOR EACH GROUP AND REMOVE GROUPS WITH HETEROGENEOUS COMPOSITION
ids_to_remove = []

for group in desired_groups_labels:
    
    vector_of_labels = group[1:]
    
    #CHECK IF ONLY ONE SPECIES CONTAINED
    if len(vector_of_labels) == 1:
        ids_to_remove.append(group[0])
        
    #CHECK IF SPECIES COMPOSITION IS HETEROGENEOUS    
    most_common_group = max(set(vector_of_labels), key = vector_of_labels.count)
    ratio = vector_of_labels.count(most_common_group)/len(vector_of_labels)
    if ratio < 1 :
        ids_to_remove.append(group[0])
    
print("\nRemoved " + str(len(ids_to_remove)) + " groups (" + 
      str(round(len(ids_to_remove)/len(desired_groups_labels), 2)) + 
      "%) with only one species present or with heterogeneous composition.")
print("\nWill now write the alignment file (this may take a while)")



#WRITE THE PHYLIP ALIGNMENT FILE
groups_to_write = []

for group in groups_binary_df[1:]:
    if group[0] not in ids_to_remove:
        groups_to_write.append(group)

output = open("/Users/wigo/Desktop/projects/xeno_ortho/155_species/filtered_155.phy", "w")

output.write(str(len(species)) + " " + str(len(groups_binary_df) - len(ids_to_remove) - 1) + "\n")

for i in range(len(species)):
    output.write(species[i] + "\t")
    for group in groups_to_write:
        output.write(str(group[i+1]))
    output.write("\n") 

output.close()

print("Alignment file written! Exiting...")
