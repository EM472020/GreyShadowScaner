import threading

# 全局锁，用于同步输出
print_lock = threading.Lock()

def read_file_lines(file_path):
    """读取文件并返回所有行"""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def process_lines(lines, start, end, thread_id):
    """处理指定范围的行并输出"""
    # 同步输出线程启动信息
    with print_lock:
        print(f"线程 {thread_id} 开始: 处理行 {start} 到 {end-1}")
    
    # 处理指定范围内的每一行
    for i in range(start, end):
        with print_lock:
            print(f"线程 {thread_id}: {lines[i].strip()}")
    
    # 同步输出线程结束信息
    with print_lock:
        print(f"线程 {thread_id} 结束")

def main(file_path, num_threads):
    """主函数，读取文件并创建线程处理"""
    lines = read_file_lines(file_path)
    total_lines = len(lines)
    print(f"总行数: {total_lines}")

    # 计算每个线程处理的基本行数和多余的行数
    base_chunk_size = total_lines // num_threads
    remainder = total_lines % num_threads
    threads = []

    start = 0
    for i in range(num_threads):
        end = start + base_chunk_size
        if i < remainder:
            end += 1

        # 创建并启动线程
        thread = threading.Thread(target=process_lines, args=(lines, start, end, i))
        threads.append(thread)
        thread.start()
        
        start = end

    # 等待所有线程完成
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    file_path = "./burp/admin.txt"  # 这里替换为你的文件路径
    num_threads = 4  # 指定你要创建的线程数
    main(file_path, num_threads)
