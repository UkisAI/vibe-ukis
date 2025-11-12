import os
import httpx
import asyncio

from pathlib import Path
from typing import Optional


def write_file(
    file_path: str, content: str, overwrite_file: bool, service_url: str
) -> None:
    directory = os.path.dirname(file_path)
    if not Path(directory).is_dir():
        os.makedirs(directory, exist_ok=True)
    if not overwrite_file:
        if Path(file_path).is_file():
            with open(file_path, encoding="utf-8") as f:
                file_content = f.read()
            content = file_content + "\n" + content
    if file_path.startswith(".cursor"):
        # Extract service name from local path or use URL
        service_name = (
            Path(service_url).stem if os.path.exists(service_url) else service_url
        )
        frontmatter = f"""---
description: Instructions from {service_name} for Cursor coding agent
alwaysApply: false
---

"""
        content = frontmatter + "\n" + content
    with open(file_path, "w", encoding="utf-8") as w:
        w.write(content)
    return None


async def get_instructions(
    instructions_url: str, max_retries: int = 10, retry_interval: float = 0.5
) -> Optional[str]:
    # Check if it's a local file path
    if os.path.exists(instructions_url):
        try:
            with open(instructions_url, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print(f"Error reading local file {instructions_url}: {e}")
            return None

    # Validate that it's a proper URL before attempting HTTP request
    if not instructions_url.startswith(("http://", "https://")):
        print(
            f"Error: '{instructions_url}' is neither a valid file path nor a valid URL"
        )
        return None

    # Fetch from URL
    async with httpx.AsyncClient() as client:
        retries = 0
        while True:
            if retries < max_retries:
                try:
                    response = await client.get(instructions_url)
                    if response.status_code == 200:
                        return response.text
                    else:
                        retries += 1
                        await asyncio.sleep(retry_interval)
                except Exception as e:
                    print(f"Error fetching URL {instructions_url}: {e}")
                    return None
            else:
                return None
