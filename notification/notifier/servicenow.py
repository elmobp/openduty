import requests

class ServicenowNotifier:

    def __init__(self, config):
        self.__config = config 
        self.__base_url = "https://" + __config["instance"] + "/api/now/table"
    
    def __do_get_request(self, path, params = {}):
        headers = {"Content-Type":"application/json","Accept":"application/json"}
        response = requests.get(base_url + "/" + path, auth=(__config['username'], __config['password']), headers=headers, params = params)
        data = response.json()
        return data
    
    def __do_post_request(self, path, params = {}):
        headers = {"Content-Type":"application/json","Accept":"application/json"}
        response = requests.post(base_url + "/" + path, auth=(__config['username'], __config['password']), headers=headers, params = params)
        data = response.json()
        return data

    def __do_put_request(self, path, params = {}):
        headers = {"Content-Type":"application/json","Accept":"application/json"}
        response = requests.put(base_url + "/" + path, auth=(__config['username'], __config['password']), headers=headers, params = params)
        data = response.json()
        return data

    def __create_ticket(self, bs_serviceid, cmdb_ci):
        params = {}
        sn = self.__do_post_request('incident', params)
    
    def __update_ticket(self, ticket, notes):
        params = {}
        sn = self.__do_put_request('incident', params)

    def __find_ticket(self, subject):
        params = {}
        sn = self.__do_get_request('incident', params)
      
    def notify(self, notification):
        ticket = self.__find_ticket(notification.message)
        if ticket is None:
            ticket = self.__create_ticket('somethihg', 'somehting')
        else:
            ticket = self.__update_ticket(ticket.id, notification.message)