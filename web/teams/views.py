import logging

from flask import abort
from flask import Blueprint
from flask import current_app
from flask import request

from .util import json_response

logger = logging.getLogger('teams.view')

main = Blueprint(
    'main',
    __name__,
)
KEY_TEAMS_OBJECT = 'teams'


@main.route("/membership", methods=['GET'])
@json_response
def get_teams_for_username():

    username = request.args.get('username', '')
    try:
        # TODO: add request metrics
        logger.debug('received user membership request: [%s]', username)
        teams = current_app.config[KEY_TEAMS_OBJECT].get_teams_by_user(username)

    except Exception, e:
        logger.error('error getting user membership: user [%s] / error [%s]',
                     username, e, exc_info=True)

        # TODO: add error metrics

        return abort(500)

    return sorted(teams)


@main.route("/teams", methods=['GET'])
@json_response
def get_all_teams():

    try:
        # TODO: add request metrics
        logger.debug('received all teams request')
        teams = current_app.config[KEY_TEAMS_OBJECT].get_all_teams()

    except Exception, e:
        logger.error('error getting all teams: error [%s]',
                     e, exc_info=True)

        # TODO: add error metrics

        return abort(500)
    return teams


@main.route("/teams/<team>", methods=['GET'])
@json_response
def get_teams_info(team):

    try:
        # TODO: add request metrics
        logger.debug('received single team request: [%s]', team)
        team_info = current_app.config[KEY_TEAMS_OBJECT].get_team(team)

    except Exception, e:
        logger.error('error getting team info: team [%s] / error [%s]',
                     team, e, exc_info=True)

        # TODO: add error metrics

        return abort(500)

    return team_info
