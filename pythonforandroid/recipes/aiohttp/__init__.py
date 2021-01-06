"""Build AIOHTTP"""
from typing import List
from pythonforandroid.recipe import CythonRecipe  # type: ignore


class AIOHTTPRecipe(CythonRecipe):  # type: ignore # pylint: disable=R0903
    """Build AIOHTTP"""

    version = "v3.7.3"
    url = "https://github.com/aio-libs/aiohttp/archive/{version}.zip"
    name = "aiohttp"

    depends = ["setuptools"]

    python_depends = [
        'attrs>=17.3.0',
        'chardet>=2.0,<4.0',
        'multidict>4.5,<7.0', 
        'async_timeout>=3.0,<4.0',
        'yarl>1.0,<2.0',
        'idna-ssl>=1.0; python_version<"3.7"',
        'typing_extensions>=3.6.5'
    ]


recipe = AIOHTTPRecipe()
