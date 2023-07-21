from odoo import http

class Motorcycle(http.Controller):
    @http.route('/compare/', auth='public', website=True)
    def index(self,**kw):
        motorcycles=http.request.env['product.template'].search([('detailed_type','=','motorcycle')])
        return http.request.render('motorcycles.compare_website',{'motorcycles':motorcycles,})