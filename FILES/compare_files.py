import difflib

def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

    differ = difflib.Differ()
    diff = list(differ.compare(file1_lines, file2_lines))
    
    for line in diff:
        print(line)

# Replace 'file1.txt' and 'file2.txt' with the paths to your files
compare_files('proposals/roof_install_contract-Andrew’s MacBook Pro.html', 'proposals/roof_install_contract.html')
