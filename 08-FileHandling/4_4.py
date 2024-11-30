def display_lines(file_name):
    # Open the file in read mode
    with open(file_name, 'r') as file:
        lines = file.readlines()  # Read all lines from the file
        
    # Define the number of lines to display at a time
    total_lines = len(lines)
    current_line = 0
    
    while current_line < total_lines:
        # Display the next 5 lines
        for i in range(current_line, min(current_line + 5, total_lines)):
            print(lines[i])  # Strip newline characters for clean output
        
        # Wait for user to press Enter before displaying the next batch
        input("Press Enter key...")
        
        # Update the current line number
        current_line += 5

# Specify the filename of the CSV file
file_name = 'it_company.csv'

# Call the function to display the lines
display_lines(file_name)
