from pycricbuzz import Cricbuzz
import json

c = Cricbuzz()

matches = c.matches()


def liveScore():
	"""Live Score."""
	head,teams,matchType,status=[],[],[],[]
	for match in matches:
		#print(json.dumps(c.livescore(match['id']),indent=4))
		game = c.livescore(match['id'])
		head.append(game['matchinfo']['srs'])
		teams.append(game['matchinfo']['mchdesc'])
		matchType.append(game['matchinfo']['type'])
		status.append(game['matchinfo']['status'])
		
	return (head,teams,matchType,status)

def commentary():
	"""Commentry."""
	for match in matches:
		print(json.dumps(c.commentary(match['id']),indent=4))

def scoreCard():
	"""Score Card."""
	for match in matches:
		print(json.dumps(c.scorecard(match['id']),indent=4))
		break

liveScore()