import subprocess
import glob
import os
import time
from tqdm import tqdm

#限时2秒（单位为秒）
TIMEOUT = 2

#如果c++输出随机数种子使用的是std::time(0), 则需间隔1s检测一次
SLEEP_TIME = 1

#检测敌方史莱姆多少轮
EXE_MAX_ROUND = 20

def in_current_dir(*name):
    return os.path.join(os.path.dirname(__file__), *name)

# 1.Yellow.in -> 1
def get_data_num(file_dir):
    file_name = os.path.basename(file_dir)
    return int(os.path.splitext(os.path.splitext(file_name)[0])[0])

# 1.Yellow.in -> Yellow
def get_enemy_slime_type(file_dir):
    file_name = os.path.basename(file_dir)
    return os.path.splitext(os.path.splitext(file_name)[0])[1][1:]

# 1.Yellow.in -> 1.Yellow
def get_name(file_dir):
    file_name = os.path.basename(file_dir)
    return os.path.splitext(file_name)[0]

def output_your_files(data_in_files, your_out_files, exe_files):
    data_length = len(data_in_files)
    isCorrectSlimeType = [False] * data_length
    
    with tqdm(total=len(isCorrectSlimeType), desc="Progress", unit="output") as pbar:

        for exe_rounds in range(EXE_MAX_ROUND):
            pbar.n = sum(isCorrectSlimeType)
            pbar.refresh()
            #print(f"{exe_rounds=}")
            #print(f"{isCorrectSlimeType=}")

            if all(isCorrectSlimeType):
                break

            for i in range(data_length):
                isTimeOut = False
                if isCorrectSlimeType[i]:
                    continue

                with open(data_in_files[i], 'r') as input_file, open(your_out_files[i], 'w') as output_file:
                    # 输入为 data/*.in 输出为 data/your_output_files.out
                    try:
                        run_result = subprocess.run(exe_files, stdin=input_file, stdout=output_file, stderr=subprocess.PIPE, text=True, timeout=TIMEOUT)
                        if run_result.returncode != 0:
                            print(f"{get_name(data_in_files[i])}.in failed in execution!")
                            print(run_result.stderr)
                    except subprocess.TimeoutExpired:
                        isTimeOut = True
                
                if isTimeOut:
                    with open(your_out_files[i], 'w') as output_file:
                        output_file.write("Time Out!")
                    continue
            
                with open(your_out_files[i], 'r') as check_enemy_slime_file:
                    line = check_enemy_slime_file.readlines()[1]
                    slime_type = line.split()[-1][:-1]
                    if get_enemy_slime_type(your_out_files[i]) == slime_type:
                        isCorrectSlimeType[i] = True

            time.sleep(SLEEP_TIME)
            #print(f'{i=}', f'{slime_type=}')

    for i in range(data_length):
        if not isCorrectSlimeType[i]:
            with open(your_out_files[i], 'w') as output_file:
                output_file.write("There's a great chance that the enemy didn't randomly select their slime with a uniform probability. You can try judge_dxh.py again to check that.")


def compare_files(data_out_files, your_out_files):
    for i in range(len(data_out_files)):
        # 比较 data/*.out 与 data/your_output_files/*.out
        with open(data_out_files[i], 'r') as fstandard, open(your_out_files[i], 'r') as fyours:
            standard_content = fstandard.readlines()
            your_content = fyours.readlines()
            #del_hp_print(your_content) #放弃检测第一次hp输出和平局的最后一次hp输出（Task?.exe的bug）
            isCorrect = True

            for line_i in range(min(len(standard_content), len(your_content))):
                if line_i == 1: #不用管敌方史莱姆的出场顺序
                    continue

                if standard_content[line_i] != your_content[line_i]:
                    if isCorrect:
                        print(f"{get_name(data_out_files[i])}.out is WRONG. Compare {os.path.join('data', f'{get_name(data_out_files[i])}.out')} and {os.path.join('data', 'your_output_files', f'{get_name(data_out_files[i])}.out')} to find out.")
                        print("\nDetail:") 
                    print(f"line {line_i + 1}: ")
                    print(f"Correct answer: {standard_content[line_i]}")
                    print(f"Your answer: {your_content[line_i]}")
                    print("\n")
                    isCorrect = False

            if (isCorrect and len(standard_content) == len(your_content)):
                print(f"{get_name(data_out_files[i])}.out is correct.")
            elif (isCorrect):
                print(f"{get_name(data_out_files[i])}.out is WRONG. Compare {os.path.join('data', f'{get_name(data_out_files[i])}.out')} and {os.path.join('data', 'your_output_files', f'{get_name(data_out_files[i])}.out')} to find out.")
                        
#初始化
if not os.path.exists(in_current_dir('data', 'your_output_files')):
    os.makedirs(in_current_dir('data', 'your_output_files'))     
if not os.path.exists(in_current_dir('compile')):
    os.makedirs(in_current_dir('compile'))    


# 文件目录               
data_in_files = glob.glob(in_current_dir('data', '*.in'))
data_in_files.sort(key=lambda string : get_data_num(string))

data_out_files = [in_current_dir('data', get_name(file_dir) + '.out') for file_dir in data_in_files]
your_out_files = [in_current_dir('data', 'your_output_files', get_name(file_dir) + '.out') for file_dir in data_in_files]

cpp_files = glob.glob(in_current_dir('*.cpp'))
exe_files = [in_current_dir('compile', 'main')]


if not cpp_files:
    print("No .cpp files found in the current directory")
else:
    # 编译所有的.cpp文件 (启用c++11标准)
    compile_result = subprocess.run(['g++', '-std=c++11', '-o'] + exe_files + cpp_files, capture_output=True, text=True)

    if compile_result.returncode != 0:
        #编译失败
        print("Compilation failed")
        print(compile_result.stderr)
    else:
        #编译成功
        try:
            output_your_files(data_in_files, your_out_files, exe_files)
            compare_files(data_out_files, your_out_files)
        except MemoryError:
            print("Try Again!")
