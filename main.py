# -*- coding: utf-8 -*-
#!/usr/bin/env python
import webapp2
from BasicHandlers import MainHandler, DodajHandler, DodanoHandler, TableHandler, TableDelete
from Pregled2015Handler import L2015Handler, Januar15Handler, Februar15Handler, Marec15Handler, April15Handler, Maj15Handler,\
    Junij15Handler, Julij15Handler, Avgust15Handler, September15Handler, Oktober15Handler, November15Handler,\
    December15Handler


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/dodaj', DodajHandler),
    webapp2.Route('/dodano', DodanoHandler),
    webapp2.Route('/table/<table_id:\d+>', TableHandler),
    webapp2.Route('/table/<table_id:\d+>/delete', TableDelete),
    webapp2.Route('/l2015', L2015Handler,  name="pregled"),
    webapp2.Route('/januar15', Januar15Handler),
    webapp2.Route('/februar15', Februar15Handler),
    webapp2.Route('/marec15', Marec15Handler),
    webapp2.Route('/april15', April15Handler),
    webapp2.Route('/maj15', Maj15Handler),
    webapp2.Route('/junij15', Junij15Handler),
    webapp2.Route('/julij15', Julij15Handler),
    webapp2.Route('/avgust15', Avgust15Handler),
    webapp2.Route('/september15', September15Handler),
    webapp2.Route('/oktober15', Oktober15Handler),
    webapp2.Route('/november15', November15Handler),
    webapp2.Route('/december15', December15Handler),
], debug=True)
