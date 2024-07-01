import subprocess
import glob
import sys

#限时2秒（单位为秒）
TIMEOUT = 2

#此.py文件名字长度
NAME_LEN = 12

def in_current_dir(name):
    return sys.argv[0][:-NAME_LEN] + name

def get_data_num(file_dir):
    index_dir = file_dir.rfind('\\')
    index_name = file_dir.rfind('.')
    return int(file_dir[index_dir + 1: index_name])


def output_your_files(data_in_files, your_out_files):
    for i in range(len(data_in_files)):
        with open(data_in_files[i], 'r') as input_file, open(your_out_files[i], 'w') as output_file:
            # 输入为 data/*.in 输出为 data/your_output_files.out
            try:
                run_result = subprocess.run(['.\\main'], stdin=input_file, stdout=output_file, stderr=subprocess.PIPE, text=True, timeout=TIMEOUT)
                if run_result.returncode != 0:
                    print(f"{i + 1}.in failed in execution!")
                    print(run_result.stderr)
            except subprocess.TimeoutExpired:
                continue
            

def compare_files(data_out_files, your_out_files):
    for i in range(len(data_out_files)):
        # 比较 data/*out.out 与 data/your_output_files.out
        with open(data_out_files[i], 'r') as fstandard, open(your_out_files[i], 'r') as fyours:
            standard_content = fstandard.read()
            your_content = fyours.read()

            if (standard_content == your_content):
                print(f"{i + 1}.out is correct.")
            else:
                print(f"{i + 1}.out is WRONG. Compare data\\{i + 1}.out and data\\your_output_files\\{i + 1}.out to find out.")   



# 文件目录               
data_in_files = glob.glob(in_current_dir('data\\*.in'))
data_out_files = [in_current_dir(f'data\\{i + 1}.out') for i in range(len(data_in_files))]
your_out_files = [in_current_dir(f'data\\your_output_files\\{i + 1}.out') for i in range(len(data_in_files))]
cpp_files = glob.glob(in_current_dir('*.cpp'))

data_in_files.sort(key=lambda string : get_data_num(string))
data_out_files.sort(key=lambda string : get_data_num(string))
your_out_files.sort(key=lambda string : get_data_num(string))


if not cpp_files:
    print("No .cpp files found in the current directory")
else:
    # 编译所有的.cpp文件
    compile_result = subprocess.run(['g++', '-o', 'main'] + cpp_files, capture_output=True, text=True)

    if compile_result.returncode != 0:
        #编译失败
        print("Compilation failed")
        print(compile_result.stderr)
    else:
        #编译成功
        output_your_files(data_in_files, your_out_files)
        compare_files(data_out_files, your_out_files)
