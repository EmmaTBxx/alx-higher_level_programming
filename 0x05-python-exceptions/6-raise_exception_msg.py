#!/usr/bin/python3

def raise_exception_msg(message=""):
    """
    Function that raises a custom NameError exception with an optional message.

    Args:
        message (str): An optional string msg  to be raised with the exception.

    Raises:
  NameError:If the optional msg is provided,it will raise with the exception.
    """
    raise NameError(message)
