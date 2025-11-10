import pytest
from typing import Optional
from src.service.item import ItemServiceImpl
from src.repository.abc.i_item import IItemRepository
from src.schema.model.item import Item
from src.schema.request.item import ItemCreate


class MockItemRepository(IItemRepository):
    def get_item(self, item_id: int) -> Optional[Item]:
        if item_id == 1:
            return Item(id=1, name="Test Item", description="A test item")
        return None

    def create_item(self, item_create: ItemCreate) -> Item:
        return Item(id=2, **item_create.model_dump())


@pytest.fixture
def item_service() -> ItemServiceImpl:
    return ItemServiceImpl(item_repo=MockItemRepository())


def test_create_item(item_service: ItemServiceImpl):
    # Arrange
    item_to_create = ItemCreate(name="New Item", description="A new item")

    # Act
    created_item = item_service.create_item(item_to_create)

    # Assert
    assert created_item is not None
    assert created_item.id == 2
    assert created_item.name == "New Item"
    assert created_item.description == "A new item"


def test_get_item(item_service: ItemServiceImpl):
    # Act
    item = item_service.get_item(1)

    # Assert
    assert item is not None
    assert item.id == 1
    assert item.name == "Test Item"
