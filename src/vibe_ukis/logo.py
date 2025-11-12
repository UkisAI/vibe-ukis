from rich.console import Console
from rich_gradient.text import Text

logo = """
██╗   ██╗██╗██████╗ ███████╗       ██╗   ██╗██╗  ██╗██╗███████╗
██║   ██║██║██╔══██╗██╔════╝       ██║   ██║██║ ██╔╝██║██╔════╝
██║   ██║██║██████╔╝█████╗  █████╗ ██║   ██║█████╔╝ ██║███████╗
╚██╗ ██╔╝██║██╔══██╗██╔══╝  ╚════╝ ██║   ██║██╔═██╗ ██║╚════██║
 ╚████╔╝ ██║██████╔╝███████╗       ╚██████╔╝██║  ██╗██║███████║
  ╚═══╝  ╚═╝╚═════╝ ╚══════╝        ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝
"""


def print_logo() -> None:
    cs = Console()
    print("\n")
    cs.print(
        Text(logo, colors=["#89b4fa", "#9c59e7", "#a83ae8"]),
        justify="center",
    )
    print("\n")
    cs.print("-" * 50, style="gray bold", justify="center")
    print("\n")
