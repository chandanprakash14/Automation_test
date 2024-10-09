import os

@then(u'Save it to a text file')
def step_impl(context):
    # Ensure context.data contains the extracted content.
    if not hasattr(context, 'data'):
        raise Exception("No data to save. Please extract the data first.")
    
    extracted_data = context.data  # Assume context.data has been set in a previous step.

    # Define the output file path
    output_file = os.path.join('reports', 'extracted_data.txt')

    # Ensure the reports directory exists
    if not os.path.exists('reports'):
        os.makedirs('reports')

    # Write the extracted data to the file
    with open(output_file, 'w') as file:
        file.write(extracted_data)
    
    print(f'Data saved to {output_file}')
