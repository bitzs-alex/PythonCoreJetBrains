from hstest.stage_test import *
from hstest.test_case import TestCase
import os, re

TOO_LONG_LINE = 'Too long line is not mentioned. '
error_code_long = "s001"

INDENTATION = "Invalid check of indentation. "
error_code_indention = "s002"

UNNECESSARY_SEMICOLON = "Your program passed the line with an unnecessary semicolon or has an incorrect format. "
error_code_semicolon = "s003"

TWO_SPACES_BEFORE_COMMENT = "The program should warn about the line with less than 2 spaces before a comment."
error_code_comments = "s004"

TODO = "Your program passed the line with TODO comment or has an incorrect format. "
error_code_todo = "s005"

TOO_MANY_BLANK_LINES = "Your program didn't warn about more than two blank lines between lines."
error_code_blank_lines = "s006"

FALSE_ALARM = "False alarm. Your program warned about correct row."

cur_dir = os.path.abspath(os.curdir)


class AnalyzerTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase(args=[f"test{os.sep}test_1.py"], check_function=self.test_1),
                TestCase(args=[f"test{os.sep}test_2.py"], check_function=self.test_2),
                TestCase(args=[f"test{os.sep}test_3.py"], check_function=self.test_3),
                TestCase(args=[f"test{os.sep}test_4.py"], check_function=self.test_4),
                TestCase(args=[f"test{os.sep}test_5.py"], check_function=self.test_5),
                TestCase(args=[f"test{os.sep}test_6.py"], check_function=self.test_6),
                TestCase(args=[cur_dir + f"{os.sep}test"], check_function=self.test_7)]

    # Check of indention violation
    def test_1(self, output: str, attach):
        file_path = f"test{os.sep}test_1.py"
        output = output.strip().lower().splitlines()
        if not len(output) == 3:
            return CheckResult.wrong("Incorrect number of warning messages.")
        for line in output:
            if re.search('line[\d]', line) is not None:
                return CheckResult.wrong('Incorrect format of an error message')
        if not output[0].startswith(f"{file_path}: line 2: {error_code_indention}"):
            return CheckResult.wrong(INDENTATION + "Your program passed the row with single column indent.")
        if not output[1].startswith(f"{file_path}: line 3: {error_code_indention}"):
            return CheckResult.wrong(INDENTATION + "Your program passed the row with two columns indent.")
        if not output[2].startswith(f"{file_path}: line 5: {error_code_indention}"):
            return CheckResult.wrong(INDENTATION + "Your program passed the row with six columns indent.")
        return CheckResult.correct()

    # Test of semicolon violation
    def test_2(self, output: str, attach):
        file_path = f"test{os.sep}test_2.py"
        output = output.strip().lower().splitlines()
        if len(output) <= 1:
            return CheckResult.wrong("It looks like there is no messages from your program.")

        # negative tests
        for item in output:
            if item.startswith(f"{file_path}: line 1: {error_code_semicolon}"):
                return CheckResult.wrong(FALSE_ALARM + "There was no any semicolons at all.")
            if item.startswith(f"{file_path}: line 5: {error_code_semicolon}") or item.startswith(
                    f"line 8 {error_code_semicolon}"):
                return CheckResult.wrong(FALSE_ALARM + "The semicolon was a part of comment block")
            if item.startswith(f"{file_path}: line 6: {error_code_semicolon}") or item.startswith(
                    f"line 7 {error_code_semicolon}"):
                return CheckResult.wrong(FALSE_ALARM + "The semicolon was a part of string")

        # positive tests
        if not len(output) == 3:
            return CheckResult.wrong("Incorrect number of warning messages.")
        for i, j in enumerate([2, 3, 4]):
            if not output[i].startswith(f"{file_path}: line {j}: {error_code_semicolon}"):
                return CheckResult.wrong(UNNECESSARY_SEMICOLON)
        return CheckResult.correct()

    # Test of todo_comments
    def test_3(self, output: str, attach):
        file_path = f"test{os.sep}test_3.py"
        output = output.strip().lower().splitlines()
        if len(output) <= 1:
            return CheckResult.wrong("It looks like there is no messages from your program.")

        # negative tests
        for item in output:
            if item.startswith(f"{file_path}: line 1: {error_code_todo}") or item.startswith(
                    f"line 8 {error_code_todo}") or \
                    item.startswith(f"line 9: {error_code_todo}"):
                return CheckResult.wrong(FALSE_ALARM + "There was no any TODO comments")
            if item.startswith(f"{file_path}: line 6: {error_code_todo}") or item.startswith(
                    f"line 7 {error_code_todo}"):
                return CheckResult.wrong(FALSE_ALARM + "TODO is inside of string")

        # positive tests
        if not len(output) == 4:
            return CheckResult.wrong("A wrong number of warning messages. "
                                     "Your program should warn about two mistakes in this test case")
        for i, j in enumerate([2, 3, 4, 5]):
            if not output[i].startswith(f"{file_path}: line {j}: {error_code_todo}"):
                return CheckResult.wrong(TODO)

        return CheckResult.correct()

    # Blank lines test
    def test_4(self, output, attach):
        file_path = f"test{os.sep}test_4.py"
        output = output.strip().lower().splitlines()
        if len(output) != 1:
            if len(output) == 0:
                return CheckResult.wrong(TOO_MANY_BLANK_LINES)
            if output[0].startswith(f"{file_path}: line 4: {error_code_blank_lines}"):
                return CheckResult.wrong(FALSE_ALARM)
            if not output[0].startswith(f"{file_path}: line 8: {error_code_blank_lines}"):
                return CheckResult.wrong(TOO_MANY_BLANK_LINES)
            else:
                return CheckResult.wrong(TOO_MANY_BLANK_LINES)
        return CheckResult.correct()

    # Test of comments style
    def test_5(self, output, attach):
        file_path = f"test{os.sep}test_5.py"
        output = output.strip().lower().splitlines()
        if len(output) <= 1:
            return CheckResult.wrong("It looks like there is no messages from your program.")

        # negative tests
        for item in output:
            if item.startswith(f"{file_path}: line 1: {error_code_comments}"):
                return CheckResult.wrong(FALSE_ALARM + "There is no comments at all.")
            if item.startswith(f"{file_path}: line 2: {error_code_comments}"):
                return CheckResult.wrong(FALSE_ALARM + "There is a correct line with comment")
            if item.startswith(f"{file_path}: line 3: {error_code_comments}" or
                               item.startswith(f"{file_path}: line 4: {error_code_comments}")):
                return CheckResult.wrong(FALSE_ALARM + "It is a correct line with a comment after code.")

        # positive test
        for i, j in enumerate([6, 7]):
            if not output[i].startswith(f"{file_path}: line {j}: {error_code_comments}"):
                return CheckResult.wrong(TWO_SPACES_BEFORE_COMMENT)

        return CheckResult.correct()

    def test_6(self, output, attach):
        file_path = f"test{os.sep}test_6.py"
        output = output.strip().lower().splitlines()

        if len(output) != 9:
            return CheckResult.wrong("It looks like there is no messages from your program.")

        if not (output[0].startswith(f"{file_path}: line 1: s004") or
                output[7].startswith(f"{file_path}: line 13: s004")):
            return CheckResult.wrong(TWO_SPACES_BEFORE_COMMENT)

        if not (output[1].startswith(f"{file_path}: line 2: s003") or
                output[3].startswith(f"{file_path}: line 3: s003") or
                output[6].startswith(f"{file_path}: line 13: s003")):
            return CheckResult.wrong(UNNECESSARY_SEMICOLON)

        if not (output[2].startswith(f"{file_path}: line 3: s001") or
                output[4].startswith(f"{file_path}: line 6: s001")):
            return CheckResult.wrong(TOO_LONG_LINE)

        if not (output[5].startswith(f"{file_path}: line 11: s006")):
            return CheckResult.wrong(TOO_MANY_BLANK_LINES)

        if not output[8].startswith(f"{file_path}: line 13: s005"):
            return CheckResult.wrong(TODO)

        return CheckResult.correct()

    def test_7(self, output, attach):
        file_1 = cur_dir.lower() + f"{os.sep}test{os.sep}test_1.py"
        file_2 = cur_dir.lower() + f"{os.sep}test{os.sep}test_2.py"
        file_3 = cur_dir.lower() + f"{os.sep}test{os.sep}test_3.py"
        file_4 = cur_dir.lower() + f"{os.sep}test{os.sep}test_4.py"
        file_5 = cur_dir.lower() + f"{os.sep}test{os.sep}test_5.py"
        output = output.strip().lower().splitlines()

        # test_1 file
        if len(output) != 22:
            return CheckResult.wrong("It looks like there is an incorrect number of error messages. "
                                     f"Expected 22 lines, found {len(output)}")
        if not output[0].startswith(f"{file_1}: line 2: {error_code_indention}"):
            return CheckResult.wrong(INDENTATION + "Your program passed the row with single column indent.")
        if not output[1].startswith(f"{file_1}: line 3: {error_code_indention}"):
            return CheckResult.wrong(INDENTATION + "Your program passed the row with two columns indent.")
        if not output[2].startswith(f"{file_1}: line 5: {error_code_indention}"):
            return CheckResult.wrong(INDENTATION + "Your program passed the row with six columns indent.")

        # negative tests
        for item in output:
            if item.startswith(f"{file_2}: line 1: {error_code_semicolon}"):
                return CheckResult.wrong(FALSE_ALARM + "There was no any semicolons at all.")
            if item.startswith(f"{file_2}: line 5: {error_code_semicolon}") or item.startswith(
                    f"line 8 {error_code_semicolon}"):
                return CheckResult.wrong(FALSE_ALARM + "The semicolon was a part of comment block")
            if item.startswith(f"{file_2}: line 6: {error_code_semicolon}") or item.startswith(
                    f"line 7 {error_code_semicolon}"):
                return CheckResult.wrong(FALSE_ALARM + "The semicolon was a part of string")

            if item.startswith(f"{file_3}: line 1: {error_code_todo}") or item.startswith(
                    f"line 8 {error_code_todo}") or \
                    item.startswith(f"line 9: {error_code_todo}"):
                return CheckResult.wrong(FALSE_ALARM + "There was no any TODO comments")
            if item.startswith(f"{file_3}: line 6: {error_code_todo}") or item.startswith(
                    f"line 7 {error_code_todo}"):
                return CheckResult.wrong(FALSE_ALARM + "TODO is inside of string")

            if item.startswith(f"{file_5}: line 1: {error_code_comments}"):
                return CheckResult.wrong(FALSE_ALARM + "There is no comments at all.")
            if item.startswith(f"{file_5}: line 2: {error_code_comments}"):
                return CheckResult.wrong(FALSE_ALARM + "There is a correct line with comment")
            if item.startswith(f"{file_5}: line 3: {error_code_comments}" or
                               item.startswith(f"{file_5}: line 4: {error_code_comments}")):
                return CheckResult.wrong(FALSE_ALARM + "It is a correct line with a comment after code.")

        # test_2 file
        for i, j in enumerate([2, 3, 4]):

            if not output[i + 3].startswith(f"{file_2}: line {j}: {error_code_semicolon}"):
                return CheckResult.wrong(UNNECESSARY_SEMICOLON)

        # test_3 file
        for i, j in enumerate([2, 3, 4, 5]):
            if not output[i + 6].startswith(f"{file_3}: line {j}: {error_code_todo}"):
                return CheckResult.wrong(TODO)

        # test_4 file
        if output[10].startswith(f"{file_4}: line 4: {error_code_blank_lines}"):
            return CheckResult.wrong(FALSE_ALARM)
        if not output[10].startswith(f"{file_4}: line 8: {error_code_blank_lines}"):
            return CheckResult.wrong(TOO_MANY_BLANK_LINES)

        # test_5 file
        for i, j in enumerate([6, 7]):
            if not output[i + 11].startswith(f"{file_5}: line {j}: {error_code_comments}"):
                return CheckResult.wrong(TWO_SPACES_BEFORE_COMMENT)

        return CheckResult.correct()


if __name__ == '__main__':
    AnalyzerTest("analyzer.code_analyzer").run_tests()
