# Kryptin

### Prerequisites
* Install Python
* Install Python Package Manager (pip/pip3) :
    ```
    apt-get install python-pip
    ```
    ```
    apt-get install python3-pip
    ```
* Install [virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b) :
    ```
    apt-get install virtualenv
    ```
* Install [`mysqlclient`](https://pypi.org/project/mysqlclient/) prerequisites :
    * You may need to install the Python and MySQL development headers and libraries like so:
        ```
        sudo apt-get install python-dev default-libmysqlclient-dev
        ```
    * If you are using python3 then you need to install python3-dev using the following command :
        ```
        sudo apt-get install python3-dev
        ```
    * Install from PyPI:
        ```
        pip3 install mysqlclient
        ```

### Project Installation

1. Clone the repository - `git clone <remote-url>`
2. Go to the project directory - `cd <cloned-repo>`
3. Set up the environment :
    * Create virtual environment files - `virtualenv venv`
    * Activate virtual environment - `source venv/bin/activate`
4. Install dependencies - `pip3 install -r requirements.txt`
5. Create a MySQL database connection configuration file - `cp db.cnf.example db.cnf`
6. Enter your MySQL credentials in `db.cnf`:
    * Set `user` and `password` to your localhost MySQL credentials.
    * Create a database `kryptin_api`
    * Set `database = 'kryptin_api'`
7. Run migrations - `python3 manage.py migrate`
8. Run seeders - `python3 manage.py loaddata */fixtures/*.json`
9. Start server - `python3 manage.py runserver`

#### Note
* Everytime you install packages or run the server, activate your virtual environment - `source venv/bin/activate`
* To deactivate the activated virtual environment - run the command `deactivate` in terminal.
* If you ran into any errors while running the server with python version incompatabilities, try `python3` instead of `python` while running the server.
* If you install any python packages, please update the file `requirements.txt`
