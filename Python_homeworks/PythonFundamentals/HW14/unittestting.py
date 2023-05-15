import unittest

import fuctions_with_errors as f


class WrongFunks(unittest.TestCase):
    def test_name(self):
        res = f.greeting_by_name("John")
        self.assertEqual("Hello John!", res)

    def test1_symbol_position(self):
        input_text = "xnjhiyuty54556uyjgvbxcfgdrtyr5u"
        input_symbol = "xnj"
        res = f.get_symbol_position(input_text, input_symbol)
        if len(input_symbol) > 1:
            self.assertEqual("Error! Symbol can be string with only one letter", res)

    def test2_symbol_position(self):
        input_text = "xnjhiyuty54556uyjgvbxcfgdrtyr5u"
        input_symbol = "e"
        res = f.get_symbol_position(input_text, input_symbol)
        if input_text.find(input_symbol) == -1:
            self.assertEqual("Not found", res)

    def test3_symbol_position(self):
        input_text = "xnjhiyuty54556uyjgvbxcfgdrtyr5u"
        input_symbol = "u"
        res = f.get_symbol_position(input_text, input_symbol)
        self.assertEqual((input_text.find(input_symbol) + 1), res)

    def test_merge(self):
        dict1 = {"a": 1}
        dict2 = {"w":234, "a":235}
        res = f.merge(dict1, dict2)
        dict1.update(dict2)
        self.assertEqual(res, dict1)