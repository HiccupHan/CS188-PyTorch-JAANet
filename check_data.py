import os

def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

def compare_csv_txt_line_counts(csv_folder, txt_folder):
    for csv_file in os.listdir(csv_folder):
        if csv_file.endswith('.csv'):
            csv_path = os.path.join(csv_folder, csv_file)
            txt_file = csv_file.replace('.csv', '.txt')
            txt_path = os.path.join(txt_folder, txt_file)
            if os.path.exists(txt_path):
                csv_line_count = count_lines(csv_path)
                txt_line_count = count_lines(txt_path)
                if txt_line_count != csv_line_count - 1:
                    print(f"Warning: {txt_file} has a different line count compared to its corresponding CSV file.")
            else:
                print(f"Warning: {txt_file} does not exist.")

if __name__ == "__main__":
    csv_folder = './AUCoding'  # Replace this with the path to the folder containing CSV files
    txt_folder = './BP4D-12AUs-txt'  # Replace this with the path to the folder containing TXT files
    compare_csv_txt_line_counts(csv_folder, txt_folder)