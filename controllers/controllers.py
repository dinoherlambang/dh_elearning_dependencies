# -*- coding: utf-8 -*-
# from odoo import http


# class DhElearningDependencies(http.Controller):
#     @http.route('/dh_elearning_dependencies/dh_elearning_dependencies', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dh_elearning_dependencies/dh_elearning_dependencies/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dh_elearning_dependencies.listing', {
#             'root': '/dh_elearning_dependencies/dh_elearning_dependencies',
#             'objects': http.request.env['dh_elearning_dependencies.dh_elearning_dependencies'].search([]),
#         })

#     @http.route('/dh_elearning_dependencies/dh_elearning_dependencies/objects/<model("dh_elearning_dependencies.dh_elearning_dependencies"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dh_elearning_dependencies.object', {
#             'object': obj
#         })
