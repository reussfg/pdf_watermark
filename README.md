**PDF Watermarking Tool**

This is a Python script that adds a watermark to a set of PDF files using the pdfrw library. The script searches for all PDF files in a specified directory and applies a watermark to each page of each file. The watermarked PDF files are saved to a new directory.

**Requirements**

Python 3
pdfrw library

**How to Use**
Install the pdfrw library using pip: pip install pdfrw
Download or clone the script to your local machine.
Open the script in a Python IDE or text editor.
Update the paths to the input and output directories in the script.
Replace the watermark file path with the path to your desired watermark file.
Run the script.
The watermarked PDF files will be saved to the output directory.


**How does it work?**

This code is written in Python and uses the pdfrw library to add a watermark to a set of PDF files.

The code first imports the necessary libraries: pdfrw, pathlib, and os.

Then, it sets the path to the directory containing the PDF files to be watermarked using the Path() function from the pathlib library. It searches for all PDF files in the directory with the glob() method.

It then iterates over each PDF file and retrieves the name of the file. It appends the names to a list called "pdf_names".

Next, the code enters a loop that iterates over the "pdf_names" list. In each iteration, it sets the input and output files' paths and the path to the watermark file.

The code then initializes the reader and writer objects and the watermark object using the PdfReader() function. It retrieves the first page of the watermark PDF file.

The code then goes through each page of the input PDF file one by one and adds the watermark to each page using the PageMerge() function. The rendered pages are written to the output PDF file using the PdfWriter() function.

Overall, this code adds a watermark to a set of PDF files and saves the modified files in a new directory.
