from abc import ABC, abstractmethod
from typing import Optional
from {{ package_name }}.schema.model.item import Item
from {{ package_name }}.schema.request.item import ItemCreate


class IItemRepository(ABC):
    @abstractmethod
    def get_item(self, item_id: int) -> Optional[Item]:
        raise NotImplementedError

    @abstractmethod
    def create_item(self, item_create: ItemCreate) -> Item:
        raise NotImplementedError
