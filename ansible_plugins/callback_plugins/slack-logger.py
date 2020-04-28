from slack_webhook import Slack
import time
import os
import sys
import socket
from ansible.plugins.callback import CallbackBase

webhook_url = os.environ.get("SLACK_WEBHOOK_URL")

class CallbackModule(CallbackBase):
    user = os.getenv('USER')
    hostname = socket.gethostname()
    playbook_name = os.path.basename(sys.argv[-1])
    start_time = time.time()

    def playbook_on_stats(self, stats):
        if stats.failures:
            message = "Failure"
            color = 'danger'
        else:
            message = "Success"
            color = 'good'

        execution_time = time.time()-self.start_time

        slack = Slack(url=webhook_url)
        message = "{}@{}\nPlaybook: {}".format(self.user, self.hostname, self.playbook_name)

        fields = [{
                    "title": "Execution time",
                    "value": "{:10.2f}s".format(execution_time),
                    "short": True
                }]
        
        for cat in ("ok","changed","unreachable","failures","skipped","rescued","ignored"):
            fields.append(
                {
                    "title": cat.capitalize(),
                    "value": "{}".format(getattr(stats, cat, {}).get("default", 0)),
                    "short": True
                }
            )

        self._display.warning(stats.__dict__)
        payload = [{
            "fallback": "Ansible Play Recap for {}".format(self.playbook_name),
            "color": str(color),
            "title": "Ansible Play Recap : {}".format(self.playbook_name),
            "text": str(message),
            "fields": fields
        }]

        slack.post(attachments=payload)