# !/usr/bin/env python
# -*- coding: UTF-8 -*-


from mongodb_cloud_helper import MongoLocalConnector
from mongodb_cloud_helper import local_mongo_api


def test_local_connection():
    assert MongoLocalConnector(user="user", password="pass").client()


def test_api_operations():
    api = local_mongo_api()
    assert api

    api.persist_one(
        database='test-db',
        collection='test-coll',
        document={'membership': 1})


def main():
    test_local_connection()
    test_api_operations()


if __name__ == "__main__":
    main()
