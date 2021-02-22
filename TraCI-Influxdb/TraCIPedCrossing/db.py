from influxdb import InfluxDBClient

class DB:

    def __init__(self):
        host = "localhost"
        port = 8086
        user = 'root'
        password = 'root'
        self.dbname = 'sumo'
        self.dbuser = 'eclipse-sumo'
        self.dbuser_password = 'eclipse-sumo-pwd'

        self.client = InfluxDBClient(host, port, user, password, self.dbname)

        

    def initialize_db(self, retention_policy='3d'):
        '''
        Method to initialize the InfluxDB "sumo" database and "pedestrian" table
        '''
        print("Create database: " + self.dbname)
        self.client.create_database(self.dbname)

        print("Create a retention policy")
        self.client.create_retention_policy('my_policy', retention_policy, 3, default=True)

        print("Switch user: " + self.dbuser)
        self.client.switch_user(self.dbuser, self.dbuser_password)

    def write(self, point):
        '''
        Method to write on the InfluxDB "sumo" database
        '''
        print("Write points: {0}".format(point))
        self.client.write_points(point)

    def query(self, query, bind_params=None):
        '''
        Method to write on the InfluxDB "sumo" database
        '''
        print("Querying data: " + query)
        result = self.client.query(query, bind_params=bind_params)

        print("Result: {0}".format(result))
        return result
