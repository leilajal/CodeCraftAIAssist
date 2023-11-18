import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utility.helpers import *
from utility.prompts import *

def test():
    # Open the random story response. It is used to define the baseline of similarity 
    # between the candidate response and random story.
    with open('resources/random_story.txt', 'r') as f:
        random_story = f.read()

    # Load the coding principles from the json file. This is used to evaluate the candidate response on how
    # it is relevant to the coding principles.
    coding_principles = read_json_file('resources/coding_principles.json')

    llm = OpenAI(temperature = TEMPERTURE, 
                 model = MODEL, 
                 max_tokens = MAX_TOKENS, 
                 openai_api_key = OPENAI_API_KEY)

    # Get random question from the database 
    coding_question = "Evaluate the code generated for CRDs"

    # Get the response from user. In this part I assumed the response is on the youtube video.
    res = get_transcript('CR8Niz9DrWU&t=6s', 'tests/coding.txt')

    # Summarize the candidate response to the question
    summerized_response = summarize_response(res)

    # Create a prompt template to use in langchain

    coding_question_prompt_template = PromptTemplate(
        input_variables =["code_generated","candidate_response"],
        template = coding_question_prompt
    )
    coding_question_query = coding_question_prompt_template.format(
            response = summerized_response,
            code_generated_asked = code_generated
        )

    check_coding_principle_prompt_template = PromptTemplate(
        input_variables =["response", "coding_principles"],
        template = check_principles_promt
    )

    # Create a prompt template to use in langchain for checking how it has coding principles in high level
    check_coding_principle_prompt = check_coding_principle_prompt_template.format(
        candidate_response = summerized_response,
        coding_principles = json.dumps(coding_principles))

    # High level evaluation of the candidate response by AI
    general_evaluation_by_ai_str = llm(coding_question_query)

    # Detailed evaluation of the candidate response by AI
    detailed_evaluation_by_ai_str = llm(check_coding_principle_prompt)
    
    #Save the string to the JSON file
    with open("tests/general_evaluation_by_ai.txt", "w") as f:
        json.dump(general_evaluation_by_ai_str, f, indent=4) 
    f.close()

    with open("tests/detailed_evaluation_by_ai.txt", "w") as f:
        json.dump(detailed_evaluation_by_ai_str, f, indent=4)
    f.close()   

    sorted_candidate_response_similarity_to_coding_principles = calculate_similarity_to_coding_principles(coding_principles, 
                                                                                                                    summerized_response, 
                                                                                                                            random_story)
    plot_horizontal_bar_chart(sorted_candidate_response_similarity_to_coding_principles)

if __name__ == "__main__":
    test()
    print("Done")

