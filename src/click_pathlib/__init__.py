"""
Custom click types.
"""

import pathlib
from typing import Any, Optional

import click


class Path(click.Path):
    """
    A Click path argument that returns a ``Path``, not a string.
    """

    def convert(
        self,
        value: str,
        param: Optional[click.core.Parameter],
        ctx: Optional[click.core.Context],
    ) -> Any:
        """
        Return a ``Path`` from the string ``click`` would have created with
        the given options.
        """
        return pathlib.Path(super().convert(value=value, param=param, ctx=ctx))
