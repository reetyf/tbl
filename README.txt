Hailey Weinschenk - Tampa Bay Lightning Take Home Assignment - Summer 2023

To create this API for this submission, I used the 

The return type is a .csv file that will download to the prompter's browser when visiting the following routes. This was returned using the FastAPI.responses StreamingResponse library.

ROUTES
/stats : returns a .csv of the current snapshot of the player stats

/stats/player/top_{x}_{stat} : Returns the top x talliers of any available stat.
			  x must be an int within the scope of the players list
			  stat: must be one of
		GP	G	A	P	+/-	PIM	PPG	SHG	GWG				S	S%			SecPerGP	MinPerGP		Shifts/GP	FOW%	Season	PPP			SH

		NOTE 
		for +/- use +
 		FOW% and S% use FOW and SP, respectively.

/stats/team/top_{x}_{stat} : Returns the top talliers for the stats for sorted by Teams
			    x must be within 1 to 32 representing the teams in the NHL


/roster/{team} : Returns the current roster of the given team. Team must be the standard abbv. for one of the 32 NHL teams (i.e TBL, VGK, TOR, NYI, etc.)

/multi-team-player: Returns the player or players who appeared on the most teams in the 2022-2023 season.