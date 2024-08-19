from openai import OpenAI
import base64

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

def openai_table_extraction_to_html(image_path, model="gpt-4o-mini", max_tokens=300):
    client = OpenAI()
    
    # Create message including base64 image information
    message = create_image_message(image_path)

    # Call the OpenAI API to generate HTML code
    response = client.chat.completions.create(
        model=model,
        messages=message,
        max_tokens=max_tokens,
    )
    return response.choices[0].message


# Example usage
image_path = "samples/PMC1626454_002_00.png"
model = "gpt-4o-mini"
response = openai_table_extraction_to_html(image_path)
html_code = response.content
print(html_code)
