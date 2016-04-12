# -*- coding: utf-8 -*-
from openerp import http

# class ManaratSchool(http.Controller):
#     @http.route('/manarat_school/manarat_school/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manarat_school/manarat_school/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('manarat_school.listing', {
#             'root': '/manarat_school/manarat_school',
#             'objects': http.request.env['manarat_school.manarat_school'].search([]),
#         })

#     @http.route('/manarat_school/manarat_school/objects/<model("manarat_school.manarat_school"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manarat_school.object', {
#             'object': obj
#         })