import requests
import datetime
class ServicenowNotifier:

    def __init__(self, config):
        self.__config = config 
        self.__base_url = "https://" + self.__config["instance"] + ".service-now.com/api/now/table"
        self.__headers = {"Content-Type":"application/json","Accept":"application/json"}

    def __do_get_request(self, path, params = {}):
        response = requests.get(self.__base_url + "/" + path, auth=(self.__config['username'], self.__config['password']), headers=self.__headers, params = params)
        data = response.json()
        return data
    
    def __do_post_request(self, path, params = {}):
        response = requests.post(self.__base_url + "/" + path, auth=(self.__config['username'], self.__config['password']), headers=self.__headers, json = params)
        data = response.json()
        return data

    def __do_put_request(self, path, params = {}):
        response = requests.put(self.__base_url + "/" + path, auth=(self.__config['username'], self.__config['password']), headers=self.__headers, json = params)
        return response

    def __create_ticket(self, notification, user, assignment_group):
        params = {
            'assignment_group': assignment_group,
            'caller_id': self.__config['caller_id'],
            'contact_type': self.__config['contact_type'],
            'assigned_to': user,
            'short_description': notification.serviceid + ": Monitoring alert",
            'description': "The check " + notification.check + " currently has a problem with message: " + notification.output,
            'cmdb_ci': notification.serviceid
        }
        response = self.__do_post_request('incident', params)
        return response

    def __update_ticket(self, ticket, notification, assignment_group):
        params = {
          'work_notes': "The check " + notification.check + " currently has a problem with message: " + notification.output,
          'assignment_group': assignment_group
        }
        sn = self.__do_put_request('incident/' + ticket, params)

    def __find_ticket(self, subject):
        params = {
            'short_description': subject,
            'sysparm_query': 'state<=5^ORDERBYDESCsys_updated_on'
        }
        sn = self.__do_get_request('incident', params)
        if len(sn['result']) != 0:
            ticket = sn['result'][0]
            last_updated = datetime.datetime.strptime(ticket['sys_updated_on'], '%Y-%m-%d %H:%M:%S')
            date_month_ago = datetime.datetime.now() - datetime.timedelta(days=30)
            if last_updated < date_month_ago:
                return None
            else:
                return ticket
        else:
            return None 

      
    def notify(self, notification):
        fout = open("/tmp/file_out.txt", "a")
        fout.write(pprint.pformat(notification))
        ticket = self.__find_ticket(notification.serviceid + ": Monitoring alert")
        if ticket is None:
            ticket = self.__create_ticket(notification,  notification.user_to_notify.email, notification.user_to_notify.profile.servicenow_assignment_group)
        else:
            ticket = self.__update_ticket(ticket['sys_id'], notification, notification.user_to_notify.profile.servicenow_assignment_group)
