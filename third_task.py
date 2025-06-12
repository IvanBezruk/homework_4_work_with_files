import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_di_tree(path: Path, prefix: str = ""):
    #Prints the directory tree with color formatiing
    entries = sorted(path.iterdir(), key = lambda x: (not x.is_dir(), x.name.lower()))
    for idx, entry in enumerate(entries):
        connector = "┣ " if idx < len(entries) - 1 else "┗"
        if entry.is_dir():
            print(prefix + Fore.BLUE + connector + "📂" + entry.name + Style.RESET_ALL)
            print_dir_tree(entry, prefix + ("┃ " if idx < len(entries) - 1 else "  "))
        else:
            print(prefix + Fore.GREEN + connector + "📜" + entry.name + Style.RESET_ALL)
        
def main():
    init(autoreset = True) #Initiliazation of colorama
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python hw03.py C:\\path\\to\\your\\directory" + Style.RESET_ALL)
        sys.exit(1)

    dir_path = Path(sys.argv[1])
    if not dir_path.exists():
        print(Fore.RED + f"Error: Path {dir_path} does not exist." + Style.RESET_ALL)
        sys.exit(1)
    if not dir_path.is_dir():
        print(Fore.RED + f"Error: Path {dir_path} is not directory" + Style.RESET_ALL)
        sys.exit(1)

    print(Fore.YELLOW + F"Directory structure: {dir_path}" + Style.RESET_ALL)
    print_di_tree(dir_path)


if __name__=="__main__":
    main()