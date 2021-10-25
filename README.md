# Flask Marvel Heroes

This project utilizes Python's Flask framework to construct a REST API that connects users to a Postgres 
database for authentication and storage of Marvel superhero information. The application is hosted live via Heroku.

The API requires a token for access, which is granted by the authentication process utilizing the Python secrets module. Therefore,
the API cannot be accessed without being authenticated.

Once authenticated, users can access the Profile page, which displays the user's email, token, and name. This token can be utilized 
in an API testing apparatus such as Insomnia or Postman to test the API functionality.

The Hero API has full CRUD functionality available. Headers & Hero schema are as follow:

Content-Type: application/json <br>
access-token: Bearer  <em><strong>INSERT TOKEN</strong></em>
<br><br>
{<br>
  "comics_appeared_in": "string",<br>
  "description": "string",<br>
  "hero_name": "string",<br>
  "id": "string - not required except within URL for delete/retrieve one",<br>
  "super_power": "string"
<br>}
  <br><br>


### Hope you enjoy!

<br>

 -- zP
