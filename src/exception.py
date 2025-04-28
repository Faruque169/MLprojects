import sys
import logging


def error_message_details(error, error_details: sys):
    """Return a detailed error message for the given exception."""
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = str(error)
    error_message = f"Error occurred in script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, error_message
    )
    return error_message


class CustomException(Exception):
    """Custom exception class for handling exceptions in the project."""

    def __init__(self, error_message, error_details: sys):
        """Initialize the custom exception with an error message and details."""
        super().__init__(error_message)
        self.error_message = error_message_details(
            error_message, error_details)

    def __str__(self):
        """Return the string representation of the custom exception."""
        return self.error_message


if __name__ == "__main__":
    # Example usage of the CustomException class
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero.")
        raise CustomException(e, sys)
    # This will raise a CustomException with the error message and details.
