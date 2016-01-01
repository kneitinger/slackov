from slackclient import SlackClient
from markoff import Markoff

class Slackov:
    def __init__(self, token, file=None, quiet=False):
        try:
            self._sc = SlackClient(token)
            self._sc.rtm_connect()
        except Exception:
            print('Slack API error. Exiting.')
            exit(1)

        self.name = self._sc.server.login_data['self']['id']
        print('Connected as: ' + self.name)
        self._markoff = Markoff(file)

    def poll_events(self):
        events = self._sc.rtm_read()
        for e in events:
            # Ignore messages that slackov sends
            if 'type' in e:
                self.process_event(e)

    def process_event(self, event):
        if event['type'] == 'message' and 'subtype' not in event:
            body = event['text']
        
            if self.name in body:
                msg = ''
                while len(msg) == 0:
                    msg = self._markoff.gen_sentence()
                print('Sending : ' + msg)
                self._sc.rtm_send_message(event['channel'], msg)
            else:
                print('Adding vocab: ' + body)
                self._markoff.add_vocab(body)
