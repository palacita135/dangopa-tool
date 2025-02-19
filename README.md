# dangopa-tool
OSINT - TOOL

clone this repository

    git clone https://github.com/palacita135/dangopa-tool.git
    cd dangopa-tool
    chmod +x dangopa.py
    python3 dangopa.py

don't forget to replace your Shodan API KEY

Commands available:
    
    email <URL> → Find emails on a website.
    phone <URL> → Extract phone numbers.
    shodan <IP> → Lookup IP details.
    clear → Clears the screen.
    exit → Closes the program.\

Packaging into an Executable for Windows USER

    pip install pyinstaller
    pyinstaller --onefile dangopa.py

Have a good day fellas
