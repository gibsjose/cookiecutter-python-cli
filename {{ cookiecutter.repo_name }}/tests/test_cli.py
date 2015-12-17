import pytest
from click.testing import CliRunner
from {{cookiecutter.package_name}} import cli


@pytest.fixture
def runner():
    return CliRunner()

def test_cli(runner):
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Hey!'

def test_cli_with_option(runner):
    result = runner.invoke(cli.main, ['-f'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Flag: True'

def test_cli_with_arg(runner):
    result = runner.invoke(cli.main, ['print', 'hello'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'hello'
