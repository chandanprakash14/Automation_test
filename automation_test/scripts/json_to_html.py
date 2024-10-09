import os
import json


def json_to_html(json_file, html_file):
    # Open and load the JSON report
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Open the HTML file for writing
    with open(html_file, 'w') as f:
        f.write("<html><head><title>Behave Report</title></head><body>")
        f.write("<h1>Behave Test Report</h1>")
        
        # Loop through features and scenarios
        for feature in data:
            f.write(f"<h2>Feature: {feature['name']}</h2>")
            f.write(f"<p>Description: {feature.get('description', 'No description')}</p>")
            for element in feature['elements']:
                f.write(f"<h3>Scenario: {element['name']}</h3>")
                f.write("<ul>")
                for step in element['steps']:
                    status = step['result']['status']
                    f.write(f"<li>{step['keyword']} {step['name']}: {status}</li>")
                f.write("</ul>")
        
        f.write("</body></html>")

# Set file paths
json_report = os.path.join('reports', 'report.json')
html_report = os.path.join('reports', 'report.html')

# Convert JSON report to HTML
json_to_html(json_report, html_report)
