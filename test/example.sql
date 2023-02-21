select sum(s.score) from score as s join player as p
on  t.player_id = s.player_id 
join team as t 
on p.team_id = t.team_id 
where t.team_name = 'RCB'
and
s.date between ('12-2-2012','15-2-2015')

