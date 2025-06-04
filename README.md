# Script Minify

This tool takes a bash or shell script as an input file and minifies it so it fits on a single line.

This is helpful if you want to take a script and run it from a single copy-paste command.

## Usage Help
This help documentation was created by running `python3 src/minifier.py` from a terminal window.

```
usage: minifier.py [-h] [-i INPUT_PATH] [-o OUTPUT_PATH]

This tool will read in a shell or bash script and output it as a single line.

options:
  -h, --help            show this help message and exit
  -i, --input-path INPUT_PATH
                        The path to the shell or bash script.
  -o, --output-path OUTPUT_PATH
                        The path to save the minified script.
```
