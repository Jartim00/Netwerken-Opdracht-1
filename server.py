from twisted.web import server, resource
from twisted.internet import reactor

class SimpleWebserver(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html>Hello, world!</html>"

if __name__ == '__main__':    
    print "######################## MENU #################################"
    print "Select the mount of clients you'd like."
    print "######################## INTERMISSION #########################"
    inputnumber = input('select number: ')
    print "---------------------------------------------------------------"
    site = server.Site(SimpleWebserver())
    if inputnumber > 0:
        inputnumber = 8000+inputnumber
        for s in range(8000,inputnumber):
            print "Starting server on: http://localhost:" + str(s)
            reactor.listenTCP(s, site)
        print "---------------------------------------------------------------"
        print "######################## END ##################################"
        reactor.run()
    else:
        print "Wrong input, please try again"
