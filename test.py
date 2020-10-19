import subprocess
import sys
import glob

def run_command(command):
    proc = subprocess.Popen(command, 
                            stdout=subprocess.PIPE, 
                            stderr= subprocess.PIPE, 
                            shell=True,
                            universal_newlines=True)
    
    std_out, std_err = proc.communicate()
    return proc.returncode, std_out, std_err

def main(command, input_prefix, result_prefix):
    input_files = glob.glob(f'{input_prefix}*')
    
    test_files = { file_name[len(input_prefix):]: 
                    [file_name,] 
                       for file_name in input_files }

    for id, files in test_files.items():
        files.append(f'{result_prefix}{id}')
    
    for file, output_file in test_files.values():
        result_obtained = run_command(f'{command} < {file}')[1]
        expected_result = run_command(f'cat {output_file}')[1]
        
        

        print(result_obtained == expected_result)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        command, input_prefix, result_prefix = sys.argv[1:]
        main(command, input_prefix, result_prefix)
    else:
        print("""
        Use: python test.py command input_prefix result_prefix
        command: comando a ejecutar.
        input_prefix: prefijo de los archivos que se usaran como entrada.
        result_prefix: prefijo de los archivos a comparar.
        """)
