from twisted.web.server import Site, NOT_DONE_YET
from twisted.web.resource import Resource

class TornadoSite(Site):

    def __init__(self, application):
        self.application = application

    def getResourceFor(self, request):
        app = self.application
        class AdaptedResource(Resource):
            def render(self, req):
                app(request)
                return NOT_DONE_YET
        return AdaptedResource()

