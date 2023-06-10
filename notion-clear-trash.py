#!python3.10
# coding=utf-8
'''
 Author: Sanfor Chow
 Date: 2023-06-10 13:10:35
 LastEditors: Sanfor Chow
 LastEditTime: 2023-06-10 13:10:56
 FilePath: /notion-clear-trash/notion-clear-trash.py
'''
from notion.client import NotionClient


def get_trash(client):
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
                "inTeams": []},
            "sort": {"field": "lastEdited", "direction": "desc"},
            "limit": 1000,
            "spaceId": client.current_space.id,
            "source": "trash"
        }
    results = client.post('/api/v3/search', query)
    block_ids = results.json()['results']

    return [block_id['id'] for block_id in block_ids]


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def delete_permanently(client, block_ids):
    for block_batch in chunks(block_ids, 10):
        try:
            client.post("deleteBlocks", {"blockIds": block_batch, "permanentlyDelete": True})
        except Exception as err:
            print(err)
            print(block_batch)


if __name__== "__main__":
    token = input('Please enter your auth token: ')
    client = NotionClient(token_v2=token)

    block_ids = get_trash(client)
    delete_permanently(client, block_ids)
    print('Successfully cleared all trash blocks.')
