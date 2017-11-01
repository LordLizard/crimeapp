class MockDBHelper():
    def connect(self, database="crimemap"):
        pass

    def add_crime(self, category, date, latitude, longitude, description):
        pass

    def get_all_crimes(self):
        return [{
            'latitude': 28.30436053157074,
            'longitude': -81.41624450683594,
            'date': '2017-10-31',
            'category': 'Asalto',
            'description': 'Este es un asalto de prueba'
            }]

    def clear_all(self):
        pass
