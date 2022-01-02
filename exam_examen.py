from openerp.osv import osv, fields
import openerp


class exam_examen(osv.osv):
	def _futur_func(self, cr, uid, ids):
		self.write(cr, uid, ids, {'state': 'futur'})
		return True

	def _present_func(self, cr, uid, ids):
		self.write(cr, uid, ids, {'state': 'present'})
		return True
		
	def _past_func(self, cr, uid, ids):
		self.write(cr, uid, ids, {'state': 'past'})
		return True
		
    
		
	_name='exam.examen'
	_columns={
        'name':fields.char('Id',size=255),
		'date':fields.date('Date'),
		'heure_debut':fields.char('Heure debut'),
        'duree':fields.float('Duree',digits=None),
		''''''
		'salle_id': fields.many2one('exam.salle','Salle',ondelete='cascade'),
		'filliere_id': fields.many2one('exam.filliere','Filiere',ondelete='cascade'),
		'semestre_id': fields.many2one('exam.semestre','Semestre',ondelete='cascade'),
		'module_id': fields.many2one('exam.module','Module',ondelete='cascade'),
		'element_id': fields.many2one('exam.element','Element',ondelete='cascade'),
		'session_id': fields.many2one('exam.session','Session',ondelete='cascade'),
		'surveillant_id': fields.many2one('exam.surveillant','Surveillant',ondelete='cascade'),
		'anneeuniv_id': fields.many2one('exam.annee','Annee',ondelete='cascade'),
		'state': fields.selection([
			('futur','Examen Programme'),
			('present','Examen en Cours'),
			('past','Examen Passe')
		], 'State',readonly=True)
			 }
exam_examen()
