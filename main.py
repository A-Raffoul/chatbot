import openai_image_to_html
import display 


# Image Extraction Tool : openai_api, llama3_api, tesseract_ocr, paddle_ocr
image_to_html_tool = 'openai_api'
# HTML Extraction Tool : openai_api, llama3_api, 
html_to_info_tool = 'openai_api'
 
# Image path
image_path = "samples/PMC1626454_002_00.png"


#  Call the function to extract the HTML code from the image
html_code = openai_image_to_html.openai_table_extraction_to_html(image_path)

# Save the HTML code to a file debug
with open('output.txt', 'w') as file:
    file.write(html_code)
intermediate_output, table_html = html_code.split("###")


# Use HTML code to give context LLM
query = "What is the size of the table (rows, columns), what are the main headers, summarize the information in the table explain its structure"
response = openai_image_to_html.html_to_info(html_code, query)



html_data = {
    'image_path': image_path,
    'intermediate_output': intermediate_output,
    'table_html': table_html,
    'query': query,
    'query_answer': response
}

display.create_html_page(html_data, 'output.html')


# Use the context to answer original query

