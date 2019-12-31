# [Pathfinder Blog](https://pathfinder-blog.herokuapp.com/tools/):
A website for Pathfinder DMs and players alike to keep updated on their campaign bio and have useful tools readily accessible, including a blog and a combat assistant feature.

[Deployed website link.](https://pathfinder-blog.herokuapp.com/tools/)

## UX
#### Scope

Scope 1 - Beta version.

The website will allow users to keep a campaign blog and to use a series of tools to facilitate the running of a Pathfinder session or campaign. While it has been designed for Pathfinder players, those running campaigns on other RPG systems can also use the site.

Registered game masters will be able to create blog posts to follow-up on sessions or progress their story, and registered players who have an account on the site and follow a given game master will have access to the blog’s content.

The main tool in this version will be a combat assistant, which will allow game masters to keep track of the initiative points and turn order without the need to write down everything on pen and paper and reducing the chances of mistakes or delays.

Users who benefit from the app can decide to support the developer by leaving a tip.

Scope 2 - More personalisation and campaign manager

The advanced version of PathBlog will feature a Source Reference Document Database section which will provide information about different elements of the games such as creature profile and descriptions, maps, spells, etc. This will allow Game Masters to quickly access information they need.

It will also feature a more comprehensive campaign management system where Game Masters can keep internal notes and save the combat stats they’ve input using the combat assistant tool.

It will also be possible for registered users to leave a tip to their Game Master. This will be very handy for those game masters who are also hosts and have bought food, drinks or game-related things for the players to share, or for those running games professionally or semi-professionally.

##### User stories:

- As a beginner Game Master, I want to find a way to run combats more quickly, so I don’t have to make my players waste time while I’m calculating every turn.
- As an experienced Pathfinder player, I want to have access to the notes of previous campaigns, so I can prepare myself for upcoming sessions.
- As an aspiring fantasy writer, I want to have a platform for others to read about the story I’ve created for my campaign, so I can get feedback and polish my skills.
- As a Game Master who streams a campaign on Twitch, I want to be able to direct my audience to a site where they can follow me as a Game Master, so I can build a community of players.

## Features

##### Existing features

A blog system in which registered users can create posts which have a unique URL they can share with their players.

A login system that prevents non-registered users from accessing the content section. This feature doesn’t prevent them from using the combant assistant tool, which is public.

A combat assistant tool which allows Game Masters to add the different players, monsters and other characters to a combat queue and automatically assigns them a turn depending on the results of their initiative roll (a number obtained by rolling a dice). The tool allows the Game Master to progress the turns, and to keep track of whose turn it is at all times, as well as making a note over characters who have become inactive.

A “Leave a Tip” section where users of the app can support the developer. This is enabled with Stripe. (Using the test API platform for now, as it's a hobbyist project)

A comments section which allows readers and campaign players to leave comments using Disqus.

##### Desired features

- We aim to allow users to tip their Game Masters via peer to peer transactions using Stripe Connect. The proposed business model is to allow players to send money to their Game Master through the PathBlog platform, while the site owners take a very small percentage. The idea behind this is for players to thank the Game Master who may have incurred costs while planning a game session (food, snacks, game material, source books, miniatures are all common expenses for the Game Master and/or house host).

- We plan to have a database of elements that are part of the Pathfinder lore and rulebooks. The proposed idea is to parse CSV files into the models for the database app. For the front end, we will expose a dynamic DataTables.js table that calls on rows through its built-in AJAX server-side rendering method and leverage Django's pagination system to build a robust set of cumulative filters. Due to time constraints this has not been included in this release.

- The proposed campaign management system will have a repository of private notes that only the Game Master will have access to (opposite to the blog which is public). Only certain select elements will be exposed to specific players for that Game Master's campaign, which will allow the Game Master to dispense important items, notes, locations and secrets, which is a common trope in the Pen and Paper RPG systems.


## Technologies Used

- [Bootstrap 3](https://getbootstrap.com/docs/3.3/)
    - For front end styling and ready-made media queries.

- [JQuery](https://jquery.com)
    - For DOM manipulation.

- [Font Awesome](https://fontawesome.com/)
    - For better design and styling.

- [Amazon AWS](https://aws.amazon.com/)
    - Robust static and media file serving in the cloud.

- [PostgreSQL Database](https://www.postgresql.org/)
    - Relational database that provides easy storage for model rows.

### Testing

Below, each user story followed by a way in which PathBlog fulfils it:

- As a beginner Game Master, I want to find a way to run combats more quickly, so I don’t have to make my players waste time while I’m calculating every turn.
- A beginner game master will find our combat assistant tool easy to use, and very handy as they only have to input the combating character’s names and initiative totals and it will calculate the order and keep track of the turns with just a click.

- As an experienced Pathfinder player, I want to have access to the notes of previous campaign sessions, so I can prepare myself for upcoming sessions.
- As Game Masters will be able to write blog posts, their players can have access to this content anytime. This means that a Game Masters running a game for an experienced group can write down crucial information or things they could forget, and make this information available to their players.

- As an aspiring fantasy writer, I want to have a platform for others to read about the story I’ve created for my campaign, so I can get feedback and polish my skills.
- While some users can use the blog for very in-game, practical posting, a creative Game Master can use the posts as a platform to build a story that others can read. Thanks to the implementation of a comments section, readers can provide feedback or show engagement with the story.

- As a Game Master who streams a campaign on Twitch, I want to be able to direct my audience to a site where they can follow me as a Game Master, so I can build a community of players.
- Users can follow a Game Master and therefore have access to read their blog posts as well as interact with them via comments. The Game Master can link to their Twitch account or other social media and use blogging as a means to announce upcoming streams.


#### Manual Testing

1. Registering:
    1. Go to “Register” section: Page with registration form opens.
    2. Click “Create account” with all form fields still empty”: A message prompting the user to fill the empty fields appears.
    3. Password and password confirmation fields are not the same: A message saying “passwords do not match” appears.
    4. Fill all fields correctly and click “Create Account”: A success message informs the user this was completed.

2. Logging in:
    1. Open login page: It prompts user to input their name and password.
    2. Input wrong password: User can’t login. A message saying username or password were not recognised appears.
    3. Input correct password and username: User logs in successfully.

3. Using the Combat Assistant tool:
- Trying to add a combatant without adding its initiative value: Action fails.
- Adding a combatant’s name and initiative number and clicking on “Add Combatant”: New combatant is added to the list.
- Added three combatants with different initiatives and click “Sort initiative”: Combatant’s queue is rearranged from highest to lowest initiative score.
- Add a new combatant to an existing queue: Combatant appears at the bottom.
- Click “next turn”: The player who is next on the combat queue becomes the current turn holder, going to the top spot on the tool and having their name highlighted with a green background.
- Click on the “X” next to a player’s name: The player’s name remains in the queue but their name is striked through and a skull symbol appears next to it to indicate they’ve been removed from combat.

5. Leaving a tip:
- Click “Gift me a candy bar” to tip €1.50: A modal appears to take card details and indicates the correct amount to be paid.
- Click “Pay €1.50” while leaving the fields empty: The empty field’s borders turn red and the action fails.
- Input the wrong card details and try to pay: The card number field goes red and the action fails.
- Input the correct card details using a test card and trying to pay: Transaction is successful and a message appear letting the user know their tip was processed.
    - Test card details are: Card Num. = 4242 4242 4242 4242, CVV = 111, Expiry = Any date in the future, e.g.: 12/20

6. Creating a blog post:
    1. Click on “Create a new post”: Blog post creator opens.
        - Attempt to publish an empty blog post: A message appears prompting the user to fill the first required empty field, in this case, the title.
        - Attempt to publish a post that has a title but no content: A message appears prompting the user to fill in the content section.
    2. Filling both required fields and clicking to publish the post: Blog post is published successfully and user is taken to their new blog post’s unique URL.

7. Different screen sizes:
    - The site is mobile friendly, and it uses Bootstrap grids to provide a flexible and appealing structure that looks well both on desktop sizes and smartphones.
    - The style and colour palette remains consistent throughout different screen sizes and the text becomes smaller, but at no point it becomes so small that it impairs readability.

### Bugs and Issues

- While most of the content is responsive, some unusual and especially smaller screen sizes might crop a portion of the blog post's images.
- The SRD Database and Campaign Management sections are not in this release.
- The Stripe payments are meant to be a system where players can use the site as a platform to send money to 3rd parties through the use of Stripe Connect. The setup for Stripe Connect requires a registered company TAX number, and is unavailable in this release.

## Deployment

- Download or pull the repository.
- Install all required packages with `pip install -r requirements.txt`.
- Create a new Heroku project.
- [Follow the great guide from Vitor Freitas on how to deploy Django projects on Heroku](https://simpleisbetterthancomplex.com/tutorial/2016/08/09/how-to-deploy-django-applications-on-heroku.html)

### Credits and acknowledgements

[Richard Dalton](https://github.com/richardadalton) provided the base for the subscription code.

### Acknowledgements

Code Institute Tutor Niel McEwen
Mentors Richard Dalton and Matt Rudge
Code Institute room on Slack
Code Institute Alumni Gabriela Guedez