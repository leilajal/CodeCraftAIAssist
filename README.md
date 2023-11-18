# coding-gpt

This repository contains a collection of notebooks and associated code components designed for the GPT-powered Kubernetes Coding Assitance, specifically tailored to serve as a CRDs, and YAML configuration files.

## Repository Structure

The repository is structured as follows:

- `resources/`: It contains imporatnt files related to the application.
    1. 'conf.env/': contains important configuration. You need to update your openAI key to work.
    2. 'coding_generated.db': db that contains question. It is SQLite db
    3. 'coding_description.txt': sample coding results that we used in test.py and notebook
    4. 'coding_principles.json': It contains coding principles in json format. 
    5. 'random_story.txt': it is a random story which is used as the basedline for comparing similarity to coding principles.
    6. 'sample_codes.txt': You can add more question to this file in the newline. It will be automatically loaded to question db.
    7. 'sample_questions.txt': You can add more samples to this file in the newline. It will be automatically loaded to question db. 
    8. 'sample_.txt': You can add more examples to this file in the newline. It will be automatically loaded to samples db.  
- `coachgpt-app.py/`: gradio app to run.
- 'utility/'
    1. 'helpers.py/`: Helper functions and classes that are needed.
    2. 'prompts.py/`: Related prompt for this project.
- 'tests/'
    1.  'test.py/`: test function which is using a youtube mock coding for the question of 'Tell me about the time that you solved constumer problem.

## Getting Started

To get started with the application, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip3 install -r requirements.txt`.
3. Add your openAI key to .env file
4. Start the Flask web server by running `python3 coachgpt-poc.py`.
5. Open your web browser and navigate to ` http://127.0.0.1:7860` to use the application.





