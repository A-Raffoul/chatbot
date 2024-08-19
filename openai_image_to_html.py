from openai import OpenAI
import base64
import torch

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def create_image_message(image_path):
    base64_image = encode_image(image_path)
    message = [
        {
            'role': 'system', 
            'content': 'You are a professional table analyser, reproduce the given table in HTML code. only give the HTML code.'},
        {
            'role': 'user',
            'content' : [
                {
                    'type': 'image_url',
                    'image_url': {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ]
    return message

def openai_table_extraction_to_html(image_path, model="gpt-4o-mini", max_tokens=3000):
    client = OpenAI()
    
    # Create message including base64 image information
    message = create_image_message(image_path)

    # Call the OpenAI API to generate HTML code
    response = client.chat.completions.create(
        model=model,
        messages=message,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


def html_to_info(html_code, query, model="gpt-4o-mini", max_tokens=300):
    # Use the HTML code to give context to LLM

    client = OpenAI()

    message = [
        {
            'role': 'system', 
            'content': "You are a professional table analyser, you will receive an HTML code for a table, I need you to go \
                        through it and understand it thouroughly. You give me a brief summary of the table about the information \
                        it contains, this summary will be used later to answer a query about the table Answer the query as short as possible. \
                        The lower the word count, the better. \
                        Always verify the information in the table before answering the query. \
                        The message will first contain a query about the table, then after the |###| symbol, the HTML code will be provided."
        },
        {
            'role': 'user',
            'content' : f"Query : {query} \
                        |###| \
                        {html_code}"
        }
    ]

    response = client.chat.completions.create(
        model=model,
        messages=message,
        max_tokens=max_tokens,
    )

    return response.choices[0].message.content

# Example usage
image_path = "samples/PMC1626454_002_00.png"
model = "gpt-4o-mini"
html_code = openai_table_extraction_to_html(image_path)
# print(html_code)
# query = "How many rows and columns are there in the table?"
# query = "What is the title of the table? \
#         What is highest value in the table? \
#         Is there any Merged cells in the table? If yes then which indices?\
#             What is the total number of cells in the table? "
query = 'with which statement does  lay persons disagree with the most? extract the statement and the number of people who disagree with it.make sure to use the correct column to extract the info'
response = html_to_info(html_code, query)
print(response)
