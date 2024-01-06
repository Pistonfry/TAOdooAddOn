from odoo import http
from odoo.http import request

class MyController(http.Controller):
    @http.route('/my_module/my_controller/', auth='public', website=True)
    def index(self, **kw):
        # Your controller logic goes here
        return "Hello, World!"  