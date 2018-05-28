import logging

# ************
# Base classes
# ************

class WeblibError(Exception):
    """
    Base class for all custom exceptions
    defined in weblib package.
    """

class ResponseNotValid(WeblibError):
    """
    Indicates unexpected data received in the
    result of network request.
    """

# **************************
# Internal weblib exceptions
# **************************

class RuntimeConfigError(WeblibError):
    """
    Raised when passed parameters do not makes sense
    or conflict with something.
    """

# **********************
# Data not found classes
# **********************

class DataNotFound(WeblibError, IndexError):
    """
    Raised when it is not possible to find requested
    data.
    """

class NextPageNotFound(DataNotFound):
    """
    Raised when the scraping logic could not extract link
    to next page from the pagination block
    """

# ******************************
# ResponseNotValid based classes
# ******************************

class DataNotValid(ResponseNotValid):
    pass


class RequestBanned(ResponseNotValid):
    pass


class CaptchaRequired(ResponseNotValid):
    pass


class PageNotFound(ResponseNotValid):
    pass


class AccessDenied(ResponseNotValid):
    pass

# *****************************
# ResponseNotValid based Classes
# specific to HTTP code errors
# *****************************

class HttpCodeNotValid(ResponseNotValid): 
    pass


class HttpCodeZero(HttpCodeNotValid):
    pass
