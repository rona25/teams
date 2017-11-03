import json
import os

from collections import defaultdict


class Teams(object):
    def __init__(
            self,
            data_dir=None):
        """Constructor.

        :param data_dir: the data directory (optional).
        """
        super(Teams, self).__init__()

        self._teams = dict()
        self._users = defaultdict(set)

        if data_dir:
            self._load_data_from_dir(data_dir)

    def get_all_teams(self):
        """Retrieves the registered teams.

        :return: the registered teams
        :rtype: list
        """
        result = self._teams.keys()
        return sorted(result)

    def get_team(self, team):
        """Retrieves the team info.

        :param team: the requested team.
        :return: the team data
        :rtype: dict
        """
        if not team:
            return {}

        result = self._teams.get(team)
        return result or {}

    def get_teams_by_user(self, username):
        """Retrieves the teams that the specified user belongs to.

        :param username: the requested username.
        :return: the teams associated with the specified username
        :rtype: set
        """
        return self._users[username]

    def _load_data_from_dir(self, data_dir):
        """Loads the team data from a directory.

        :param data_dir: the directory containing the team info.
        """
        if not data_dir:
            return

        dir_files = os.listdir(data_dir)
        for next_file in dir_files:
            file_path = os.path.join(data_dir, next_file)
            if not os.path.isfile(file_path):
                continue

            with open(file_path, mode='r') as f:
                obj = json.load(f)
                self._add_team_info(next_file, obj)

    def _add_team_info(self, team_name, team_data):
        """Add team information in this object.

        :param team_name: the team name.
        :param team_data: the team data associated with the team name.
        """
        if not (team_name and team_data):
            raise ValueError('all parameters are required')

        elif not isinstance(team_data, dict):
            raise ValueError('team data must be a dictionary')

        # add the team
        self._teams[team_name] = team_data

        # add the users
        if team_data.get('roles') and team_data['roles'].get('owners'):
            for username in team_data['roles']['owners']:
                self._users[username].add(team_name)
