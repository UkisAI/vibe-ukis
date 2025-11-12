import pytest
import shutil
from pathlib import Path

from src.vibe_ukis.start import starter, services
from src.vibe_ukis.start.terminal import app1, app2, app3
from prompt_toolkit.application import Application
from src.vibe_ukis.start.utils import write_file, get_instructions


@pytest.mark.asyncio
async def test_starter() -> None:
    """Test the starter function with new agent structure (Cursor, Claude Code, Windsurf)"""
    # Clean up any existing test directories
    test_dirs = [".cursor", ".claude", ".windsurf"]
    for test_dir in test_dirs:
        if Path(test_dir).exists():
            shutil.rmtree(test_dir)

    # Test with Cursor agent and LlamaIndex service
    try:
        await starter(agent="Cursor", service="LlamaIndex", verbose=False)
        success = True
    except Exception as e:
        print(f"Exception occurred: {e}")
        success = False
    assert success, "starter() should complete without exceptions"

    # Check that the Cursor rules directory was created
    assert Path(".cursor/rules").exists(), ".cursor/rules directory should be created"

    # Clean up
    if Path(".cursor").exists():
        shutil.rmtree(".cursor")

    # Test with missing parameters (should return False)
    r = await starter(agent="Cursor")  # type: ignore
    assert not r, "starter() should return False when parameters are incomplete"

    # Test with invalid agent name
    with pytest.raises(KeyError):
        await starter(agent="InvalidAgent", service="LlamaIndex")

    # Test with invalid service name
    with pytest.raises(KeyError):
        await starter(agent="Cursor", service="InvalidService")


@pytest.mark.asyncio
async def test_get_instructions() -> None:
    instr = await get_instructions(services["LlamaIndex"])
    # services["LlamaIndex"] returns a local file path, not a URL
    # So we should read the file directly instead of using httpx
    with open(services["LlamaIndex"], "r", encoding="utf-8") as f:
        content = f.read()
    assert instr is not None
    assert instr == content


def test_write_file(tmp_path: Path) -> None:
    fl = tmp_path / "hello.txt"
    write_file(str(fl), "hello world\n", False, "https://www.llamaindex.ai")
    assert fl.is_file()
    assert fl.stat().st_size > 0
    write_file(str(fl), "hello world", False, "https://www.llamaindex.ai")
    with open(fl) as f:
        content = f.read()
    assert content == "hello world\n\nhello world"
    write_file(str(fl), "hello world\n", True, "https://www.llamaindex.ai")
    with open(fl) as f:
        content = f.read()
    assert content == "hello world\n"


def test_terminal_apps() -> None:
    assert isinstance(app1, Application)
    assert isinstance(app2, Application)
    assert isinstance(app3, Application)
