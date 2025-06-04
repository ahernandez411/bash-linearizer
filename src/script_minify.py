import argparse
import os

from argparse import Namespace

class ScriptMinify:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="This tool will read in a shell or bash script and output it as a single line."
        )
        parser.add_argument("-i", "--input-path", help="The path to the shell or bash script.")
        parser.add_argument("-o", "--output-path", help="The path to save the minified script.")
        self.parser = parser

        args = parser.parse_args()    
        self.input_path = args.input_path   
        self.output_path = args.output_path
        

    def run(self):
        if self.input_path is None and self.output_path is None:
            print("No inputs detected, please provide arguments and try again")
            print("")
            self.parser.print_help()
            return

        if not os.path.exists(self.input_path):
            return

        dir_output = os.path.dirname(self.output_path)
        if not os.path.exists(dir_output):
            os.makedirs(dir_output)

        input_lines = self._load_file_lines(self.input_path)
        single_line = self._linearize_script(input_lines)
        self._save_file(self.output_path, single_line)

    def _linearize_script(self, input_lines):
        single_line_list = []
        str_equals_double = '="'
        str_equals_single = "='"
        str_equals_match = None
        newline = f"\\n"
        for line in input_lines:
            if line is None or line.strip() == "":
                continue

            line_trim = line.strip()      
            
            if line_trim.startswith("#"):
                continue

            if "#" in line_trim:
                # cut off everything in the line after this character
                before_comment = line_trim.split("#")[0].strip()
                single_line_list.append(f"{before_comment}; ")
                continue

            # if there is a =" and it doesn't end in that line treat line ending different
            # until we detect a closing quote of the same kind
            if str_equals_match is not None:
                if str_equals_match in line_trim:
                    str_equals_match = None
                else:
                    single_line_list.append(f"{line_trim}{newline}")
                    continue

            elif str_equals_double in line_trim:
                includes_closing_quote = self._has_closing_quote(str_equals_double, line_trim)
                if not includes_closing_quote:
                    str_equals_match = '"'
                    single_line_list.append(f"{line_trim}{newline}")
                    continue
            
            elif str_equals_single in line_trim:
                includes_closing_quote = self._has_closing_quote(str_equals_single, line_trim)
                if not includes_closing_quote:
                    str_equals_match = '"'
                    single_line_list.append(f"{line_trim}{newline}")
                    continue

            single_line_list.append(f"{line_trim}; ")

        single_line = "".join(single_line_list)
        return single_line


    def _has_closing_quote(self, begin_equals_quote: str, line: str) -> bool:
        quote_type = begin_equals_quote.replace("=", "")
        start = line.index(begin_equals_quote) + len(begin_equals_quote)
        after_equals_quote = line[start:]

        if quote_type in after_equals_quote:
            return True
        
        return False        


    def _save_file(self, path: str, data: str):
        with open(path, "w") as writer:
            writer.write(data)

        
    def _load_file_lines(self, path: str) -> list:
        data = None
        with open(path, "r") as reader:
            data = reader.read()

        lines = data.splitlines()
        return lines


if __name__ == "__main__":    
    ScriptMinify().run()
