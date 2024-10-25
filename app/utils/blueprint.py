# To recreate Instagram's backend logic, here's a list of potential endpoints you might want to implement:
#
# 1. User Authentication & Authorization
# POST /auth/signup – User registration (with username, email, password, etc.).
# POST /auth/login – User login (JWT token-based).
# POST /auth/logout – User logout.
# POST /auth/password-reset – Password reset request.
# PUT /auth/password-update – Update password after verification.


# 2. User Profile
# GET /user/{username} – Fetch user profile details.
# PUT /user/{username} – Edit user profile details (bio, name, etc.).
# PUT /user/{username}/avatar – Upload/change user profile picture.
# GET /user/{username}/posts – Fetch posts by user.
# GET /user/{username}/followers – Get the list of followers.
# GET /user/{username}/following – Get the list of followed accounts.


# 3. Posts & Media
# POST /post/create – Create a new post (with image or video, caption, tags).
# GET /post/{post_id} – Fetch a specific post (image, caption, comments).
# DELETE /post/{post_id} – Delete a post.
# PUT /post/{post_id}/edit – Edit caption or tags of a post.
# GET /posts/feed – Fetch the feed with posts from followed accounts.
# POST /post/{post_id}/like – Like a post.
# DELETE /post/{post_id}/like – Unlike a post.
# GET /post/{post_id}/likes – Get a list of users who liked the post.


# 4. Comments
# POST /post/{post_id}/comment – Add a comment to a post.
# GET /post/{post_id}/comments – Fetch comments on a post.
# PUT /comment/{comment_id}/edit – Edit a comment.
# DELETE /comment/{comment_id} – Delete a comment.
# POST /comment/{comment_id}/like – Like a comment.
# DELETE /comment/{comment_id}/like – Unlike a comment.


# 5. Stories
# POST /story/create – Upload a story (image/video).
# GET /story/feed – Get the list of stories from followed accounts.
# GET /story/{story_id} – View a specific story.
# DELETE /story/{story_id} – Delete a story.
# POST /story/{story_id}/like – Like a story.
# DELETE /story/{story_id}/like – Unlike a story.
# GET /story/{story_id}/likes – Get a list of users who liked the story.


# 6. Direct Messaging (DM)
# POST /dm/{recipient_username}/send – Send a direct message.
# GET /dm/conversations – Fetch the list of conversations.
# GET /dm/conversations/{conversation_id} – Fetch specific conversation.
# POST /dm/{conversation_id}/message/{message_id}/delete – Delete a message.


# 7. Notifications
# GET /notifications – Fetch all notifications for the user.
# PUT /notifications/read – Mark notifications as read.
# DELETE /notifications/{notification_id} – Delete a notification.
# 8. Follow/Unfollow
# POST /user/{username}/follow – Follow a user.
# DELETE /user/{username}/follow – Unfollow a user.
# GET /user/{username}/followers – Get the list of followers.
# GET /user/{username}/following – Get the list of followed accounts.


# 9. Search
# GET /search/users – Search for users by username.
# GET /search/tags – Search for posts by tags.


# 10. Explore/Discover
# GET /explore/trending – Fetch trending posts.
# GET /explore/suggested – Fetch suggested accounts to follow.


# 11. Hashtags
# GET /tags/{tag_name}/posts – Fetch posts related to a specific hashtag.
# POST /tags/follow – Follow a hashtag.
# DELETE /tags/unfollow – Unfollow a hashtag.


# 12. Analytics (Optional)
# GET /user/{username}/analytics – Get analytics for a user’s profile (followers growth, post performance).
# GET /post/{post_id}/analytics – Get analytics for a specific post (likes, views, etc.).
# This is a general list of endpoints you could consider. You can build on top of these by adding more advanced
# features like reels, ads management, or business accounts, depending on your scope.
