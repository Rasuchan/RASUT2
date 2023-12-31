# TASK 2 : CREATE A BASIC TOOL TO PROCESS THE GIVEN URL'S INTO DIFFERENT COMBINATIONS WITH RESPECT TO THE ENDPOINTS OF URL <hr>
# SUBMITTED BY RASHMIKA R S
# WORKING WITH URL's
- INPUT FILE VALIDATION - Check if the specified input file exists, if the file is not found print an error message and exit the program.
- READ URL's FROM INPUT FILE - Open the input file and reads its contents line by line, strip any leading / trailing whitespaces from eachline.
- GENERATE UNIQUE ENDPOINTS - For each URL split it into parts by using '/' as the separator. Create a set called UNIQUE_ENDPOINTS by joining the parts in different combination, starting from the third part upto the entire URL.
- WRITE TO OUTPUT FILE: Open the output file in write mode, Write the unique endpoints to the output file, each on a new line.
- COMMAND LINE ARGUMENT PARSING: Use argparse to parse command-line arguments. Accept the input file path using the --input option. Accept the output file path using the -o option.
- USER INPUT FOR INPUT AND OUTPUT FILES: Prompt the user to provide the paths for the input and output files if not provided as command-line arguments.
- EXECUTION : If executed as the main program (not imported as a module), run the URL processing function with the provided input and output file paths.
  ## WORKING SCREENSHOTS 
  ### PYTHON CODE
![code](https://github.com/Rasuchan/RASUT2/blob/main/code.png)
### EXECUTING ON TERMINAL
![code](https://github.com/Rasuchan/RASUT2/blob/main/terminal.png)
