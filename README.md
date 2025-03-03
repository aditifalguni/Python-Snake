<h1> Algorithm:</h1>
1. Create Game window <br> 
2. Keep the window open (main loop) <br> 
3. Create Canvas to draw on <br> 
4. Fix the position of the <br> 
5. Calculate X.Y coordinates for drawing <br> 
6. Add X,Y position to the then window <br> 
7. Sort the X,Y position (Create Tile Class) <br> 
8. Initialize game (position snake head and food) <br> 
9. Draw snake (co-ordinate, color, size) <br> 
10. Loop the snake (*call draw again every 100ms )* <br> 
11. Add speed to move the snake <br> 
12. Draw **Key listener** [change direction on key release] 
(Key Release → detects *when you press on any key and then let go)*  
keysym( key symbol) → *able to register, which key have been pressed*<br> 
13. <b>Game loop</b> ( logic → when up pressed snake goes up && not going towards down 
(while pressing a key, make sure not gong to the opposite direction, in a game of snake mouth cannot go towards the tail ) <br> 
14. <b>Next Positions</b> (X, Y position while moving the snake) <br> 
15. <b>call move()</b> function before drawing the snake (*calling move within draw function-> snake moves 10 frames per sec)* <br> 
16. <b>clear the previous frame</b> every time after drawing the new frame, otherwise gets overlapped <br> 
17. <b>draw the food first,</b> (before the snake) so it doesn't cover the snake when they collide <br> 
18. Sort all the snake Body parts (list/ Array) <br> 
19. <b>Detect Collision</b> with food ( X,Y position of the food and snake are the same) → when this happens add a segment to the body → then move the food to another random location →later  (add to the score ) <br> 
20. Add Snake body (Grow snake after eating food) <br> 
21. Move (snake with the body) <br> 
22. Update snake body (move the snakes body starting from the back ) <br> 
23.  GAME OVER → snake collides with its body && Walls <br> 
24. Stop snake movement (*if game over, the snake won't respond to key presses, snake will stop moving)* <br> 
25. Add & Show Score <br> 
26. Draw game over & Score<br> 

<h1> Add Functionalities:</h1>
1. Restart Button<br> 
2. Main Menu <br> 
3. Different mode -> calssic, endless, maze, <br> 
4. Add difficulty -> increase speed, minus point<br> 
5. HIGH SCORE <br> 
