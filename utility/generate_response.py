question_prompt = ''' Please complete the code {question_asked}.
Here is the summarized response: {response}

Question: How do you evaluate the generated code?

Instructions:

Please use the following template for your response:

Your general ranking should be only one of these choices:

1) Weak, 
2) Average, 
3) Good,
4) Excellent

With the Explanation of your ranking. Create a response like the following format:

Ranking: Weak; 
AI-Explanation: your explanation
'''

b_check_principles_promt ='''
Here is the sumerized response: {candidate_response}

Context: we have different ltemplates that we want to evaluate the code response against.
Here is the list of  principles represented as a json string. 

Question : Is code relevant to this principles?.

Instructions:
1) Validate your answer by highlighting the related text extracted from the candidate response.
2) Use the format of principle name and your answer.
3) Use all the principles in your answer.

For example, if you think the candidate response is relevant to the  principle "CRD Template", then your answer 
should look like the template: your answer. If it is not relevant to principles, then write 'AI-could not get 
specific evidence in answer'. 

Create a response like the follwoing format:

1- Principle Name;
AI-Explanation: your answer;
----------------------------------------------------------------------------------------------------
2- Principle Name;
AI-Explanation: your answer;
----------------------------------------------------------------------------------------------------
...
'''

b_ai_answer_promt ='''
Consider the code for CRDs. 
We ask you question : {interview_question_asked}

c_question_prompt = ''' We asked a uestion of {interview_question_asked}.
Here is the summarized response: {response}

Question: How do you evaluate coding response?

Instructions:

1) It should contains CRD templates.
2) How the fields are written. Does it follow the best practices?
3) Does the code solve the problem?
4) Does code have good level of comments and explaination?

Please use the following template for your response:

Your general ranking should be only one of these choices:

1) Weak, 
2) Average, 
3) Good,
4) Excellent

With the Explanation of your ranking. Create a response like the following format:

Ranking: Weak; 
AI-Explanation: your explanation
'''

c_ai_answer_promt ='''
We ask you a coding evaluation : {question_asked}

Please answer the mentioned coding question based on the following instructions:

1) Write a code with a simple test that works.
2) Explain the code.
3) Your Response should be less than 4000 words.

Create a response like the following format:

Code: your code
AI-Explanation: your explanation
'''

ms_interview_question_prompt = ''' We asked a candidate to evaluate the question of {question_asked}.
Here is the summarized response: {candidate_response}

Question: How do you evaluate the candidate's response?

Instructions:

1) It should contains important blocks of CRD components.
2) It should contains important fields that are used in CRDs.
3) It should talk about important metrics.
4) It should talk about important features used.

Please use the following template for your response:

Your general ranking should be only one of these choices:

1) Weak, 
2) Average, 
3) Good,
4) Excellent

With the Explanation of your ranking. Create a response like the following format:

Ranking: Weak; 
AI-Explanation: your explanation
'''

ms_ai_answer_promt ='''
We ask you the following coding evaluation question : {question_asked}


Create a response like the following format:

Important components: your explanation
Important metrics for system evaluation: your explanation
Important features: your explanation
'''
