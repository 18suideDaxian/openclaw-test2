import os
from datetime import datetime, timedelta

def cleanup_memory(days_to_keep=30):
    # 获取当前时间
    now = datetime.now()
    
    # 遍历 knowledge 文件，删除超过指定天数的内容
    with open('memory/knowledge.md', 'r') as f:
        lines = f.readlines()
    
    with open('memory/knowledge.md', 'w') as f:
        for line in lines:
            if line.startswith("## "):
                date_str = line[3:].strip()
                entry_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                if (now - entry_date) < timedelta(days=days_to_keep):
                    f.write(line)
            else:
                f.write(line)
    
    # 同样的逻辑应用于 User.md 和 MEMORY.md
    for file_name in ['memory/User.md', 'memory/MEMORY.md']:
        with open(file_name, 'r') as f:
            lines = f.readlines()
        
        with open(file_name, 'w') as f:
            for line in lines:
                if line.startswith("## "):
                    date_str = line[3:].strip()
                    entry_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                    if (now - entry_date) < timedelta(days=days_to_keep):
                        f.write(line)
                else:
                    f.write(line)

if __name__ == "__main__":
    cleanup_memory(days_to_keep=30)