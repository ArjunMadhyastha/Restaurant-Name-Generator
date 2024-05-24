from langchain.chains.llm import LLMChain
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
import os
from dotenv import load_dotenv

load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')


def restaurant_name_generator(cuisine):
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
    llm = HuggingFaceEndpoint(
        repo_id=repo_id,
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN)
    template = ("<s>[INST]I want to open a restaurant for {cuisine} food. Suggest only one fancy name for this. Don't give any description[/INST]")
    prompt_template = PromptTemplate.from_template(template)
    name_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="restaurant_name")

    template2 = ("<s>[INST] Suggest me menu items for {restaurant_name}. Return it as a comma separated list. No need "
                 "of description")
    prompt_template_2 = PromptTemplate.from_template(template2)
    food_chain = LLMChain(llm=llm, prompt=prompt_template_2, output_key="menu_items")

    chain = SequentialChain(chains=[name_chain, food_chain], input_variables=['cuisine'],
                            output_variables=['restaurant_name', 'menu_items'])
    response = chain({'cuisine': cuisine})
    return response


if __name__ == "__main__":
    print(restaurant_name_generator("Arabic"))
