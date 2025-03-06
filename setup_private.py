"""
This code is for setup user private data he automates create .env file with
user data he is (user_agent)
"""

import os


class SetupPrivateData:
    def __init__(self, user_agent: str = ''):
        self.user_agent = user_agent

        self.config_exists()

    def create_env_file(self, envfile='.env'):
        private_data = f"""USER_AGENT='{self.user_agent}'"""  # private data

        # TODO: create the env file

        with open(file=f'config/{envfile}', mode='w') as file:
            file.write(private_data)
            print(f'File {envfile} success created')

    def config_exists(self):
        try:
            if os.path.exists('config'):
                return self.create_env_file()
            else:
                print('not found packed config')
        except (FileExistsError, FileNotFoundError):
            ...


def main():
    return SetupPrivateData(
        user_agent=input('Enter your user agent: ').strip(),

    )


if __name__ == '__main__':
    main()
