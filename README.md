SECCON 2019 Final (Domestic & International Contest) - Challenge 4: follow-me-again
====

About this CTF: https://www.seccon.jp/2019/akihabara/


Instructions
-----
I made black box programs called *box*.
Can you find the input which follows my execution trace?

### ATTACK POINT
There are 4 boxes called *attack-box* and attached below.
In other words, there are 4 problems (4 flags).

Submit your input to API `/attack/<_id>/submit` to get attack flag.
An example `sample-api-requestl.py` attached below describes how to request.

### DEFENSE POINT
There are 12 hourly rounds. Every round starts on xx:00.
For example, round 1 starts on Day 1 11:00, and round 7 starts on Day 2 10:00.

A new box and a new execution trace are provided in every round through API `/defense/latest.zip`.
Submit your input to API `/defense/latest/submit`.
If your input passes server-side checks **and if this is first correct submission in a round**, challenge server writes your team's defense keyword into `/defense/last/int/result` (for international contest) or `/defense/last/dom/result` (for domestic contest).

Boxes in defense rounds are variant of attack-box's Box1.

### About challenge server

- Server compares execution path of your input with original execution traces. You will get  attack flag (or writes your team's defense keyword) if these are the same.
- NOTE: You MUST NOT attack the challenge server (including too frequent access and directory bruteforce).
- Location: http://follow-me-again-int.seccon/ (for international contest) or http://follow-me-again-dom.seccon/ (for domestic contest)
- Format of API request and response body are MessagePack or file stream.

### Attached files
- Attack-box: attack-box.zip
- Source code of tracer: branchtrace.cpp
- Sample script to call APIs: sample-api-request.py


/files
----
Distributed fliles in the contest.


/solver
----
### /defense
There's a solver for attack box1 and defense boxes. My solver uses Triton.