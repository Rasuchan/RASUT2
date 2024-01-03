<p align="center">

# URL Processing Tool Documentation <hr>
### SUBMITTED BY RASHMIKA R S

<!-- Profile Views -->
<p align="left">
  <img src="https://komarev.com/ghpvc/?username=Rasuchan&label=Profile%20views&color=0e75b6&style=flat" alt="Rasuchan" />
</p>

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

<hr>

<p align="center">
  <img src="URL PROCESSING (2).gif">
</p>

## OVERVIEW
> The URL Processing Tool is a utility designed to process URLs from an input file and generate a list of unique endpoints, which are then written to an output file. This tool is particularly useful for analyzing and extracting endpoints from URLs.

# WORKING WITH URL's
- INPUT FILE VALIDATION - Check if the specified input file exists, if the file is not found print an error message and exit the program.
- READ URL's FROM INPUT FILE - Open the input file and reads its contents line by line, strip any leading / trailing whitespaces from eachline.
- GENERATE UNIQUE ENDPOINTS - For each URL split it into parts by using '/' as the separator. Create a set called UNIQUE_ENDPOINTS by joining the parts in different combination, starting from the third part upto the entire URL.
- WRITE TO OUTPUT FILE: Open the output file in write mode, Write the unique endpoints to the output file, each on a new line.
- COMMAND LINE ARGUMENT PARSING: Use argparse to parse command-line arguments. Accept the input file path using the --input option. Accept the output file path using the -o option.
- USER INPUT FOR INPUT AND OUTPUT FILES: Prompt the user to provide the paths for the input and output files if not provided as command-line arguments.
- EXECUTION : If executed as the main program (not imported as a module), run the URL processing function with the provided input and output file paths.

  <p align="center">
  <img src="url features.gif">
</p><hr>

  ## WORKING SCREENSHOTS 
  ### PYTHON CODE :-
![code](https://github.com/Rasuchan/RASUT2/blob/main/code.png)
### EXECUTING ON TERMINAL :-
![code](https://github.com/Rasuchan/RASUT2/blob/main/terminal.png)
### INPUT FILE :-
![input](https://github.com/Rasuchan/RASUT2/blob/main/input.png)
### OUTPUT GENERATED :-
![output1](https://github.com/Rasuchan/RASUT2/blob/main/output1.png)
![output](https://github.com/Rasuchan/RASUT2/blob/main/output2.png)

<hr>

## INSTALLATION
**CLONE THE REPOSITORY** <hr>
`bash`
```
 git clone https://github.com/Rasuchan/URL_PROCESSING_TOOL.git
```
**NAVIGATE TO THE PROJECT DIRECTORY** <hr>
`bash`
```
cd URL_PROCESSING_TOOL
```
**RUN THE SCRIPT**
> Ensure you have Python installed on your machine.
>> Execute the script with the desired input and output file paths. For example:
<hr>

`bash`
```
python url_processing_tool.py --input input_file.txt -o output_file.txt
```
> Replace input_file.txt and output_file.txt with your actual file paths.


<hr>

## FEATURES
- INPUT VALIDATION
> Checks input file existence; prompts for user input if file not found.
- URL PROCESSING
> Reads, deduplicates, and generates unique endpoints from URLs.
- SORTING AND OUTPUT
> Alphabetically sorts unique endpoints; writes results to the output file.
- COMMAND-LINE INTERFACE
> Utilizes argparse for seamless command-line interactions.
- EXECUTION
> Standalone execution processes URLs, producing unique endpoints.


<hr>

<h3 align="left">Connect with me:</h3>
<p align="left">
  <a href="https://www.linkedin.com/in/rashmika02/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="RASHMIKA R S" height="30" width="40" /></a>
<a href="https://www.instagram.com/rasu_chan8825/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="RASHMIKA R S" height="30" width="40" /></a>
</p>
