import camelCase
from unittest import TestCase


class TestCamelCase(TestCase):
    def test_camelcase_sentence(self):
        self.assertEqual('helloWorld', camelCase.camelcase('Hello World'))

    def test_capitalize_first_letters(self):
        potential_inputs = ['HELLO', 'hello', 'heLLO', 'HELlo']
        expected_capitalization = 'HelloHelloHelloHello'
        self.assertEqual(expected_capitalization, camelCase.capitalize_first_letters(potential_inputs))

    def test_remove_all_whitespace_from_input_sentence(self):
        input_sentence = '    The   weather            is    delightful  today     '
        expected_return_string = 'The weather is delightful today'
        self.assertEqual(expected_return_string, camelCase.remove_space(input_sentence))
