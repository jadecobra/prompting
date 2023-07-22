!pip install langchain==0.0.26
!pip install openai

import langchain.llms
import os

os.environ['OPENAI_API_KEY'] = "sk-YOUR_KEY_HERE"

llm = langchain.llms.OpenAI(
    model_name='text-davinci-002',
    temperature=0
)

MATH_PROMPT = '''
Q: There were nine computers in the server room.
Five more computers were installed each day, from monday to thursday.
How many computers are now in the server room?

# solution in Python:
"""There were nine computers in the server room.
Five more computers were installed each day from monday to thursday.
How many computers are now in the server room?"""
computers_initial=9
computers_per_day=5
num_days = 4 # 4 days between monday and thrusday
computers_added = computers_per_day * num_days
computers_total = computers_initial + computers_added
result = computers_total
return result

Q: Shawn has five toys.
For christmas, he got two toys each from his mom and dad.
How many toys does he have now?

# solution in Python:
"""Shawn has five toys.
For christmas, he got two toys each from his mom and dad.
How many toys does he have now?"""
toys_initial = 5
mom_toys = 2
dad_toys = 2
total_received = mom_toys + dad_toys
total_toys = toys_initial + total_received
result = total_toys

Q: Jason had 20 lollipops.
He gave Denny some lollipops.
Now Jason has 12 lollipops.
How many lollipops did Jason give to Denny?

# solution in Python:
"""Jason had 20 lollipops.
He gave Denny some lollipops.
Now Jason has 12 lollipops.
How many lollipops did Jason give to Denny?"""
jason_lollipops_initial = 20
jason_lollipops_after = 12
denny_lolliposp = jason_lollipops_initial - jason_lollipops_after
result = denny_lollipops

Q: {question}

# solution in Python:
'''

question = """Emma took a 60 minute plane ride to seattle.
She then took a 2 hour train ride to portland,
and then a 30 minute bus ride to vancouver.
How long did it take her to get to vancouver?"""

print(llm(MATH_PROMPT.format(question=question)))