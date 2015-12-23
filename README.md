# slackov
A Slack bot that uses Markov chains to learn to speak like a generic member of your team

---

## Installation

Manual method:

```
$ git clone https://github.com/kneitinger/slackov.git
$ cd slackov
$ sudo python setup.py install
```

 Automatic method with 'pip':

```
$ sudo pip install slackov
```

## Usage

First, acquire a Slack API token by clicking on your team's name or user name in the top left corner of the screen. which opens the Slack menu,  From there, choose 'Apps & Custom Integrations'. There will be a button at the top-right corner that says 'Build your own', click that and then select 'Make a custom Integration'. Finally you will see 'Bots' listed.  Click on that and follow the steps to register the bot and receive the API token.  Store the API token in a file such as `~/.slackov_token` and launch slackov with the command:

```
$ slackov -t "$(cat ~/.slackov_token)"
```

Additionally, you may specify a file where received messages are stored and/or loaded from, with the -f flag.  The -v flag enables verbose output to stdout, printing all received and sent messages.

```
$ slackov -t "$(cat ~/.slackov_token)" -f ~/.slackov_words -v
```

As expected, the -h flag prints the program usage.
