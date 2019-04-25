from pathlib import Path

import click
import click_pathlib
from click.testing import CliRunner


def test_example(tmp_path: Path) -> None:
    @click.command('delete')
    @click.argument(
        'existing_file',
        type=click_pathlib.Path(exists=True),
    )
    def delete(existing_file: Path) -> None:
        assert isinstance(existing_file, Path)
        existing_file.unlink()

    tmp_file = tmp_path / 'new.txt'
    tmp_file.touch()
    assert tmp_file.exists()
    runner = CliRunner()
    result = runner.invoke(
        delete,
        [str(tmp_file)],
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert not tmp_file.exists()
