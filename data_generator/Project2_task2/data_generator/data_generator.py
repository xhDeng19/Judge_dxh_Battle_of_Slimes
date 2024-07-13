import subprocess
import glob
import random
import os

#是否加入escape&back的检测（会浪费很多无用行）
IS_ZERO_IN_INPUT = False

#限时10秒（单位为秒）
TIMEOUT = 10

#此.py文件名字长度（含.py三个字符）
NAME_LEN = 17

#随机生成的输入的行数
MAX_RANDOM_LINE = 300

#一轮测评的输入数
MAX_IN_FILE = 10

#间隔多少轮显示一次
SHOW_ROUND_GAP = 100

def random_data_in_file(data_in_files):
    begin = 0 if IS_ZERO_IN_INPUT else 1
    for i in range(1, MAX_IN_FILE + 1):
        lst = random.sample(range(1, 6), 3)
        for _ in range(MAX_RANDOM_LINE - 3):
            lst.append(random.randint(begin, 3))
        
        for file in data_in_files:
            try:
                with open(file, 'w') as in_file:
                    for num in lst:
                        in_file.write(str(num) + '\n')
            except PermissionError:
                continue


def in_current_dir(*name):
    return os.path.join(os.path.dirname(__file__), *name)

def get_data_num(file_dir):
    file_name = os.path.basename(file_dir)
    return int(os.path.splitext(file_name)[0])


def output_your_files(data_in_files, your_out_files, exe_files, score):
    for i in range(MAX_IN_FILE):
        try:
            with open(data_in_files[i], 'r') as input_file, open(your_out_files[i], 'w') as output_file:
                # 输入为 data/*.in 输出为 data/your_output_files.out
                    subprocess.run(exe_files, stdin=input_file, stdout=output_file, stderr=subprocess.PIPE, text=True, timeout=TIMEOUT)

            with open(your_out_files[i], 'r') as score_file:
                lines = score_file.readlines()
                for line_num in range(len(lines) - 1, -1, -1):
                    if "Round" in lines[line_num]:
                        score[i] = int(lines[line_num][6:])
                        break
        except subprocess.TimeoutExpired or PermissionError or TimeoutError or RuntimeError:
            continue

def get_max_score(data_in_files, your_out_files, record_file, scores, round):
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
            
            #记录最多round数的敌方slime类型
            with open(your_out_files[max_score_index], 'r') as output_file:
                line = output_file.readlines()[1]
                slime_type = line.split()[-1][:-1]

            #记录最多round的操作
            with open(data_in_files[max_score_index], 'r') as read_max_score:
                lines_max_score = read_max_score.read()
            with open(in_current_dir('record', f'Max_Score_Operation_score_{max_score}.{slime_type}.in'), 'w') as write_max_score:
                write_max_score.write(lines_max_score)
        except PermissionError:
            return

#初始化
for i in range(MAX_IN_FILE):
    with open(in_current_dir('data', f'{i + 1}.in'), 'w') as f:
        continue

with open(in_current_dir('record', 'record.txt'), 'w') as f:
    f.write("Record Round: 0\nMax Game Score: 0\n\n")

if not os.path.exists(os.path.join(in_current_dir('data'), 'your_output_files')):
    os.makedirs(os.path.join(in_current_dir('data'), 'your_output_files'))     
if not os.path.exists(in_current_dir('compile')):
    os.makedirs(os.path.join(in_current_dir('compile')))  

# 文件目录               
data_in_files = glob.glob(in_current_dir('data', '*.in'))
your_out_files = [in_current_dir(f'data', 'your_output_files', f'{i + 1}.out') for i in range(MAX_IN_FILE)]
record_file = in_current_dir('record', 'record.txt')
cpp_files = glob.glob(in_current_dir('*.cpp'))
exe_files = [os.path.join(in_current_dir('compile'), 'main')]

data_in_files.sort(key=lambda string : get_data_num(string))


if not cpp_files:
    print("No .cpp files found in the current directory")
else:
    # 编译所有的.cpp文件
    compile_result = subprocess.run(['g++', '-o'] + exe_files + cpp_files, capture_output=True, text=True)

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
            output_your_files(data_in_files, your_out_files, exe_files, scores)
            get_max_score(data_in_files, your_out_files, record_file, scores, round)
            round += 1

