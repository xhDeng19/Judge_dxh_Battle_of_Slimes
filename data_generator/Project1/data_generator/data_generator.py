import subprocess
import glob
import sys
import random

#限时10秒（单位为秒）
TIMEOUT = 10

#此.py文件名字长度（含.py三个字符）
NAME_LEN = 17

#随机生成的输入的行数
MAX_RANDOM_LINE = 200

#一轮测评的输入数
MAX_IN_FILE = 10

#间隔多少轮显示一次
SHOW_ROUND_GAP = 100

def random_data_in_file(data_in_files):
    for i in range(1, MAX_IN_FILE + 1):
        lst = []
        for _ in range(MAX_RANDOM_LINE):
            lst.append(random.randint(1, 3))
        
        for file in data_in_files:
            try:
                with open(file, 'w') as in_file:
                    for num in lst:
                        in_file.write(str(num) + '\n')
            except PermissionError:
                continue


def in_current_dir(name):
    return sys.argv[0][:-NAME_LEN] + name

def get_data_num(file_dir):
    index_dir = file_dir.rfind('\\')
    index_name = file_dir.rfind('.')
    return int(file_dir[index_dir + 1: index_name])


def output_your_files(data_in_files, your_out_files, score):
    for i in range(MAX_IN_FILE):
        try:
            with open(data_in_files[i], 'r') as input_file, open(your_out_files[i], 'w') as output_file:
                # 输入为 data/*.in 输出为 data/your_output_files.out
                    subprocess.run(['.\\main'], stdin=input_file, stdout=output_file, stderr=subprocess.PIPE, text=True, timeout=TIMEOUT)
                
            with open(your_out_files[i], 'r') as score_file:
                lines = score_file.readlines()
                for line_num in range(len(lines) - 1, -1, -1):
                    if "Round" in lines[line_num]:
                        score[i] = int(lines[line_num][6:])
                        break
        except PermissionError or TimeoutError or RuntimeError:
            continue

def get_max_score(data_in_files, record_file, scores, round):
    try:
        with open(record_file, 'r') as record_file_content:
            lines = record_file_content.readlines()
            for line in reversed(lines):
                if "Max Game Score" in line:
                    max_score = int(line[16:])
                    break
    except PermissionError:
        return
    
    isGreaterThanRecord = False

    for score_index in range(len(scores)):
        if scores[score_index] > max_score:
            max_score = scores[score_index]
            max_score_index = score_index
            isGreaterThanRecord = True
    
    if isGreaterThanRecord:
        try:
            #记录最多的round数
            with open(record_file, 'a') as recore_file_append:
                recore_file_append.write(f"Record Round: {round}\nMax Game Score: {max_score}\n\n")
            
            #记录最多round的操作
            with open(data_in_files[max_score_index], 'r') as read_max_score:
                lines_max_score = read_max_score.read()
            with open(in_current_dir(f"record\\Max_Score_Operation_score_{max_score}.in"), 'w') as write_max_score:
                write_max_score.write(lines_max_score)
        except PermissionError:
            return

#初始化
for i in range(MAX_IN_FILE):
    with open(in_current_dir(f'data\\{i + 1}.in'), 'w') as f:
        continue

with open(in_current_dir('record\\record.txt'), 'w') as f:
    f.write("Record Round: 0\nMax Game Score: 0\n\n")

# 文件目录               
data_in_files = glob.glob(in_current_dir('data\\*.in'))
your_out_files = [in_current_dir(f'data\\your_output_files\\{i + 1}.out') for i in range(MAX_IN_FILE)]
record_file = in_current_dir('record\\record.txt')
cpp_files = glob.glob(in_current_dir('*.cpp'))

data_in_files.sort(key=lambda string : get_data_num(string))
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
        round = 1
        while(True):
            
            # cmd上显示的内容
            if round % SHOW_ROUND_GAP == 0:
                print(f"Current round: {round}")
                try:
                    with open(record_file, 'r') as record_file_content:
                        lines = record_file_content.readlines()
                        for line in reversed(lines):
                            if "Max Game Score" in line:
                                print(line + "\n\n")
                                break
                except PermissionError:
                    continue
            
            scores = [0 for _ in range(MAX_IN_FILE)]
            random_data_in_file(data_in_files)
            output_your_files(data_in_files, your_out_files, scores)
            get_max_score(data_in_files, record_file, scores, round)
            round += 1

