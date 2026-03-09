def output_to_console(text):
    """
        Outputs text to the console.

        Args:
            text (str): The text to be printed to the console.
        """
    print(text)

def write_file(filepath, text):
    """
        Writes text to a file using Python's built-in capabilities.

        Args:
            filepath (str): The path to the file where the text will be written.
            text (str): The text to write to the file.
        """
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(str(text))

def write_file_pandas(filepath, data):
    """
        Writes data to a file using the pandas library.

        Args:
            filepath (str): The path to the output file.
            data (DataFrame): The pandas DataFrame to be written to the file.
        """
    data.to_csv(filepath, index=False)