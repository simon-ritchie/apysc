"""Interface implementation for the `update_path_data` method.
"""

from abc import ABC, abstractmethod


class UpdatePathDataInterface(ABC):

    @abstractmethod
    def update_path_data(self) -> None:
        """
        Update the path's data settings.
        """
