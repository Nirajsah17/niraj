---
author: niraj kumar sah
title: Github jekyll setup
tags: github, pages, actions, ruby, jekyll, static site geneartor, github profile.
description: Guide to setup github pages usning ruby && jekyll with minimal theme.
---

# Github Pages using Jekyll

## Getting Started

### Step 1 [Installation of ruby with ruby environmet manager similar to nvm]

1. Updating package manager and installing essential tools from apt

```bash
sudo apt update
sudo apt install -y curl gpg build-essential libffi-dev libyaml-dev libssl-dev libgdbm-dev libncurses5-dev libsqlite3-dev
```

2. Install rbenv and Ruby-build:

```bash
curl -fsSL https://github.com/rbenv/rbenv-installer/raw/main/bin/rbenv-installer | bash
```

3. Add rbenv to your shell:

```bash
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
source ~/.bashrc
```

4. Install Ruby:

```bash
rbenv install 3.2.0  # Or any latest version
rbenv global 3.2.0
```

### Step 2 [Install Bundler and Jekyll]

```bash
gem install bundler jekyll
```

### Step 3 [Create a repository]

1. Goto to your github and create new repo with `your_user_name` as repo name.

> Note : This repo considered as you profile repo, so no need to setup github workflow. Github automatically do it for you. Even though you can configured by your own as well.

2. Create file `_config.yml`

3. Add these lines

```bash
title: Niraj Kumar Sah # Your user_name
logo: ./images/niraj.png # Logo image path
description: Software Engineer @Mapmyindia # Description text
show_downloads: true # Tells you download option of your page (tar| zip) format
theme: jekyll-theme-minimal # here you can choose theme of your choices
```

> Note : Image path should be there, If not create directory `images` and put image `name.png`.

4. Create a `README.md` Add Profile Information

### Step 4 Configure jekyll

1. Create `Gemfile`

2. Add the following dependencies

```bash
source "https://rubygems.org"

gem "jekyll", "~> 3.9.5"
gem "github-pages", group: :jekyll_plugins
gem "webrick"  # Add this line
```

## Step 5 [Build and deploy]

1. Install related dependencies

```bash
bundle install
```

2. Build and serve

```bash
bundle exec jekyll serve
```

You have successfulluy serve your profile page at `https://localhost:4000`
