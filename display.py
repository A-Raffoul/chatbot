
def create_html_page(info, output_file):
    
    html_template = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Table Page</title>
    </head>
    <body>
    <h1>Table image</h1>
        <img src="{info['image_path']}" alt="Table Image">

    <h2>Table HTML</h2>
        {info['table_html']}

    <h2>Table Information (LLM intermediate step)</h2>
        {info['intermediate_output']}

    <h2>Query</h2>
        {info['query']}
    <h3>Query Answer</h3>
        {info['query_answer']}
    </body>
    </html>
    '''

    with open(output_file, 'w') as file:
        file.write(html_template)




