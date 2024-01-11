import re
import json

start = 400
# The input string
open('result_analysis_4.json', "w").close()
with open('result_4.json', 'r') as f:
    data = json.load(f)
with open('hover_dev_release_v1.1.json', 'r') as g:
    data_2 = json.load(g)
answer1 = []
for i in range(len(data)):
    input_string = data[i]['answer']

    # Define a regular expression pattern to match text inside ** and **
    pattern = re.compile(r'\*\*(.*?)\:\*\*')

    # Find all matches in the input string
    matches = re.findall(pattern, input_string)

    # Output the results
    with open('result_analysis_4.json', "a") as fileb:
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

with open('result_analysis_4.json', "a") as fileb:
    json.dump(answer1, fileb, indent=2)
            

# with open('hover_dev_release_v1.1.json', 'r') as g:
#     data_2 = json.load(g)
# for i in range(400,430):
    
    
