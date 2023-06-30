import connexion
import sys
import functions


sys.path.insert(0, '')

server = connexion.App(__name__, options= {"swagger_ui" : True } )
resolver = connexion.RestyResolver("functions") 

server.add_api("api.json", base_path="/tokio/1.0", resolver=resolver)

if __name__ == "__main__":
    server.run(port=5005, debug=True)
    exit(0)