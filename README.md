# instagram_api
GoWombat Test

- Clone repo
- Install from requirements.txt (pip install -r requirements.txt)
- Run django server 

## This API has
1. jwt auth in auth (simplejwt)
2. list of posts ordered by recent
3. create post (Post has caption and image post)
4. create comment 
5. like post 
6. get likes for post 
7. get comments for post
8. create reply to comment
9. get replies to comments

## API Routes
/ ==> "Displays API Routes"

/api/core/register/ ==> "POST user details to register new user (email,username,password)"

/api/token/ ==> "POST login to get JWT access and refresh tokens (login with username,password)"

/api/token/refresh/ ==> "POST refresh token to get new JWT access token"

/api/core/posts/ ==> "GET all posts"

/api/core/posts/create/ ==> "POST to create new post (caption, post<image>)"
  
/api/core/posts/like/ ==> "POST to like post (post<pk>)"
  
/api/core/posts/likes/pk/ ==> "GET likes for post"
  
/api/core/posts/comments/create/ ==> "POST to comment on post (comment, post<pk>)"
  
/api/core/posts/comments/pk/ ==> "GET comments for post"
  
/api/core/posts/comments/reply/ ==> "POST to reply to comment (reply,comment<pk>)"
  
/api/core/posts/comments/replies/pk/ ==> "GET replies for comment"
