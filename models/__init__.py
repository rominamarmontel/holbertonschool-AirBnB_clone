#!/usr/bin/python3
"""
    import file_storage
"""

from models.engine import file_storage


"""
    creates variable storage to call reload
"""
storage = file_storage.FileStorage()
storage.reload()
