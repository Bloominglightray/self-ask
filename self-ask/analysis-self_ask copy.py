import re
import json

def extract_text_between_keywords(input_text, start_keyword, end_keyword):
    pattern = re.compile(f'{re.escape(start_keyword)}(.*?){re.escape(end_keyword)}')
    match = pattern.search(input_text)
    
    if match:
        return match.group(1)
    else:
        return None


start = 400
# The input string
open('result_analysis_self_ask.json', "w").close()
with open('result_self_ask.json', 'r') as f:
    data = json.load(f)
with open('hover_dev_release_v1.1.json', 'r') as g:
    data_2 = json.load(g)
answer1 = []
for i in range(len(data)-3):
    input_string = str(data[i]["process"])

    # Define a regular expression pattern to match text inside ** and **
    start_keyword = "Intermediate answer:"
    end_keyword = "is"
    # Find all matches in the input string
    matches = extract_text_between_keywords(input_string, start_keyword, end_keyword)
    # Output the results
    with open('result_analysis_self_ask.json', "a") as fileb:
        answer = []
        for k, match in enumerate(matches, start=1):
            answer.append(match.strip())
        judge = {}
        judge['question'] = data[i]['question']
        judge['process'] = answer
        judge['judge'] = data[i]['judge']
        judge['database_supporting_facts'] = data_2[start+i]['supporting_facts']
        
        fit = 0
        for j in judge['database_supporting_facts']:
            for p in judge['process']:
                if j[0] in p:
                    fit += 1
                    break
        judge['fit'] = fit    
        answer1.append(judge)  

with open('result_analysis_self_ask.json', "a") as fileb:
    json.dump(answer1, fileb, indent=2)
    
with open('result_analysis_self_ask.json', 'r') as f:
    data = json.load(f)
    false_analysis = []
    for i in data:
        if i['judge'] == 'False':
            false_analysis.append(i)
    for i in data:
        if i['judge'] == 'Indeterminable':
            false_analysis.append(i)
            
with open('false_analysis_self_ask.json', "w") as filec:
    json.dump(false_analysis, filec, indent=2)

    
    
