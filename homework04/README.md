Buddy Flask
=

* This project is for COE332 homework 04.

* This is a Flask application for querying the ISS position and velocity

Installation
--
Install this application by cloning the repository, making the scripts executable, and adding them to your PATH. For example:

```
git clone ...
chmod ...
...
...

etc
```
Access the data set
--

* Navigate to the ISS Trajectory Data website from this link (https://spotthestation.nasa.gov/trajectory_data.cfm)
* There are two downloads available, and they contain the same data.
*  It is the ‘Orbital Ephemeris Message (OEM)’ data in either plain text or XML format. 


Running the Code
--
* part2
   * You can use this application to load in the data from the link above, and expose that data to an end user with carefully crafted routes.
    
   * A function to return the entire data set, for example:
   
    ```
  @app.route('/')
  def data_set():
     """
    Return the entire data set
    :return: the entire data set
     """
    return dic
    ```
   
 Sample output
 --
 * The entire data set
 ```

```
* A list of all Epochs in the data set
* State vectors for a specific Epoch from the data set
* Instantaneous speed for a specific Epoch in the data set (math required!)



