#!/usr/bin/env python

from bottle import route, run, static_file, view
from jira.client import JIRA
from ring3perf_dashboard.lib import config

_config = config.get_config()
_jira = JIRA(options={"server": _config.jira_url},
        basic_auth=(_config.jira_username, _config.jira_password))

@route("/")
@view("main")
def index():
    groups = _jira.search_issues("'assignee' = '%s' \
            AND 'project' = 'CA' \
            AND 'engineering tags' ~ 'ring3perfgroup'"
            % _config.jira_username)
    return dict(url=_config.jira_url, groups=groups)

@route("/static/<path:path>")
def static(path):
    return static_file(path, root="static")

if __name__ == "__main__":
    run(host=_config.server_ip, port=8080)
