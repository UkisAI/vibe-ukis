from typing import Optional
from rich.console import Console

from .terminal import run_terminal_interface
from .utils import write_file, get_instructions
from .data import agent_rules, services
from .mcp import mcp_server
from .mcp_tools import mcp_tools, install_mcp_config, generate_mcp_json, run_mcp_server
from .mcp_terminal import run_mcp_terminal_interface
from .skills import create_claude_skills
from .windsurf import create_windsurf_rules
from .cursor import create_cursor_rules
from .antigravity import create_antigravity_rules


async def starter(
    agent: Optional[str] = None,
    service: Optional[str] = None,
    overwrite_files: Optional[bool] = None,
    verbose: Optional[bool] = None,
) -> bool:
    cs = Console(stderr=True)
    if agent is None and service is None:
        term_res = await run_terminal_interface()
        if not term_res:
            cs.log(
                "[bold red]ERROR[/]\tYou need to choose at least one agent and one service before continuining. Exiting..."
            )
            return False
        agent_files, service_urls, overwrite_files = term_res
        if agent_files is None or service_urls is None:
            cs.log(
                "[bold red]ERROR[/]\tYou need to choose at least one agent and one service before continuining. Exiting..."
            )
            return False
    elif agent is not None and service is not None:
        agent_files = [agent_rules[agent]]
        service_urls = [services[service]]
    else:
        cs.log(
            "[bold red]ERROR[/]\tEither you pass the options from command line or you choose them from terminal interface, you can't mix the two."
        )
        return False
    instructions = ""
    services_content = {}  # Store service name -> content mapping

    for serv_url in service_urls:
        if verbose:
            cs.log(f"[bold cyan]FETCHING[/]\t{serv_url}")
        instr = await get_instructions(instructions_url=serv_url)
        if instr is None:
            cs.log(
                f"[bold yellow]WARNING[/]\tIt was not possible to retrieve instructions for {serv_url}, please try again later"
            )
            continue
        instructions += instr + "\n\n---\n\n"

        # Store content by service name for skills generation
        for service_name, service_path in services.items():
            if service_path == serv_url:
                services_content[service_name] = instr
                break

        if verbose:
            cs.log("[bold green]FETCHED✅[/]")

    if not instructions:
        cs.log(
            "[bold red]ERROR[/]\tIt was not possible to retrieve instructions at this time, please try again later"
        )
        return False

    for fl in agent_files:
        # Check if this is the Claude skills directory
        if fl == ".claude/skills/":
            if verbose:
                cs.log(f"[bold cyan]CREATING CLAUDE SKILLS[/]\t{fl}")
            created = create_claude_skills(
                base_dir=".claude",
                services_content=services_content,
                overwrite=overwrite_files or False,
                verbose=verbose,
            )
            total_created = sum(len(files) for files in created.values())
            if total_created > 0:
                cs.log(
                    f"[bold green]CREATED CLAUDE SKILLS STRUCTURE WITH {total_created} FILE(S)✅[/]"
                )
            else:
                cs.log(
                    "[bold yellow]No new skills created (files may already exist)[/]"
                )
        # Check if this is the Windsurf rules directory
        elif fl == ".windsurf/rules/":
            if verbose:
                cs.log(f"[bold cyan]CREATING WINDSURF RULES[/]\t{fl}")
            created = create_windsurf_rules(
                base_dir=".windsurf",
                services_content=services_content,
                overwrite=overwrite_files or False,
                verbose=verbose,
            )
            total_created = sum(len(files) for files in created.values())
            if total_created > 0:
                cs.log(
                    f"[bold green]CREATED WINDSURF RULES STRUCTURE WITH {total_created} FILE(S)✅[/]"
                )
            else:
                cs.log("[bold yellow]No new rules created (files may already exist)[/]")
        # Check if this is the Cursor rules directory
        elif fl == ".cursor/rules/":
            if verbose:
                cs.log(f"[bold cyan]CREATING CURSOR RULES[/]\t{fl}")
            created = create_cursor_rules(
                base_dir=".cursor",
                services_content=services_content,
                overwrite=overwrite_files or False,
                verbose=verbose,
            )
            total_created = sum(len(files) for files in created.values())
            if total_created > 0:
                cs.log(
                    f"[bold green]CREATED CURSOR RULES STRUCTURE WITH {total_created} FILE(S)✅[/]"
                )
            else:
                cs.log("[bold yellow]No new rules created (files may already exist)[/]")
        # Check if this is the Antigravity rules directory
        elif fl == ".antigravity/rules/":
            if verbose:
                cs.log(f"[bold cyan]CREATING ANTIGRAVITY RULES[/]\t{fl}")
            created = create_antigravity_rules(
                base_dir=".antigravity",
                services_content=services_content,
                overwrite=overwrite_files or False,
                verbose=verbose,
            )
            total_created = sum(len(files) for files in created.values())
            if total_created > 0:
                cs.log(
                    f"[bold green]CREATED ANTIGRAVITY RULES STRUCTURE WITH {total_created} FILE(S)✅[/]"
                )
            else:
                cs.log("[bold yellow]No new rules created (files may already exist)[/]")
        else:
            # Regular file writing for standard agents
            if verbose:
                cs.log(f"[bold cyan]WRITING[/]\t{fl}")
            write_file(
                fl, instructions, overwrite_files or False, ", ".join(service_urls)
            )
            if verbose:
                cs.log("[bold green]WRITTEN✅[/]")
    cs.log(
        "[bold green]SUCCESS✅[/]\tAll the instructions files have been written, happy vibe-coding!"
    )
    cs.log(
        "[bold yellow]⚠️  IMPORTANT[/]\tPlease restart Cursor/Windsurf/Claude Code/Antigravity for vibe-ukis to start working!"
    )
    return ".vibe-ukis/rules/AGENTS.md" in agent_files


__all__ = [
    "starter",
    "agent_rules",
    "services",
    "mcp_server",
    "mcp_tools",
    "install_mcp_config",
    "generate_mcp_json",
    "run_mcp_server",
    "run_mcp_terminal_interface",
]
