SELECT S.hacker_id, H.name
FROM Submissions as S
LEFT JOIN Challenges as C ON S.challenge_id  = C.challenge_id
LEFT JOIN Difficulty as D ON C.difficulty_level = D.difficulty_level
LEFT JOIN Hackers as H ON S.hacker_id = H.hacker_id
WHERE S.score=D.score
GROUP BY S.hacker_id, H.name HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC, S.hacker_id
