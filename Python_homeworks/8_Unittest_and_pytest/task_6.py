# Create function file_parser. If function is called with 2 arguments it must count the number of occurrences string in
# a file, in case of 3 arguments it must replace string in a file to new string
# first argument - path to file
# second argument - find string
# third argument - replace string
# Function must returned string with count of occurrences or count of replaced strings
# Example:
# file_parser("file.txt", 'x', 'o')-> Replaced 8 strings
# file_parser("file.txt", 'o') -> Found 8 strings
# Please, create class ParsesTest and write unittest for file_parser function uses mock object

import unittest
from unittest.mock import patch, mock_open

def file_parser(filename, text_for_count, text_for_replace=None):
    with open(filename, "r") as f:
        res_text = f.read()
        counter = res_text.count(text_for_count)
    if text_for_replace:
        with open(filename, "w") as f:
            res_text = res_text.replace(text_for_count, text_for_replace)
            f.write(res_text)
            return f"Replaced {counter} strings"
    return f"Found {counter} strings"

class ParserTest(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='O Captain! my Captain! our fearful trip is done')
    def test_read(self, mock_file):
        self.assertEqual(file_parser("test_file.txt", "O"), 'Found 1 strings')
        mock_file.assert_called_with("test_file.txt", "r")

    @patch('builtins.open', new_callable=mock_open, read_data='O Captain! my Captain! our fearful trip is done')
    def test_write(self, mock_file):
        self.assertEqual(file_parser("test_file.txt", "!", "?"), 'Replaced 2 strings')
        mock_file.assert_called_with("test_file.txt", "w")

#Tests

print(count_tests >= 2)#Expect True

print(file_parser('parser.txt', 'better'))#Expect Found 8 strings

try:
    file_parser('pars.txt', 'better')
except FileNotFoundError as e:
    print('File is not exist')
#Expect File is not exist