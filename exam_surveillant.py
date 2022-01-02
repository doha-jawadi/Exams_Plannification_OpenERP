from openerp.osv import osv,fields
import openerp
class exam_surveillant(osv.osv):
    _name='exam.surveillant'
    _columns={
		'name': fields.char('Nom Surveillant', size=64),
		'prenom': fields.char('Prenom Surveillant'),
        'salle': fields.many2one('exam.salle','Sale',ondelete='cascade'),
        'date': fields.date('Date'),
        'heure_debut': fields.char('Heure de debut'),
        'duree': fields.float('Duree',digits=None),
			 }
exam_surveillant()