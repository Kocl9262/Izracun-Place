# -*- coding: utf-8 -*-
#!/usr/bin/env python
import webapp2
from BasicHandlers import MainHandler, DodajHandler, DodanoHandler, TableHandler, TableDelete
from Pregled2015Handler import L2015Handler, Januar15Handler, Februar15Handler, Marec15Handler, April15Handler,\
    Maj15Handler, Junij15Handler, Julij15Handler, Avgust15Handler, September15Handler, Oktober15Handler,\
    November15Handler, December15Handler
from Pregled2016Handler import L2016Handler, Januar16Handler, Februar16Handler, Marec16Handler, April16Handler,\
    Maj16Handler, Junij16Handler, Julij16Handler, Avgust16Handler, September16Handler, Oktober16Handler,\
    November16Handler, December16Handler
from AdminHandlers import AdminHandler, SporociloOddano, KontaktHandler, MessageHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/dodaj', DodajHandler),
    webapp2.Route('/dodano', DodanoHandler),
    webapp2.Route('/table/<table_id:\d+>', TableHandler),
    webapp2.Route('/table/<table_id:\d+>/delete', TableDelete),
    webapp2.Route('/l2015', L2015Handler,  name="pregled15"),
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
    webapp2.Route('/l2016', L2016Handler,  name="pregled16"),
    webapp2.Route('/januar16', Januar16Handler),
    webapp2.Route('/februar16', Februar16Handler),
    webapp2.Route('/marec16', Marec16Handler),
    webapp2.Route('/april16', April16Handler),
    webapp2.Route('/maj16', Maj16Handler),
    webapp2.Route('/junij16', Junij16Handler),
    webapp2.Route('/julij16', Julij16Handler),
    webapp2.Route('/avgust16', Avgust16Handler),
    webapp2.Route('/september16', September16Handler),
    webapp2.Route('/oktober16', Oktober16Handler),
    webapp2.Route('/november16', November16Handler),
    webapp2.Route('/december16', December16Handler),
    webapp2.Route('/admin', AdminHandler),
    webapp2.Route('/poslano', SporociloOddano),
    webapp2.Route('/kontakt', KontaktHandler),
    webapp2.Route('/msg/<msg_id:\d+>', MessageHandler),
], debug=True)
