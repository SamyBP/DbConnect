import os
import sys

from dotenv import load_dotenv

from cmd.parser import CommandLineParser

if __name__ == '__main__':
    load_dotenv()
    creds = {
        "database": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD")
    }
    parser = CommandLineParser(creds)
    command = parser.get_command(sys.argv[1])
    command.execute()
