import cmd
import requests
import re
import shodan
from bs4 import BeautifulSoup

# ASCII Banner
BANNER = r"""
██████╗  █████╗ ███╗   ██╗ ██████╗  ██████╗ ██████╗  █████╗
██╔══██╗██╔══██╗████╗  ██║██╔════╝ ██╔═══██╗██╔══██╗██╔══██╗
██║  ██║███████║██╔██╗ ██║██║  ███╗██║   ██║██████╔╝███████║
██║  ██║██╔══██║██║╚██╗██║██║   ██║██║   ██║██╔═══╝ ██╔══██║
██████╔╝██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝██║     ██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝  ╚═╝
OSINT TOOL - DANGOPA | v1.0 | Coded by DirtyHeroes
"""

# Regex Patterns
EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
PHONE_REGEX = r'(\+?\d{1,2}\s?)?(\(?\d{1,4}\)?[\s\-]?)?(\d{1,4}[\s\-]?\d{1,4}[\s\-]?\d{1,4})'

# Set Your Shodan API Key
SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"

class DangopaShell(cmd.Cmd):
    intro = f"{BANNER}\nType 'help' for commands."
    prompt = ">> "

    # Email Search
    def do_email(self, arg):
        """Search for emails on a website. Usage: email <URL>"""
        if not arg:
            print("Usage: email <URL>")
            return
        try:
            response = requests.get(arg)
            emails = set(re.findall(EMAIL_REGEX, response.text))
            print("\n".join(emails) if emails else "No emails found.")
        except Exception as e:
            print(f"Error: {e}")

    # Phone Number Search
    def do_phone(self, arg):
        """Search for phone numbers on a website. Usage: phone <URL>"""
        if not arg:
            print("Usage: phone <URL>")
            return
        try:
            response = requests.get(arg)
            phones = set(re.findall(PHONE_REGEX, response.text))
            print("\n".join(phones) if phones else "No phone numbers found.")
        except Exception as e:
            print(f"Error: {e}")

    # Shodan IP Lookup
    def do_shodan(self, arg):
        """Search for IP information using Shodan. Usage: shodan <IP>"""
        if not arg:
            print("Usage: shodan <IP>")
            return
        try:
            api = shodan.Shodan(SHODAN_API_KEY)
            result = api.host(arg)
            print(f"IP: {result['ip_str']}\nOrganization: {result.get('org', 'N/A')}\nOS: {result.get('os', 'N/A')}")
        except Exception as e:
            print(f"Error: {e}")

    # Clear Screen
    def do_clear(self, arg):
        """Clear the screen."""
        print("\033c", end="")

    # Exit Tool
    def do_exit(self, arg):
        """Exit DANGOPA"""
        print("Exiting DANGOPA...")
        return True

if __name__ == "__main__":
    DangopaShell().cmdloop()
