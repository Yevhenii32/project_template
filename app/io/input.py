import pandas as pd


def input_console():
    """
        Reads text input from the console.

        Returns:
            str: The text entered by the user.
        """
    return input("Введіть текст: ")

def read_file(filepath):
    """
        Reads text from a file using Python's built-in capabilities.

        Args:
            filepath (str): The path to the file to read.

        Returns:
            str: The content of the file.
        """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def read_file_pandas(filepath):
    """
        Reads data from a file using the pandas library.

        Args:
            filepath (str): The path to the file to read.

        Returns:
            DataFrame: The pandas DataFrame containing the read data.
        """
    return pd.read_csv(filepath)