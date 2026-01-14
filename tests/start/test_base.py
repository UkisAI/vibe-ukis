import pytest
import shutil
from pathlib import Path

from src.vibe_ukis.start import starter, services
from src.vibe_ukis.start.terminal import app1, app2, app3
from prompt_toolkit.application import Application
from src.vibe_ukis.start.utils import write_file, get_instructions


@pytest.mark.asyncio
async def test_starter() -> None:
    """Test the starter function with new agent structure (Cursor, Claude Code, Windsurf, Antigravity)"""
    # Clean up any existing test directories
    test_dirs = [".cursor", ".claude", ".windsurf", ".antigravity"]
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

    # Test with Cursor agent and Firecrawl service
    try:
        await starter(agent="Cursor", service="Firecrawl", verbose=False)
        success = True
    except Exception as e:
        print(f"Exception occurred with Firecrawl: {e}")
        success = False
    assert success, "starter() should complete without exceptions for Firecrawl"

    # Check that the Cursor rules directory was created
    assert Path(".cursor/rules").exists(), ".cursor/rules directory should be created for Firecrawl"

    # Clean up
    if Path(".cursor").exists():
        shutil.rmtree(".cursor")

    # Test with Cursor agent and Qdrant service
    try:
        await starter(agent="Cursor", service="Qdrant", verbose=False)
        success = True
    except Exception as e:
        print(f"Exception occurred with Qdrant: {e}")
        success = False
    assert success, "starter() should complete without exceptions for Qdrant"

    # Check that the Cursor rules directory was created
    assert Path(".cursor/rules").exists(), ".cursor/rules directory should be created for Qdrant"

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
    """Test get_instructions for all services"""
    # Test LlamaIndex
    instr = await get_instructions(services["LlamaIndex"])
    with open(services["LlamaIndex"], "r", encoding="utf-8") as f:
        content = f.read()
    assert instr is not None
    assert instr == content

    # Test Chainlit
    instr_chainlit = await get_instructions(services["Chainlit"])
    with open(services["Chainlit"], "r", encoding="utf-8") as f:
        content_chainlit = f.read()
    assert instr_chainlit is not None
    assert instr_chainlit == content_chainlit

    # Test Firecrawl
    instr_firecrawl = await get_instructions(services["Firecrawl"])
    with open(services["Firecrawl"], "r", encoding="utf-8") as f:
        content_firecrawl = f.read()
    assert instr_firecrawl is not None
    assert instr_firecrawl == content_firecrawl

    # Test Qdrant
    instr_qdrant = await get_instructions(services["Qdrant"])
    with open(services["Qdrant"], "r", encoding="utf-8") as f:
        content_qdrant = f.read()
    assert instr_qdrant is not None
    assert instr_qdrant == content_qdrant


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


@pytest.mark.asyncio
async def test_claude_skills() -> None:
    """Test Claude Code skills generation with all services"""
    # Clean up any existing test directories
    if Path(".claude").exists():
        shutil.rmtree(".claude")

    # Test with Claude Code agent and LlamaIndex service
    try:
        await starter(agent="Claude Code", service="LlamaIndex", verbose=False)
        success = True
    except Exception as e:
        print(f"Exception occurred for Claude with LlamaIndex: {e}")
        success = False
    assert success, "starter() should complete without exceptions for Claude Code + LlamaIndex"
    assert Path(".claude/skills").exists(), ".claude/skills directory should be created"

    # Clean up
    if Path(".claude").exists():
        shutil.rmtree(".claude")

    # Test with Claude Code agent and Firecrawl service
    try:
        await starter(agent="Claude Code", service="Firecrawl", verbose=False)
        success = True
    except Exception as e:
        print(f"Exception occurred for Claude with Firecrawl: {e}")
        success = False
    assert success, "starter() should complete without exceptions for Claude Code + Firecrawl"
    assert Path(".claude/skills").exists(), ".claude/skills directory should be created for Firecrawl"

    # Clean up
    if Path(".claude").exists():
        shutil.rmtree(".claude")

    # Test with Claude Code agent and Qdrant service
    try:
        await starter(agent="Claude Code", service="Qdrant", verbose=False)
        success = True
    except Exception as e:
        print(f"Exception occurred for Claude with Qdrant: {e}")
        success = False
    assert success, "starter() should complete without exceptions for Claude Code + Qdrant"
    assert Path(".claude/skills").exists(), ".claude/skills directory should be created for Qdrant"

    # Clean up
    if Path(".claude").exists():
        shutil.rmtree(".claude")


@pytest.mark.asyncio
async def test_windsurf_rules() -> None:
    """Test Windsurf rules generation with all services"""
    # Clean up any existing test directories
    if Path(".windsurf").exists():
        shutil.rmtree(".windsurf")

    # Test with Windsurf agent and Firecrawl service
    try:
        await starter(agent="Windsurf", service="Firecrawl", verbose=False)
        success = True
    except Exception as e:
        print(f"Exception occurred for Windsurf with Firecrawl: {e}")
        success = False
    assert success, "starter() should complete without exceptions for Windsurf + Firecrawl"
    assert Path(".windsurf/rules").exists(), ".windsurf/rules directory should be created for Firecrawl"

    # Clean up
    if Path(".windsurf").exists():
        shutil.rmtree(".windsurf")

    # Test with Windsurf agent and Qdrant service
    try:
        await starter(agent="Windsurf", service="Qdrant", verbose=False)
        success = True
    except Exception as e:
        print(f"Exception occurred for Windsurf with Qdrant: {e}")
        success = False
    assert success, "starter() should complete without exceptions for Windsurf + Qdrant"
    assert Path(".windsurf/rules").exists(), ".windsurf/rules directory should be created for Qdrant"

    # Clean up
    if Path(".windsurf").exists():
        shutil.rmtree(".windsurf")


@pytest.mark.asyncio
async def test_antigravity_rules() -> None:
    """Test Antigravity rules generation with all services"""
    # Clean up any existing test directories
    if Path(".antigravity").exists():
        shutil.rmtree(".antigravity")

    # Test with Antigravity agent and Firecrawl service
    try:
        await starter(agent="Antigravity", service="Firecrawl", verbose=False)
        success = True
    except Exception as e:
        print(f"Exception occurred for Antigravity with Firecrawl: {e}")
        success = False
    assert success, "starter() should complete without exceptions for Antigravity + Firecrawl"
    assert Path(".antigravity/rules").exists(), ".antigravity/rules directory should be created for Firecrawl"

    # Clean up
    if Path(".antigravity").exists():
        shutil.rmtree(".antigravity")

    # Test with Antigravity agent and Qdrant service
    try:
        await starter(agent="Antigravity", service="Qdrant", verbose=False)
        success = True
    except Exception as e:
        print(f"Exception occurred for Antigravity with Qdrant: {e}")
        success = False
    assert success, "starter() should complete without exceptions for Antigravity + Qdrant"
    assert Path(".antigravity/rules").exists(), ".antigravity/rules directory should be created for Qdrant"

    # Clean up
    if Path(".antigravity").exists():
        shutil.rmtree(".antigravity")


def test_terminal_apps() -> None:
    assert isinstance(app1, Application)
    assert isinstance(app2, Application)
    assert isinstance(app3, Application)
