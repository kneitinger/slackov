from slackclient import SlackClient
from markoff import Markoff

class Slackov:
    def __init__(self, token, file=None, verbose=False):
        try:
            self._sc = SlackClient(token)
            self._sc.rtm_connect()
        except Exception:
            print('Slack API error. Exiting.')
            exit(1)

        self._markoff = Markoff(file)
        self.verbose = verbose

        self.name = self._sc.server.login_data['self']['id']
        if self.verbose:
            print('Connected as: ' + self.name)

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
                if self.verbose:
                    print('Sending : ', msg.encode('utf-8'))
                self._sc.rtm_send_message(event['channel'], msg)
            else:
                if self.verbose:
                    print('Adding vocab: ', body.encode('utf-8'))
                self._markoff.add_vocab(body)
