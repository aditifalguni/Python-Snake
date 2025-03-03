<h1> Algorithm:</h1>
1. Create Game window
2. Keep the window open (main loop) 
3. Create Canvas to draw on 
4. Fix the position of the
5. Calculate X.Y coordinates for drawing 
6. Add X,Y position to the then window 
7. Sort the X,Y position (Create Tile Class) 
8. Initialize game (position snake head and food) 
9. Draw snake (co-ordinate, color, size) 
10. Loop the snake (*call draw again every 100ms )* 
11. Add speed to move the snake 
12. Draw **Key listener** [change direction on key release] 
(Key Release → detects *when you press on any key and then let go)*  
keysym( key symbol) → *able to register, which key have been pressed*
13. **Game loop** ( logic → when up pressed snake goes up && not going towards down 
(*while pressing a key, make sure not gong to the opposite direction, in a game of snake mouth cannot go towards the tail )* 
14. **Next Positions** (X, Y position while moving the snake) 
15. **call move()** function before drawing the snake (*calling move within draw function-> snake moves 10 frames per sec)* 
16. **clear the previous frame** *every time after drawing the new frame, otherwise gets overlapped*
17. **draw the food first,** *(before the snake) so it doesn't cover the snake when they collide* 
18. Sort all the snake Body parts (list/ Array) 
19. **Detect Collision** with food ( X,Y *position of the food and snake are the same) → when this happens add a segment to the body → then move the food to another random location →later  (add to the score )*
20. Add Snake body (Grow snake after eating food) 
21. Move (snake with the body)
22. Update snake body (*move the snakes body starting from the back )*
23.  *GAME OVER → snake collides with its body && Walls*
24. Stop snake movement (*if game over, the snake won't respond to key presses, snake will stop moving)* 
25. Add & Show Score 
26. Draw game over & Score

<h1> Add Functionalities:</h1>
1. Restart Button
2. Main Menu 
3. Different mode -> calssic, endless, maze, 
4. Add difficulty -> increase speed, minus point
5. HIGH SCORE 
