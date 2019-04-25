import click
from pathlib import Path
# import click_pathlib

from click.testing import CliRunner


def test_example(tmp_path: Path) -> None:
    @click.command('delete')
    @click.argument(
        'existing_file',
        # type=click_pathlib.Path(exists=True),
    )
    def delete(existing_file: Path) -> None:
        pass
        # assert isinstance(existing_file, Path)

    runner = CliRunner()
    result = runner.invoke(
        delete,
        [str(tmp_path)],
        catch_exceptions=False,
    )
    import pdb; pdb.set_trace()
    assert result.exit_code == 0
