import os
import logging
from notion.client import NotionClient
from dotenv import load_dotenv

# Configure logging format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Load environment variables
load_dotenv()


def get_trash(client):
    """
    Retrieves a list of IDs of the trash blocks in Notion.

    Args:
        client (NotionClient): An authenticated NotionClient instance.

    Returns:
        list: A list of block IDs that are in the trash.
    """
    query = {
        "type": "BlocksInSpace",
        "query": "",
        "filters": {
            "isDeletedOnly": True,
            "excludeTemplates": False,
            "navigableBlockContentOnly": True,
            "requireEditPermissions": False,
            "includePublicPagesWithoutExplicitAccess": False,
            "ancestors": [],
            "createdBy": [],
            "editedBy": [],
            "lastEditedTime": {},
            "createdTime": {},
            "inTeams": [],
        },
        "sort": {"field": "lastEdited", "direction": "desc"},
        "limit": 1000,
        "spaceId": client.current_space.id,
        "source": "trash",
    }
    results = client.post("/api/v3/search", query)
    return [block_id["id"] for block_id in results.json()["results"]]


def chunks(lst, n):
    """
    Yields successive n-sized chunks from a list.

    Args:
        lst (list): The list to be divided into chunks.
        n (int): The number of elements per chunk.

    Yields:
        list: An n-sized chunk from the list.
    """
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def delete_permanently(client, block_ids):
    """
    Deletes a list of blocks permanently from Notion.

    Args:
        client (NotionClient): An authenticated NotionClient instance.
        block_ids (list): A list of block IDs to be deleted.
    """
    for block_batch in chunks(block_ids, 10):
        try:
            client.post(
                "deleteBlocks", {"blockIds": block_batch, "permanentlyDelete": True}
            )
        except Exception as err:
            logging.error(f"Error deleting block batch: {err}, Batch: {block_batch}")


if __name__ == "__main__":
    try:
        token = os.getenv("NOTION_AUTH_TOKEN")
        if not token:
            logging.error(
                "No auth token provided. Please set NOTION_AUTH_TOKEN in your .env file."
            )
            exit(1)

        client = NotionClient(token_v2=token)

        block_ids = get_trash(client)
        if block_ids:
            delete_permanently(client, block_ids)
            logging.info(f"Successfully cleared {len(block_ids)} trash blocks.")
        else:
            logging.info("No trash blocks found.")

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        exit(1)
