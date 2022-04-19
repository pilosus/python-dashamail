class DashaMailException(Exception):
    """Base exception"""
    pass


class DashaMailAPIError(DashaMailException):
    """Error returned by the API"""
    def __init__(
        self,
        error_code: int,
        error_type: str,
        error_message: str,
    ) -> None:
        self.error_code = error_code
        self.error_type = error_type
        self.error_message = error_message
        self.message = "Error code {} ({}): {}".format(self.error_code, self.error_type, self.error_message)

    def __str__(self):
        return self.message
