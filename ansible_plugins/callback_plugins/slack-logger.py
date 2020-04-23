from slack_webhook import Slack
import time
import os
import sys
import socket
from ansible.plugins.callback import CallbackBase

webhook_url = os.environ.get("SLACK_WEBHOOK_URL")

class CallbackModule(CallbackBase):
    hostname = socket.gethostname()
    playbook_name = os.path.basename(sys.argv[-1])
    start_time = time.time()

    def playbook_on_stats(self, stats):
        slack = Slack(url=webhook_url)
        message = "Host: {}\nPlaybook: {}\n Execution time:{}".format(self.hostname, self.playbook_name, time.time()-self.start_time)
        slack.post(text=message)
