# QuizApp
## This is a submission for the module software design
The implemented program adheres to the following task definition:

There should be a quiz application for daily pastime.
In the application there are two roles, the User and the Registered User.
When starting the application, there are three options:
- The current user, can select an existing quiz and play it.
- The current user, can log in with username and password.
- The current user can register if he is not registered yet.

### Activity: Registration 
During registration it is necessary to enter a username (alphanumeric, no special characters) and a password.
Registered users are then saved in a corresponding file.
Catch: An already registered user cannot register again.

### Activity: Registration
A registered user can log in with the user name and password.
For simplicity, the login data should be checked against the data in the file.
Appropriate security measures, that the password is not visible, etc. are not required.

### Activity: Create quiz
The registered user has the possibility to complete the quiz after each created question, as long as the minimum number of questions are created.
Upon completion, the registered user must still decide whether the quiz is public for all users or only for this user.
The number of questions is also saved on the quiz.

### Activity: Main Menu
Once the registered user is logged in, he can create a quiz or play one of his own quizzes or play a public quiz.
In addition, he likewise has the option to view his statistics.
As keywords:
- Create Quiz
- Play Quiz
o Own quiz
o Public quiz

### Requirements: User
Attributes:
- Number of quizzes played
- Number of questions played
- Number of correctly answered questions

A user can only play public quizzes and view his statistics since the start of the application.
The user's statistics are discarded when the application is closed.

### Requirements: Registered user
Attributes:
- Inherits from user
- User name 
- Password: Inherits
- Statistics
On the registered user is stored how many quizzes he has played, how many questions he has answered and how many questions he has answered correctly.
Requirement: Statistics
A statistic visualizes the data:
- Number of quizzes played
- Number of played questions
- Number of correctly answered questions
z. B.:
 
These key figures are then visible in the statistics and are also weighted by percentage.
These statistics are stored permanently. Registered users are saved from which the statistic is generated when needed.
A user can only view his statistics since the start of the application.

### Requirements: Quiz
Attributes:
- A quiz consists of at least 3 questions and at most 10 questions.
- A quiz has a title.

### Requirements: Question
A question always has a specific question type:
- Choice
- Unique number 
- Unique text

#### Choice option:	
In a choice question, the question can have a minimum of 2 and a maximum of 4 answer choices.
How tall is the Eiffel Tower?
1. 1 meter
2. 20 meters
3. 300 meters
4. 768 meters

#### Unique number:
When was Germany the last soccer world champion?

Answer: 2014

#### Unique text:
What is the name of the famous yellow bear with red t-shirt who likes to be honey:

Answer: Winnie Pooh
