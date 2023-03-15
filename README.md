# dotfiles

Dotfiles and scripts managed with [Chezmoi](https://www.chezmoi.io/).

## Dotfiles setup for the first time
If this is the first time setting up a machine, these are the steps needed to setup the dotfiles.

On Windows:
```
winget install twpayne.chezmoi
chezmoi init https://github.com/jnonino/dotfiles.git
chezmoi diff
chezmoi apply -v
```

On MacOS:
```
sh -c "$(curl -fsLS get.chezmoi.io)" -- -b $HOME/bin
chezmoi init https://github.com/jnonino/dotfiles.git
chezmoi diff
chezmoi apply -v
```

On Linux:
```
sh -c "$(curl -fsLS get.chezmoi.io)" -- -b $HOME/.local/bin
chezmoi init https://github.com/jnonino/dotfiles.git
chezmoi diff
chezmoi apply -v
```

On Windows Linux Subsystem (WSL):
```
sh -c "$(curl -fsLS get.chezmoi.io)"
chezmoi init https://github.com/jnonino/dotfiles.git
chezmoi diff
chezmoi apply -v
```

## Chezmoi tasks

These are some common tasks to perform with Chezmoi.

Pull the latest changes from the repository to see what would change, without applying the changes.
```
chezmoi git pull -- --autostash --rebase
chezmoi diff
```

Check for differences and apply changes.

If the changes are ok, then run this command to apply.
```
chezmoi diff
chezmoi apply
```

Pull the latest changes from the repository and apply them.
```
$ chezmoi update
```
Internally it runs `chezmoi git pull -- --autostash --rebase` and `chezmoi apply`

## TODO

- [Populate `~/.ssh/authorized_keys` with your public SSH keys from GitHub](https://www.chezmoi.io/user-guide/manage-different-types-of-file/#populate-sshauthorized_keys-with-your-public-ssh-keys-from-github)
- [Handle configuration files which are externally modified](https://www.chezmoi.io/user-guide/manage-different-types-of-file/#handle-configuration-files-which-are-externally-modified)
