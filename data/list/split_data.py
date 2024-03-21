output_file = 'BP4D_combine_path.txt'
output_part_1_2_file = 'BP4D_combine_1_2_path.txt'
output_part_3_file = 'BP4D_part_3_path.txt'
def read_txt_files():
    data = open(output_file).readlines()    
    with open(output_part_1_2_file, 'w') as outfile:
        for i in range(83924):
            outfile.write(data[i])
    with open(output_part_3_file, 'w') as outfile:
        for i in range(83924, 125884):
            outfile.write(data[i])
read_txt_files()