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
 * The entire data set.
 ```
<EPOCH>2023-048T12:20:00.000Z</EPOCH>
                        <X units="km">-5063.01655412946</X>
                        <Y units="km">-3888.6472910294901</Y>
                        <Z units="km">2302.9065286659102</Z>
                        <X_DOT units="km/s">4.6388138749528096</X_DOT>
                        <Y_DOT units="km/s">-2.8228432495973399</Y_DOT>
                        <Z_DOT units="km/s">5.4174928915010803</Z_DOT>
```
* A list of all Epochs in the data set.
```
<EPOCH>2023-048T14:16:00.000Z</EPOCH>
<EPOCH>2023-048T14:20:00.000Z</EPOCH>
```
* State vectors for a specific Epoch from the data set.
```
<X units="km">4088.6810739994698</X>
<Y units="km">-2531.86624046617</Y>
<Z units="km">4794.4381789315503</Z>
```
* Instantaneous speed for a specific Epoch in the data set.
```
<X_DOT units="km/s">5.7520747044379101</X_DOT>
<Y_DOT units="km/s">4.3451316656044199</Y_DOT>
<Z_DOT units="km/s">-2.59528004498392</Z_DOT>

```



