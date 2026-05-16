import unittest
from unittest.mock import patch
import quiz
import guess


def test_getQuestions():
    questions = quiz.getQuestions(2)
    assert len(questions) == 2


class TestQuiz(unittest.TestCase):

    @patch("quiz.getQuestions", return_value=[{'question': 'Capital of France', 'answer': 'paris'}])
    @patch("builtins.input", side_effect=["1", "paris"])  # inputs must be strings
    def test_quiz_play_correct(self, mock_input, mock_questions):
        quiz.play()
        self.assertTrue(True)

    @patch("quiz.getQuestions", return_value=[{'question': 'Capital of France', 'answer': 'paris'}])
    @patch("builtins.input", side_effect=["1", "london", "paris"])
    def test_quiz_play_incorrect_then_correct(self, mock_input, mock_questions):
        quiz.play()
        self.assertTrue(True)


class TestGuess(unittest.TestCase):
    @patch('random.randint', return_value=7)
    @patch("builtins.input", side_effect=["1", "17", "7"])
    def test_guess_play_easy_correct(self, mock_input, mock_number):
        guess.play()
        self.assertTrue(True)

    @patch('random.randint', return_value=34)
    @patch("builtins.input", side_effect=["2", "17", "27", "30", "32", "35", "34"])
    def test_guess_play_medium_correct(self, mock_input, mock_number):
        guess.play()
        self.assertTrue(True)


class TestGuessWrong(unittest.TestCase):
    @patch('random.randint', return_value=34)
    @patch("builtins.input", side_effect=["2", "17", "27", "30", "32", "35", "37", "67"])
    def test_guess_play_incorrect(self, mock_input, mock_rand):
        guess.play()
        self.assertTrue(True)
