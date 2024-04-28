from server.server_restrictions_information import get_restrictions_information_server
data = get_restrictions_information_server().json()
print(data["id"])