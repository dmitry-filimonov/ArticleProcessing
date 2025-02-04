from article_processing import detect_language
from libs.file_reader import read_file
from . import *


def execute_test(file_path):
    file_name, article_text = read_file(file_path)
    detect_lang_title = detect_language(file_name)
    detect_lang_text = detect_language(article_text)
    assert detect_lang_title == 'ru', f"Title language check failed in file {file_path}"
    assert detect_lang_text == 'ru', f"Text language check failed in file {file_path}"


def test_health_1():
    execute_test(health_1)


def test_health_2():
    execute_test(health_2)


# def test_science_1():
#     execute_test(science_1)


# def test_science_2():
#     execute_test(science_2)


# def test_politic_1():
#     execute_test(politic_1)


# def test_politic_2():
#     execute_test(politic_2)


# def test_sport_1():
#     execute_test(sport_1)


# def test_sport_2():
#     execute_test(sport_2)


def test_economic_1():
    execute_test(economic_1)


def test_economic_2():
    execute_test(economic_2)
