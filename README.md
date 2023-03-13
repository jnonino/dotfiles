# dotfiles

## Prerequisites

### Install Chezmoi

#### MacOS and Linux

Only for Linux, install these dependencies:
```
sudo apt-get install build-essential procps curl file git
```

Install [brew](https://brew.sh/)

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Only for Linux, it is recommended to install GCC.
```
brew install gcc
```

Install [Chezmoi](https://www.chezmoi.io/install/)

```
brew install chezmoi
```

## Dotfiles setup

Dotfiles manged with [chezmoi](https://www.chezmoi.io/).

Install Chezmoi and these dotfiles in an empty machine
```
$ sh -c "$(curl -fsLS get.chezmoi.io)" -- init --apply jnonino
```

Pull the latest changes from your repo and see what would change, without actually applying the changes.
```
$ chezmoi git pull -- --autostash --rebase && chezmoi diff
```

If the changes are ok, then run this command to apply.
```
$ chezmoi apply
```

Pull the latest changes from the repo and apply them. It runs the two previous commands in one line.
```
$ chezmoi update
```

## TODO

- [Populate `~/.ssh/authorized_keys` with your public SSH keys from GitHub](https://www.chezmoi.io/user-guide/manage-different-types-of-file/#populate-sshauthorized_keys-with-your-public-ssh-keys-from-github)
- [Handle configuration files which are externally modified](https://www.chezmoi.io/user-guide/manage-different-types-of-file/#handle-configuration-files-which-are-externally-modified)
