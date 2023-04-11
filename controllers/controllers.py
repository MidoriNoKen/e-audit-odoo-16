# -*- coding: utf-8 -*-
# from odoo import http


# class Eaudit(http.Controller):
#     @http.route('/eaudit/eaudit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eaudit/eaudit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('eaudit.listing', {
#             'root': '/eaudit/eaudit',
#             'objects': http.request.env['eaudit.eaudit'].search([]),
#         })

#     @http.route('/eaudit/eaudit/objects/<model("eaudit.eaudit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eaudit.object', {
#             'object': obj
#         })
