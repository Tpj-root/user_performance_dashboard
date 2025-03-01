#!/bin/bash
# Input PDF and output text file
input_pdf="result.pdf"  # Change this to your actual file
output_text="output.txt"
cleaned_file="cleaned_input.txt"
line_input=41  # Number of lines to extract in each batch

# Set page range (Modify these values later)
start_page=1
end_page=711  # Change this as needed

# Convert specific pages from PDF to text
pdftotext -f $start_page -l $end_page "$input_pdf" "$output_text"

# Remove unwanted lines from the text file
grep -v -E "Page|TEACHERS RECRUITMENT BOARD|DIRECT RECRUITMENT|Directorate of Elementary Education|Date of Examination|Date of release of result|Maximum Marks|Result Published" "$output_text" > "$cleaned_file"

# Extract the first occurrence of each required header
sno_line=$(grep -n "^S. No." "$cleaned_file" | head -n 1 | cut -d: -f1)
rollno_line=$(grep -n "^Roll No." "$cleaned_file" | head -n 1 | cut -d: -f1)
marks_line=$(grep -n "^Marks Scored in Part-B" "$cleaned_file" | head -n 1 | cut -d: -f1)

# Get total number of lines in the cleaned file
total_lines=$(wc -l < "$cleaned_file")

# Ensure valid line numbers
if [ -z "$sno_line" ] || [ -z "$rollno_line" ] || [ -z "$marks_line" ]; then
    echo "Error: One or more headers not found in the file."
    exit 1
fi

# Start processing in batches
start=1

while [ $start -le $((total_lines - sno_line)) ]; do
    # Extract next batch of lines
    sno_data=$(sed -n "$((sno_line + start)),$((sno_line + start + line_input - 1))p" "$cleaned_file")
    rollno_data=$(sed -n "$((rollno_line + start)),$((rollno_line + start + line_input - 1))p" "$cleaned_file")
    marks_data=$(sed -n "$((marks_line + start)),$((marks_line + start + line_input - 1))p" "$cleaned_file")

    # Break if no data is found (end of file reached)
    if [ -z "$sno_data" ] || [ -z "$rollno_data" ] || [ -z "$marks_data" ]; then
        break
    fi

    # Format and print output correctly
    paste -d ',' <(echo "$sno_data") <(echo "$rollno_data") <(echo "$marks_data") | awk '{print $1","$2","$3}'

    # Move to the next batch
    start=$((start + line_input))
done
