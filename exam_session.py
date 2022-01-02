from openerp.osv import osv,fields
import openerp
class exam_session(osv.osv):
    _name='exam.session'
    _columns={
		'name': fields.char('Session'),
			 }
exam_session()