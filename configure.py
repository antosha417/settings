import errno
import os
import logging
import subprocess
from collections.abc import Iterable


ENV_ARGS = {
    'HOME': os.getenv('HOME')
}


class App:
    def __init__(self, name, from_='', to='', commands=None, installable=True):
        self.name = name
        self.from_ = from_.format(**ENV_ARGS)
        self.to = to.format(**ENV_ARGS)
        self.commands = commands
        self.installable = installable

    def install(self):
        logging.info('Installing {}'.format(self.name))
        if self.installable:
            cmd = 'apt install -y {}'.format(self.name)
            logging.info('running "{}"'.format(cmd))
            subprocess.run(cmd.split())

        if not self.commands:
            return

        for command in self.commands:
            command = command.split()
            subprocess.run(command)

    def configure(self):
        logging.info('Configuring {}'.format(self.name))
        if not self.from_ or not self.to:
            logging.info('Nothing to configure')
            return
        try:
            # creating destination directory
            os.mkdir(os.path.dirname(self.to))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        try:
            # removing existing config
            os.remove(self.to)
        except OSError as e:
            if e.errno != errno.ENOENT:
                raise

        os.symlink(os.path.abspath(self.from_), self.to)


class DefaultSettings:
    def __init__(self):
        self.apps = [
            App('git'),
            App('curl'),
            App('zsh', 
                'zsh/zshrc', 
                '{HOME}/.zshrc',
                commands=['sh zsh/oh-my-zsh.sh']),
            App('i3', 'i3/config', '{HOME}/.config/i3/config'),
            App('i3blocks', 'i3/i3blocks.conf', '{HOME}/.i3blocks.conf'),
            App('ideavim', 'idea/ideavimrc', '{HOME}/.ideavimrc', installable=False),
            App('vim', 'vim/vimrc', '{HOME}/.vimrc'),
            App('programmer_dvorak_on_startup', 
                commands=['rm /etc/default/keyboard', 
                          'cp programmer_dvorak/keyboard /etc/default/keyboard'],
                installable=False),
            App('russian_programmer_dvorak',
                'programmer_dvorak/ru',
                '/usr/share/X11/xkb/symbols/ru', 
                installable=False),
            App('i3lock-fancy'),
            App('nautilus-dropbox'),
            App('xautolock'),
            App('i3lock-fancy'),
            App('fonts-font-awesome'),
        ]

    def install_apps(self):
        subprocess.run('apt update'.split())
        subprocess.run('apt upgrade -y'.split())
        for app in self.apps:
            app.install()

    def configure_apps(self):
        for app in self.apps:
            app.configure()


class HomeSettings(DefaultSettings):
    pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info('something')
    settings = DefaultSettings()
    settings.install_apps()
    settings.configure_apps()

