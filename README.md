# Medical Map

## locates medical facilities for procedures

### This is a proof of concept mockup created for Alvin Healthcare.

**Check it out at medicalmap.us**

This mockup was created with dummy data as public medical pricing is hard to find. The backend database (PostgreSQL) is ready to scale and could easily handle incoming information.

Begin by typing into the search bar; you will see the current procedures in the database that match.

The current focus of the map is in NYC, and will automatically center there by default. If you allow the app to use your IP address for location, you will probably not see any facilities locally until more data is added.

The facilities that are in the database do exist and their addresses are correct, and the procedures and their CPT codes are accurate as of May 2017.

The prices for the procedures in our database are completely made up and are meant only as placeholders. They are not accurate estimates.

### Technologies

As this mockup was created for Alvin Health, the headers and footers are theirs. Almost all of the CSS and HTML are from their site. The bulk of this project was written with Python and vanilla Javascript.

Google Maps API was used for the display.

PostgreSQL stores the data.

The web app is served on Digital Ocean using Ubuntu and Apache.



