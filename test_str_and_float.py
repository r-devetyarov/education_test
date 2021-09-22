import pytest


class DataForFloatTests:
    operation_sum = [(0.7, 10, "+", 10.7), (1.73, 0, "+", 1.73), (1.55, 2.45, "+", 4.0)]
    operation_subtraction = [
        (10.75, 10, "-", 0.75),
        (14.53, 10.03, "-", 4.5),
        (0.3, 0, "-", 0.3),
        (0, 5.5, "-", -5.5),
    ]
    operation_multiplication = [
        (11.1, 2, "*", 22.2),
        (13.12, 0, "*", 0),
        (1.2, 1.3, "*", 1.56),
    ]
    operation_divisor = [(10.6, 2, "/", 5.3), (0, 3.3, "/", 0), (7.0, 2.5, "/", 2.8)]

    float_data_operations_tests = [
        *operation_sum,
        *operation_subtraction,
        *operation_multiplication,
        *operation_divisor,
    ]

    float_data_type_tests = [0.0, 1.0, 10.999, -1.0, -10.999]
    float_data_zero_division = [1.0, -1.0]


class TestFloat:
    data_for_test = DataForFloatTests()

    @pytest.mark.parametrize(
        "number_1, number_2, operator, expected_result",
        data_for_test.float_data_operations_tests,
    )
    def test_operation_with_float(self, number_1, number_2, operator, expected_result):

        if operator == "+":
            assert number_1 + number_2 == expected_result
        elif operator == "-":
            assert number_1 - number_2 == expected_result
        elif operator == "*":
            assert number_1 * number_2 == expected_result
        elif operator == "/":
            assert number_1 / number_2 == expected_result

    @pytest.mark.parametrize("number", data_for_test.float_data_type_tests)
    def test_type_float(self, number):
        assert isinstance(number, float)

    def test_negative_iterable_float(self):
        with pytest.raises(TypeError):
            for i in 5.55:
                pass

    def test_negative_overflow_error(self):
        with pytest.raises(OverflowError):
            999.999 ** 1000


class DataForStrTests:
    operation_concurrency = [
        ("ab", "cd", "+", "abcd"),
        ("qw", "", "+", "qw"),
        ("", "", "+", ""),
    ]
    operation_multiplication = [("a", 3, "*", "aaa"), ("", 5, "*", "")]
    data_str_operations_tests = [*operation_concurrency, *operation_multiplication]


class TestStr:
    data_for_test = DataForStrTests()

    @pytest.mark.parametrize(
        "string, param, operator, expected_result",
        data_for_test.data_str_operations_tests,
    )
    def test_operation_with_string(self, string, param, operator, expected_result):
        if operator == "+":
            assert string + param == expected_result
        elif operator == "*":
            assert string * param == expected_result

    def test_string_iteration(self):
        string = "abcd"
        for symbol in string:
            assert isinstance(symbol, str)
            assert symbol in string

    def test_negative_change_string(self):
        string = 'abcd'
        with pytest.raises(TypeError):
            string[0] = "1"

    def test_negative_string_get_non_existent_index(self):
        string = "qwerty"
        with pytest.raises(IndexError):
            string[len(string) + 1]
