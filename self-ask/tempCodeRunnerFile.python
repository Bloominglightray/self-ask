import json

def sort_json_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        data = json.load(file)
    
    # 对 JSON 数据进行排序
    sorted_list = sorted(data, key=lambda x: x['num_hops'])
    
    sorted_data = json.dumps(sorted_list, indent=4)
    
    # 将排序后的数据写回文件
    with open(output_file_path, 'w') as output_file:
        output_file.write(sorted_data)


# 示例用法
input_file_path = 'hover_dev_release_v1.1.json'  # 替换为你的输入文件路径
output_file_path = 'hover_dev_sorted_output.json'  # 替换为你的输出文件路径

sort_json_file(input_file_path, output_file_path)