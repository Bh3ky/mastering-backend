"""
json_storage.py

Handles saving and loading application data.
"""

import json
from pathlib import Path


class JsonStorage:
    """
    Handles persistence of banking data.
    """

    DATA_FILE = Path("data/bank_data.json")

    @classmethod
    def save(cls, data: dict) -> None:
        """
        Save application data.
        """

        cls.DATA_FILE.parent.mkdir(
            exist_ok=True
        )

        with open(
            cls.DATA_FILE,
            "w"
        ) as file:
            
            json.dump(
                data,
                file,
                indent=4
            )


    @classmethod
    def load(cls) -> dict:
        """
        Load application data.
        """

        if not cls.DATA_FILE.exists():
            return {
                "customers": [],
                "accounts": []
            }
        
        with open(
            cls.DATA_FILE,
            "r"
        ) as file:
            
            return json.load(file)