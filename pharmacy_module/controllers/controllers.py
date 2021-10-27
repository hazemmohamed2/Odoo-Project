# -*- coding: utf-8 -*-
# from odoo import http


# class PharmacyModule(http.Controller):
#     @http.route('/pharmacy_module/pharmacy_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pharmacy_module/pharmacy_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pharmacy_module.listing', {
#             'root': '/pharmacy_module/pharmacy_module',
#             'objects': http.request.env['pharmacy_module.pharmacy_module'].search([]),
#         })

#     @http.route('/pharmacy_module/pharmacy_module/objects/<model("pharmacy_module.pharmacy_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pharmacy_module.object', {
#             'object': obj
#         })
