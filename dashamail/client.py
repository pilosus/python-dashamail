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
from typing import Any, List, Optional

import requests

from .exceptions import DashaMailAPIError

ResponseType = dict


class DashaMailClient:
    """
    DashaMail API client for Python
    https://dashamail.ru/api/
    """

    def __init__(
        self,
        api_key: str,
        timeout: float = 10.0,
        raise_for_error: bool = False,
        requests_params: Optional[dict] = None,
    ) -> None:
        self.base_url = "https://api.dashamail.com"
        self.response_format = "json"

        self.api_key = api_key
        self.timeout = timeout
        self.raise_for_error = raise_for_error
        self.requests_params = requests_params or {}

        self.base_params = {"api_key": self.api_key, "format": self.response_format}

    def _request(self, api_method: str, **params: Any) -> ResponseType:
        payload = {**self.base_params, "method": api_method, **params}
        raw_response = requests.get(url=self.base_url, params=payload, timeout=self.timeout, **self.requests_params)
        json_response = raw_response.json().get("response", {})

        error = json_response.get("msg", {})
        if error.get("err_code") != 0 and self.raise_for_error:
            raise DashaMailAPIError(
                error_code=error.get("err_code"), error_type=error.get("type"), error_message=error.get("text")
            )

        return json_response

    def lists_get(self, **params: Any) -> ResponseType:
        """
        Get user's contact lists

        API method: lists.get

        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.get", **params)

    def lists_add(self, name: str, **params: Any) -> ResponseType:
        """
        Create a contact list

        API method: lists.add

        :param name: contact list title
        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.add", name=name, **params)

    def lists_update(self, list_id: int, **params: Any) -> ResponseType:
        """
        Update contact list details

        API method: lists.update

        :param list_id: contact list id
        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.update", list_id=list_id, **params)

    def lists_delete(self, list_id: int, **params: Any) -> ResponseType:
        """
        Delete a contact list and all its subscribers

        API method: lists.delete

        :param list_id: contact list id
        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.delete", list_id=list_id, **params)

    def lists_get_unsubscribed(self, **params: Any) -> ResponseType:
        """
        Get unsubscribed contacts

        API method: lists.get_unsubscribed

        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.get_unsubscribed", **params)

    def lists_get_complaints(self, **params: Any) -> ResponseType:
        """
        Get complaints "It's a spam"

        API method: lists.get_complaints

        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.get_complaints", **params)

    def lists_member_activity(self, email: str, **params: Any) -> ResponseType:
        """
        Get subscriber activity

        API method: lists.member_activity

        :param email: email address string
        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.member_activity", email=email, **params)

    def lists_upload(self, list_id: int, file_url: str, email_col_num: int, **params: Any) -> ResponseType:
        """
        Import contact list from a file

        API method: lists.upload

        :param list_id: contact list id
        :param file_url: URL to a contacts file
        :param email_col_num: column number (starting from 0) of email data in the file
        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.upload", list_id=list_id, file=file_url, email=email_col_num, **params)

    def lists_add_member(self, list_id: int, email: str, **params: Any) -> ResponseType:
        """
        Add a single subscriber to the contact list

        API method: lists.add_member

        :param list_id: contact list id
        :param email: email address string
        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.add_member", list_id=list_id, email=email, **params)

    def lists_add_member_batch(self, list_id: int, batch: List[List[str]], **params: Any) -> ResponseType:
        """
        Add subscribers to the contact list in bulk

        API method: lists.add_member_batch

        :param list_id: contact list id
        :param batch: contacts in format [["email 1", "col 1", "col 2", ...], ["email 2", "col 1", "col 2", ...], ...]
        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        batch_str = ";".join([",".join(s) for s in batch]) + ";"
        return self._request(api_method="lists.add_member_batch", list_id=list_id, batch=batch_str, **params)

    def lists_update_member(self, member_id: int, email: str, list_id: int, **params: Any) -> ResponseType:
        """
        Update subscriber data in the contact list

        API method: lists.update_member

        :param member_id: subscriber id
        :param email: email address string
        :param list_id: contact list id
        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(
            api_method="lists.update_member", member_id=member_id, email=email, list_id=list_id, **params
        )

    def lists_delete_member(self, member_id: int, **params: Any) -> ResponseType:
        """
        Delete a subscriber from a contact list

        API method: lists.delete_member

        :param member_id: subscriber id
        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.delete_member", member_id=member_id, **params)

    def lists_unsubscribe_member(self, member_id: int, **params: Any) -> ResponseType:
        """
        Unsubscribe a member from a contact list

        API method: lists.unsubscribe_member

        :param member_id: subscriber id
        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.unsubscribe_member", member_id=member_id, **params)

    def lists_move_member(self, member_id: int, list_id: int, **params: Any) -> ResponseType:
        """
        Move subscriber data to another contact list

        API method: lists.move_member

        :param member_id: subscriber id
        :param list_id: destination contact list id
        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.move_member", member_id=member_id, list_id=list_id, **params)

    def lists_copy_member(self, member_id: int, list_id: int, **params: Any) -> ResponseType:
        """
        Copy subscriber to another contact list

        API method: lists.copy_member

        :param member_id: subscriber id
        :param list_id: destination contact list id
        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.copy_member", member_id=member_id, list_id=list_id, **params)

    def lists_last_status(self, email: str, list_id: int, **params: Any) -> ResponseType:
        """
        Get the status of the last email sent to the contact list

        API method: lists.last_status

        :param email: email address string
        :param list_id: contact list id
        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.last_status", email=email, list_id=list_id, **params)

    def lists_get_import_history(self, list_id: int, **params: Any) -> ResponseType:
        """
        Get the history of contacts import for the contact list

        API method: lists.get_import_history

        :param list_id: contact list id
        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.get_import_history", list_id=list_id, **params)

    def lists_check_email(self, email: str, list_id: int, **params: Any) -> ResponseType:
        """
        Check if the email address is valid and if it's unsubscribed or in the stop-list for the contact list

        API method: lists.check_email

        :param email: email address string
        :param list_id: contact list id
        :param params: any other parameters expected by API method
        :return: ResponseType
        """
        return self._request(api_method="lists.check_email", email=email, list_id=list_id, **params)

    def lists_add_merge(self, **params):
        raise NotImplementedError("TODO")

    def lists_update_merge(self, **params):
        raise NotImplementedError("TODO")

    def lists_delete_merge(self, **params):
        raise NotImplementedError("TODO")
