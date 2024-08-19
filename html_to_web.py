import webbrowser

# Assuming `html_code` is your generated HTML code
html_code = "<h1>Hello, World!</h1>"

# Save the HTML code to a file
with open("output.html", "w") as file:
    file.write(html_code)

# Open the HTML file in the default web browser
