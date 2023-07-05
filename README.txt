Hailey Weinschenk - Tampa Bay Lightning Take Home Assignment - Summer 2023

To create this API for this submission, I used the FastAPI library. Output was originally chosen to be JSON, but then changed to StreamingResponse to most easily align with the developers wishes to be imported to .xlsx. The table queries themselves were completed using pandas.

The return type is a .csv file that will download to the prompter's browser when visiting the following routes.

ROUTES
/stats : returns a .csv of the current snapshot of the player stats from nhl.com

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



DOCKER USAGE: 
Link on Docker Hub (https://hub.docker.com/repository/docker/reetyf/tampabay/general)


docker  pull reetyf/tampabay:tbl
docker run -d   -p 80:80 reetyf/tampabay:tbl 



(I'm 99% sure that this method of pulling from docker should work, but just in case, I've attached all files to this email!)
