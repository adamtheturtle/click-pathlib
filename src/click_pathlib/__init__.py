"""
Custom click types.
"""

from __future__ import annotations

import pathlib
from typing import Any

import click


class Path(click.Path):
    """
    A Click path argument that returns a ``Path``, not a string.
    """

    def convert(
        self,
        value: str,
        param: click.core.Parameter | None,
        ctx: click.core.Context | None,
    ) -> Any:
        """
        Return a ``Path`` from the string ``click`` would have created with
        the given options.
        """
        return pathlib.Path(super().convert(value=value, param=param, ctx=ctx))
