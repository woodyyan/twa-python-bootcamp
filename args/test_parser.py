import unittest

from args.parser import Parser


class TestParser(unittest.TestCase):
    # 词法分析
    # test_should_return_flag_length_should_be_1_given_flag_length_is_2_when_verify_args
    # test_should_return_flags_length_should_be_1_given_two_flags_without_space
    # test_should_return_flags_cannot_be_duplicated_given_two_same_flags
    # test_should_return_invalid_flag_given_flag_has_space_between_dash_and_letter
    # test_should_return_invalid_value_given_value_has_space
    # test_should_return_args_given_multi_space_at_start_end_middle
    # test_should_return_args_given_multi_space_between_two_flags_when_no_value
    # test_should_return_total_length_should_not_greater_than_255_given_message_length_is_256
    #
    # 语法分析
    # test_should_return_unsupported_flags_given_flag_is_l_when_schema_is_f
    # test_should_return_flag_l_type_is_int_given_l_abc_when_schema_is_l_with_int_value
    # test_should_return_correct_args_given_d_123_l_abc_i_when_schema_is_d_int_l_string_i_bool_value
    #
    # 默认值
    # test_should_return_default_value_false_0_empty_given_p_d_when_schema_is_b_bool_p_int_d_string
    # test_should_return_default_value_false_0_empty_given_none_message_when_schema_is_b_bool_p_int_d_string
    # test_should_return_true_8080_logs_value_given_i_p_8080_d_logs_when_schema_is_b_bool_p_int_d_string
    def test_should_return_flag_length_should_be_1_given_flag_length_is_2_when_verify_args(self):
        schema = {'l': 'int'}
        parser = Parser(schema)
        message = '-ll'
        args = parser.parse(message)
        self.assertEqual(args.message, 'invalid flag length.')

    def test_should_return_unsupported_flag_given_two_flags_without_space(self):
        schema = {'l': 'int'}
        parser = Parser(schema)
        message = '-l-p'
        args = parser.parse(message)
        self.assertEqual(args.message, 'unsupported flag.')

    def test_should_return_flags_cannot_be_duplicated_given_two_same_flags(self):
        schema = {'-l': 'int'}
        parser = Parser(schema)
        message = '-l -l'
        args = parser.parse(message)
        self.assertEqual(args.message, 'flags cannot be duplicated.')

    def test_should_return_invalid_flag_given_flag_has_space_between_dash_and_letter(self):
        schema = {'l': 'int'}
        parser = Parser(schema)
        message = '- l'
        args = parser.parse(message)
        self.assertEqual(args.message, 'invalid flag length.')

    def test_should_return_invalid_value_given_value_has_space(self):
        schema = {'l': 'str'}
        parser = Parser(schema)
        message = '-l a b'
        args = parser.parse(message)
        self.assertEqual(args.message, 'invalid value.')

    def test_should_return_args_given_multi_space_at_start_end_middle(self):
        schema = {'l': 'int'}
        parser = Parser(schema)
        message = '   -l    0   '
        args = parser.parse(message)
        self.assertEqual(args.message, None)

    def test_should_return_args_given_multi_space_between_two_flags_when_no_value(self):
        schema = {'l': 'int'}
        parser = Parser(schema)
        message = '-l    0'
        args = parser.parse(message)
        self.assertEqual(args.message, None)

    def test_should_return_total_length_should_not_greater_than_255_given_message_length_is_256(self):
        schema = ''
        parser = Parser(schema)
        message_with_256_length = ''
        for num in range(256):
            message_with_256_length += str(num)
        args = parser.parse(message_with_256_length)
        self.assertEqual(args.message, 'total length of message should not greater than 255.')

    def test_should_return_unsupported_flags_given_flag_is_l_when_schema_is_f(self):
        schema = {'f': 'int'}
        parser = Parser(schema)
        message = '-l abc'
        args = parser.parse(message)
        self.assertEqual(args.message, 'unsupported flag.')

    def test_should_return_flag_l_type_is_int_given_l_abc_when_schema_is_l_with_int_value(self):
        schema = {'l': 'int'}
        parser = Parser(schema)
        message = '-l abc'
        args = parser.parse(message)
        self.assertEqual(args.message, 'flag l type should be int.')

    def test_should_return_correct_args_given_d_123_l_abc_i_when_schema_is_d_int_l_string_i_bool_value(self):
        schema = {'d': 'int', 'l': 'str', 'i': 'bool'}
        parser = Parser(schema)
        message = '  -d   123  -l  abc   -i   '
        args = parser.parse(message)
        self.assertEqual(args.message, None)

    def test_should_return_default_value_false_0_empty_given_p_d_when_schema_is_b_bool_p_int_d_string(self):
        schema = {'p': 'int', 'd': 'str', 'b': 'bool'}
        parser = Parser(schema)
        message = '  -d   -p   '
        args = parser.parse(message)
        self.assertEqual(args.message, None)
        self.assertEqual(args.items['b'], False)
        self.assertEqual(args.items['d'], '')
        self.assertEqual(args.items['p'], 0)

    def test_should_return_default_value_false_0_empty_given_none_message_when_schema_is_b_bool_p_int_d_string(self):
        schema = {'p': 'int', 'd': 'str', 'b': 'bool'}
        parser = Parser(schema)
        args = parser.parse(None)
        self.assertEqual(args.message, None)
        self.assertEqual(args.items['b'], False)
        self.assertEqual(args.items['d'], '')
        self.assertEqual(args.items['p'], 0)

    def test_should_return_true_8080_logs_value_given_i_p_8080_d_logs_when_schema_is_b_bool_p_int_d_string(self):
        schema = {'p': 'int', 'd': 'str', 'b': 'bool'}
        parser = Parser(schema)
        args = parser.parse('   -p  8080  -d logs  -b')
        self.assertEqual(args.message, None)
        self.assertEqual(args.items['b'], True)
        self.assertEqual(args.items['d'], 'logs')
        self.assertEqual(args.items['p'], 8080)
