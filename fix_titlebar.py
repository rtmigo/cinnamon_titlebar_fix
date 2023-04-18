import os.path
import shutil
from pathlib import Path

def confirm(message: str) -> bool:
    answer = ""
    while answer not in ["y", "n"]:
        answer = input(message.strip() + " ").lower()
    return answer == "y"

def backup_file(source: Path) -> None:
    for i in range(1000):
        new_path = source.parent / (source.name + f".bak{i}")
        if not new_path.exists():
            shutil.copy(str(source), str(new_path))
            print(f"Backup saved to {new_path}")
            return
    raise Exception(f"Failed to backup {source}")

gtk_css_file = Path(os.path.expanduser("~/.config/gtk-3.0/gtk.css"))

css_1_4 = """
headerbar {
	min-height: 36px;
}

headerbar button.titlebutton,
headerbar button.titlebutton image {
	min-width: 30px;
	min-height: 30px;
	-gtk-icon-transform: scale(1.4);
	background-size: 24px 24px;
}
"""

def fix():
    if gtk_css_file.exists():
        backup_file(gtk_css_file)
    print(f"Updating {gtk_css_file}")
    gtk_css_file.write_text(css_1_4)
    print("Done. Restart Cinnamon to see effect (try Ctrl+Alt+Esc).")


if __name__ == '__main__':
    if confirm(f"Replace {gtk_css_file} [Y/N]?"):
        fix()
