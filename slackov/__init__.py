#!/usr/bin/env python

from slacksocket import SlackSocket
from markoff import Markoff
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description=
        'A Slack bot that uses Markov chains to learn to speak like a generic \
        member of your team')
    parser.prog = 'slackov'
    parser.add_argument('--token','-t',
            required=True, type=str, nargs=1, help='Slack RTM API Token')
    parser.add_argument('--verbose','-v',
            help='Log events to stdout', action='store_true')
    parser.add_argument('--file','-f',
            required=False, type=str, nargs='?', default=None,
            help='Recieved phrases backup file')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    api_token = args.token

    try:
        s = SlackSocket(api_token,translate=False,event_filters=['message'])
    except Exception:
        print('SlackAPI Error: exiting.')
        exit(1)
    print('Connected to team: ' + s.team)

    markov = Markoff(args.file)
    if args.verbose and args.file:
        print('Markoff initialized with file: ' + args.file + '\n\nBots:')
        

    # Compile list of other bots to avoid processing their text
    bots = []
    for user in s.loaded_users:
        if user['is_bot']:
            bots.append(user['id'])
            if args.verbose:
                print(user['id'])

    
    try:

        while(1):
            # Useful message info
            event = s.get_event()
            channel = event.event['channel']
            body = event.event['text']
            msg_user = event.event['user']

            # If slackov is addressed
            if s.user in body:
                response = markov.gen_sentence()
                s.send_msg(response,channel_id=channel,confirm=False)
                if args.verbose:
                    print('Sent: ' + response + '\n\tto: ' + channel)

            # Add text to markoff data structure if message is from a human
            elif msg_user not in bots:
                markov.add_vocab(body)
                if args.verbose:
                    print('Adding text: ' + body)

    except Exception:
        print("other")
    except KeyboardInterrupt:
        print('Keyboard Interrupt: quiting.')
    finally:
        s.close()

if __name__ == "__main__":
    main()
