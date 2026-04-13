# memory-pkm

## 功能描述

- **自动归档**：在重要对话结束后，立即将信息归档到 `knowledge`、`User.md` 和 `MEMORY.md` 中。
- **定期清理**：引入定期清理和整理的机制，自动归档旧信息并删除不再需要的信息。

## 使用方法

1. **自动归档**：
   - 在重要对话结束后，调用 `archive_conversation` 函数将信息归档。
2. **定期清理**：
   - 设置一个定时任务，定期调用 `cleanup_memory` 函数进行清理。

## 代码实现

### 自动归档

```python
import datetime

def archive_conversation(conversation, user_info):
    # 将对话内容写入 knowledge
    with open('memory/knowledge.md', 'a') as f:
        f.write(f"## {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(conversation + "\n\n")

    # 更新 User.md
    with open('memory/User.md', 'a') as f:
        f.write(f"## {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(user_info + "\n\n")

    # 更新 MEMORY.md
    with open('memory/MEMORY.md', 'a') as f:
        f.write(f"## {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(conversation + "\n\n")
```

### 定期清理

```python
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
```

### 定时任务

为了定期执行清理任务，可以使用 `cron` 或其他定时任务工具。以下是一个简单的 `cron` 示例：

```bash
# 每天凌晨 2 点执行清理任务
0 2 * * * /usr/bin/python3 /path/to/cleanup_script.py
```

其中 `cleanup_script.py` 包含上述 `cleanup_memory` 函数的实现。