from base_test import BaseTestCase

from teams.model import Teams


class TeamsTest(BaseTestCase):
    def _make_teams_object(self):
        teams = Teams()
        teams._add_team_info(
            'demo',
            {
                "roles": {
                    "owners": [
                        "jerry",
                    ]
                },
                "jira": {
                    "scrum_team": "Demo Team",
                    "project": "DMO"
                }
            }
        )
        teams._add_team_info(
            'mystery-inc',
            {
                "roles": {
                    "owners": [
                        "dblake",
                        "fjones",
                        "nrogers",
                        "sdoo",
                        "vdinkley"
                    ]
                },
                "jira": {
                    "scrum_team": "Mystery Incorporated",
                    "project": "MYS"
                }
            }
        )
        teams._add_team_info(
            'planet-express',
            {
                "roles": {
                    "owners": [
                        "amy",
                        "bender",
                        "fjones",
                        "fry",
                        "hermes",
                        "leela",
                        "nrogers",
                        "theprofessor",
                        "zoidberg"
                    ]
                },
                "jira": {
                    "scrum_team": "Planet Express",
                    "project": "PLAN"
                }
            }
        )
        return teams

    def test_get_all_teams(self):
        obj = self._make_teams_object()

        self.assertEqual(
            obj.get_all_teams(),
            ['demo', 'mystery-inc', 'planet-express']
        )

    def test_get_team(self):
        obj = self._make_teams_object()

        self.assertEqual(
            obj.get_team('foo'),
            dict()
        )

        team = obj.get_team('demo')
        self.assertEqual(
            team['roles']['owners'],
            ['jerry']
        )
        self.assertEqual(
            team['jira']['scrum_team'],
            'Demo Team'
        )
        self.assertEqual(
            team['jira']['project'],
            'DMO'
        )

    def test_get_teams_by_user(self):
        obj = self._make_teams_object()

        self.assertEqual(
            obj.get_teams_by_user('brian'),
            set()
        )
        self.assertEqual(
            obj.get_teams_by_user('amy'),
            {'planet-express'}
        )
        self.assertEqual(
            obj.get_teams_by_user('fjones'),
            {'planet-express', 'mystery-inc'}
        )
