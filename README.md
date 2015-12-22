# slackov
A Slack bot that uses Markov chains to learn to speak like a generic member of your team

---

## Installation

Manual method:

'''
$ git clone https://github.com/kneitinger/slackov.git
$ cd slackov
$ sudo python setup.py install
'''

 Automatic method with 'pip':

'''
$ sudo pip install slackov
'''

## Usage

First, acquire a Slack API token by .  Store the API token in a file such as `~/.slackov_token` and luanch slackov with the command:

```
$ slackov -t "$(cat ~/.slackov_token)"
```

Additionally, you may specify a file where recieved messages are stored and/or loaded from, with the -f flag.  The -v flag enables verbose output to stdout, printing all recieved and sent messages.

```
$ slackov -t "$(cat ~/.slackov_token)" -f ~/.slackov_words -v
```

As expected, the -h flag prints the program usage.
