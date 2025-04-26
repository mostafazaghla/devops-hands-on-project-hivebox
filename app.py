import sys
import argparse

# Application Version
APP_VERSION = "v0.0.1"

def print_version_and_exit():
    print(f"Current app version: {APP_VERSION}")
    sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description="Simple app with version info.")
    parser.add_argument('--version', action='store_true', help="Show the current app version and exit.")
    args = parser.parse_args()

    if args.version:
        print_version_and_exit()

    # You can add more code here if needed
    print("App is running...")

if __name__ == "__main__":
    main()
