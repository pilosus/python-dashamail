"""
Copyright 2022 Vitaly Samigullin and contributors. All rights reserved.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

SPDX-License-Identifier: Apache-2.0
"""


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
