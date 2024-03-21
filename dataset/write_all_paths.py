import os
import argparse

def find_image_paths(root_dir):
    image_paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            image_paths.append(os.path.join(dirpath, filename).replace('\\', '/'))
    return image_paths

def write_paths_to_file(paths, output_file):
    with open(output_file, 'w') as file:
        for path in paths:
            file.write(path + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parser for file path")
    parser.add_argument('-fp','--foldpath', type=str, default='BP4D/', help="Relative folder path to BP4D images")
    parser.add_argument('-op', '--outputpath', type=str, default="BP4D_combine_path.txt", help="Output file path")
    args = parser.parse_args()

    folder_path = args.foldpath 
    output_file = args.outputpath  

    image_paths = find_image_paths(folder_path)
    print('Number of images: ' + len(image_paths))
    write_paths_to_file(image_paths, output_file)
    print("Image paths written to:", output_file)