# This code is for v1 of the openai package: pypi.org/project/openai
import openai
import json
openai.api_key = "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"

def call_gpt(question):
  ans = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            max_tokens=256,
            messages=[
      {"role": "user", "content": question}
    ],
            temperature=0)
            
  returned = ans.choices[0].message.content
  return returned

prompt = ['''This is a simple true and false question, what you should do is simplely judge whether the prompt in the quote is true or false, think step by step and logically and give an '**True**' or '**False**' answer at the end of the answer.. The following four Q&As are example questions:

Question: Is "Muhammad Ali lives longer than Alan Turing" true or false? think step by step and logically and give an '**True**' or '**False**' answer at the end of the answer.
answer is: Let's examine the facts step by step:

1. **Muhammad Ali's birthdate:** January 17, 1942.
2. **Alan Turing's birthdate:** June 23, 1912.

Alan Turing was born before Muhammad Ali.

3. **Muhammad Ali's death date:** June 3, 2016.
4. **Alan Turing's death date:** June 7, 1954.

Muhammad Ali lived from 1942 to 2016, a total of 74 years. Alan Turing lived from 1912 to 1954, a total of 41 years.

Based on this information, the statement "Muhammad Ali lives longer than Alan Turing" is **True.**

Question: Is "The founder of craigslist was born in December 6, 1952" true or false? think step by step and logically and give an '**True**' or '**False**' answer at the end of the answer.
answer is: Let's break down the statement and analyze it step by step:

1. **Founder of Craigslist:** Craig Newmark is the founder of Craigslist.
2. **Craig Newmark's birthdate:** December 6, 1952.

Now, let's compare this birthdate to the statement:

- The statement claims that the founder of Craigslist was born on December 6, 1952, and we established that Craig Newmark is indeed the founder.

Therefore, the statement "The founder of Craigslist was born on December 6, 1952" is **True.**

Question: Is "The maternal grandfather of George Washington? is Joseph Ball" true or false? think step by step and logically and give an '**True**' or '**False**' answer at the end of the answer..
answer is: Let's break down the statement and analyze it step by step:

1. **George Washington:** He was the first President of the United States.
2. **Maternal grandfather of George Washington:** Mary Ball Washington was George Washington's mother.

Now, let's focus on the maternal grandfather:

3. **Maternal grandfather of George Washington:** Joseph Ball.

Therefore, the statement "The maternal grandfather of George Washington is Joseph Ball" is **True.**

Question: Is "Both the directors of Jaws and Casino Royale from the same country?" true or false? think step by step and logically and give an '**True**' or '**False**' answer at the end of the answer.
answer is:Let's break down the statement and analyze it step by step:

1. **Director of Jaws:** Steven Spielberg directed Jaws.
2. **Director of Casino Royale:** Martin Campbell directed Casino Royale.

Now, let's consider their countries of origin:

- **Steven Spielberg:** He is from the United States.
- **Martin Campbell:** He is from New Zealand.

Since Steven Spielberg is from the United States, and Martin Campbell is from New Zealand, they are not from the same country.

Therefore, the statement "Both the directors of Jaws and Casino Royale are from the same country" is **False.**

The True Question is: ''']

# This code is for v1 of the openai package: pypi.org/project/openai
import openai
import json
openai.api_key = "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"

def call_gpt(question):
  ans = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
      {"role": "user", "content": question}
    ],
            temperature=0)
            
  returned = ans.choices[0].message.content
  return returned

question = 0
open('result_3.txt', 'w').close()
open('result_judge_3.txt', 'w').close()
correct = 0
incorrect = 0
indeterminable = 0
with open('hover_dev_release_v1.1.json', 'r') as f:
    data = json.load(f)
for i in range(820,830):
    question = prompt[0] + 'Is" ' + data[i]['claim'][:-1] + '" true or false? think step by step and logically and give an "**True**" or "**False**" answer at the end of the answer.'
    
    answer = data[i]['label']
    if answer == 'SUPPORTED':
        answer = 'true'
    else:
        answer = 'false'
        
    with open('result_3.txt', "a") as file:
        file.write('\n')
        file.write('question: ' + 'Is" ' + data[i]['claim'][:-1] + '" true or false? think step by step and logically and give an "True" or "False" answer at the end of the answer.' + '\n')   
        ret = call_gpt(question)
        file.write('answer: ' + ret + '\n')
    
    with open('result_judge_3.txt', "a") as fileb:

        if 'indeterminable' in (ret.lower())[-30:] or 'indeterminate' in (ret.lower())[-30:] or 'true or false' in (ret.lower())[-30:]:
            fileb.write('Indeterminable' + '\n')
            indeterminable += 1
        elif answer in (ret.lower())[-30:]:
            fileb.write('True' + '\n')
            correct += 1
        else:
            fileb.write('False' + '\n')
            incorrect += 1
with open('result_judge_3.txt', "a") as fileb:
    fileb.write('True:' + str(correct) + '\n')
    fileb.write('False:' + str(incorrect) + '\n')
    fileb.write('Indeterminable:' + str(indeterminable) + '\n')
