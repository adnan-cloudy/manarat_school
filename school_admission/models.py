# -*- coding: utf-8 -*-

from openerp import models, fields, api


from openerp import tools
from openerp.tools.translate import _
from openerp.exceptions import Warning
#from openerp.tools import email_re, email_split

# class manarat_school(models.Model):
#	 _name = 'manarat_school.manarat_school'

#	 name = fields.Char()

LANGUAGS = [("arabic","Arabic"),("english","English"),("french","French"),("german","German")]
GENDER = [("male","Male"),("female","Female")]
RELIGION = [("muslim","Muslim"),("christian","Christian")]
LIVE_STATUS = [("alive","Alive"),("dead","Dead")]
ID_TYPYE = [("passport","Passport"),("national id","National ID")]
RELATIONSHIP = [("mother","Mother"),("brother","Brother"),("sister","Sister"),("grandfather","Grandfather"),
	("grandmother","Grandmother"),("aunts","Aunts"),("uncle","Uncle"),("coisen","Coisen"),("other","Other")]
REGISTERATION_TYPE = [("passed","Passed"),("new","New"),("none","None")]
BUS_STATUS = [("going and come back","Going and come back"),("going","Going"),("back","Back")]

STASTE = [('new','New'),('spot_checked','Spot checked'),('data_completed','Data Completed'),
('confirm_fees','Fees payment confirmed'),('pass_assessment','Pass Assessment'),('installment_complete','Documents complete'),
('invoice_paid','Invoice paid'),('added_to_class_list','Added to class list')]

	
class AdmetionInfo:
	#father info
	father_full_name = fields.Char(string="Full Name")
	father_nationality = fields.Many2one("res.country", string="Nationality")
	father_religion =  fields.Selection(RELIGION, string="Religion")
	father_acadimic = fields.Char(string="Academic Qualification")
	father_mob_no = fields.Char(string="Mobile Number")
	father_mob_no2 = fields.Char(string="Mobile Number 2")
	father_home_address = fields.Char(string="Home Address")
	father_home_tel = fields.Char(string="Home Telephone")
	father_job = fields.Char(string="Job")
	father_employer_address = fields.Char(string="Current Employer Address")
	father_occupation_phone = fields.Char(string="Curent Occupation Phone")
	father_status =  fields.Selection(LIVE_STATUS, string="Status")
	father_id_type = fields.Selection(ID_TYPYE, string="ID Type")
	father_id_no = fields.Char(string="ID Number")
	father_email = fields.Char(string="Email") 
	
	#education info
	student_id = fields.Char(string="Student ID")
	student_mother_tongue = fields.Selection(LANGUAGS, string="Mother Tongue")
	student_first_foreign_language = fields.Selection(LANGUAGS, string="First Foregin Language")
	student_second_foreign_language = fields.Selection(LANGUAGS, string="Second Foreign Language")
	
	#student personal info
	student_first_name = fields.Char(string="First Name")
	student_middle_name = fields.Char(string="Middle Name")
	student_surname = fields.Char(string="Surname")
	student_arabic_full_name = fields.Char(string="Arabic Full Name")
	student_birth_date = fields.Date(string="Birth Date")
	student_place_of_birth = fields.Char(string="Place Of Birth")
	student_gender = fields.Selection(GENDER, string="Gender")
	student_nationality = fields.Many2one("res.country", string="Nationality")
	student_religion = fields.Selection(RELIGION, string="Religion")
	student_national_id = fields.Char(string="National ID")
	student_birth_certificate_no = fields.Char(string="Birth Certificate Number")
	student_issue_date = fields.Date(string="Date Of Issue")
	
	#mother info
	mother_full_name = fields.Char(string="Full Name")
	mother_nationality = fields.Many2one("res.country", string="Nationality")
	mother_religion =  fields.Selection(RELIGION, string="Religion")
	mother_acadimic = fields.Char(string="Academic Qualification")
	mother_mob_no = fields.Char(string="Mobile Number")
	mother_mob_no2 = fields.Char(string="Mobile Number 2")
	mother_home_address = fields.Char(string="Home Address")
	mother_home_tel = fields.Char(string="Home Telephone")
	mother_job = fields.Char(string="Job")
	mother_employer_address = fields.Char(string="Current Employer Address")
	mother_occupation_phone = fields.Char(string="Curent Occupation Phone")
	mother_status =  fields.Selection(LIVE_STATUS, string="Status")
	mother_id_type = fields.Selection(ID_TYPYE, string="ID Type")
	mother_id_no = fields.Char(string="ID Number")
	mother_email = fields.Char(string="Email")
	
	#gardian info
	first_guardian = fields.Boolean(string="First Guardian")
	fg_relationship = fields.Selection(RELATIONSHIP, string="Guardian Relationship With Student")
	fg_full_name = fields.Char(string="Guardian Full Name")
	fg_relative = fields.Char(string="Guardian Relative")
	fg_job = fields.Char(string="Guardian Job")
	fg_address = fields.Char(string="Guardian Home Address")
	fg_tel = fields.Char(string="Guardian Home Telephone")
	fg_mob = fields.Char(string="Guardian Mobile Phone")
	fg_work_tel = fields.Char(string="Guardian Work Telephone")
	
	second_guardian = fields.Boolean(string="Second Guardian")
	sg_relationship = fields.Selection(RELATIONSHIP, string="Guardian Relationship With Student")
	sg_full_name = fields.Char(string="Guardian Full Name")
	sg_relative = fields.Char(string="Guardian Relative")
	sg_job = fields.Char(string="Guardian Job")
	sg_address = fields.Char(string="Guardian Home Address")
	sg_tel = fields.Char(string="Guardian Home Telephone")
	sg_mob = fields.Char(string="Guardian Mobile Phone")
	sg_work_tel = fields.Char(string="Guardian Work Telephone")
	
	#enrollment data
	applicant_date = fields.Date(string="Applicant Date")
	registeration_date = fields.Date(string="Registeration Date")
	registeration_type = fields.Selection(REGISTERATION_TYPE, string="Student Registeration Type")
	grade_level = fields.Char(string="Grade Level")
	student_grade = fields.Many2one(comodel_name='product.product',string="Student Grade")
	join_bus = fields.Boolean(string="Join Bus")
	bus_status = fields.Selection(BUS_STATUS,string="Bus Status")
	bus_route = fields.Many2one(comodel_name='product.product',string="Bus Route")
	enrollment_date = fields.Date(string="Enrollement Date")
	id_code = fields.Char(string="Identification Code")
	left_date = fields.Date(string="Student Left Date")
	prev_school = fields.Char(string="Student Previous School")
	reason_of_transfer = fields.Text(string="Reason For Transfer")
	
	#health_info
	health_info = fields.Text(string="Health Information")
	
	
	
	

class CrmLead(models.Model, AdmetionInfo):
	_inherit = "crm.lead"
	
	state = fields.Selection(STASTE,default='new')
	level = fields.Many2one('manarat.level', string='Level')
	wait_list = fields.Boolean(string='Waiting List')
	tester_aprove = fields.Boolean(string='Teacher approval')
	pr_aprove = fields.Boolean(string='PR approval')
	principle_aprove = fields.Boolean(string='Principle approval')
	in_draft =  fields.Boolean(string='In draft')
	documents = fields.One2many('manarat.document','lead_id_rel',string='Documents')
	
	
	def check_available_spots(self, cr, uid, ids, context=None):
		for lead in self.browse(cr, uid, ids, context=context):
			spots = lead.level.available_spots
			if(spots <= 0 ):
				self.write(cr, uid, ids, {'wait_list': True}, context=context)
				#self.send_mail_without_pop(cr, uid, ids, context=context)
				#raise Warning( _( 'no available spots, admission added to waiting list' ) )
			else:
				self.write(cr, uid, ids, {'state': 'spot_checked'}, context=context)
				# level_model = self.pool.get('manarat.level')
				# level_id = level_model.search(cr, uid, [('id', '=',mail_obj_id)])[0]
				lead.level.write({'available_spots': spots - 1})
		
	
	def check_data_completed(self, cr, uid, ids, context=None):
		self.write(cr, uid, ids, {'state': 'data_completed'}, context=context)
		
	def check_fees_payment(self, cr, uid, ids, context=None):
		self.write(cr, uid, ids, {'state': 'confirm_fees'}, context=context)
		
	def check_pass_assessment(self, cr, uid, ids, context=None):
		self.write(cr, uid, ids, {'state': 'pass_assessment'}, context=context)
		
	def check_installment_complete(self, cr, uid, ids, context=None):
		self.write(cr, uid, ids, {'state': 'installment_complete'}, context=context)
		
	def check_invoice_paid(self, cr, uid, ids, context=None):
		self.write(cr, uid, ids, {'state': 'invoice_paid'}, context=context)
	
		
	def check_add_to_class_list(self, cr, uid, ids, context=None):
		#documents
		#for doc in lead.documents:
		#	doc.write({'partner_id_rel':lead.partner_id.id})
		#lead.partner_id.write({'documents': [x.id for x in lead.documents]})
		
		for lead in self.browse(cr, uid, ids, context=context):
			self.pool['res.partner'].write(cr, uid, lead.partner_id.id, {'lead' : False,'customer' : True})
			self.pool['res.partner'].write(cr, uid, lead.partner_id.parent_id.id, {'lead' : False,'customer' : True})
			
			#for doc in lead.documents:
			#	self.pool['manarat.document'].write(cr, uid, doc,{'partner_id_rel':lead.partner_id.id})
			#self.pool['res.partner'].write(cr, uid, lead.partner_id.id, {'documents': [x for x in lead.documents]})
			
		self.write(cr, uid, ids, {'state': 'added_to_class_list'}, context=context)
		
		
		
	def add_to_wait_list(self, cr, uid, ids, context=None):
		self.write(cr, uid, ids, {'wait_list': True,'in_draft' : False}, context=context)
		
	
	def return_to_admession_process(self, cr, uid, ids, context=None):
		self.write(cr, uid, ids, {'wait_list': False,'in_draft' : False}, context=context)
		
	def reject(self, cr, uid, ids, context=None):
		self.write(cr, uid, ids, {'wait_list': False,'in_draft' : True}, context=context)
		
	
	
	def _lead_create_contact(self, cr, uid, lead, name, is_company, parent_id=False, context=None):
		partner = self.pool.get('res.partner')
		vals = {'name': name,
			'user_id': lead.user_id.id,
			'comment': lead.description,
			'section_id': lead.section_id.id or False,
			'parent_id': parent_id,
			'phone': lead.phone,
			'mobile': lead.mobile,
			'email': tools.email_split(lead.email_from) and tools.email_split(lead.email_from)[0] or False,
			'fax': lead.fax,
			'title': lead.title and lead.title.id or False,
			'function': lead.function,
			'street': lead.street,
			'street2': lead.street2,
			'zip': lead.zip,
			'city': lead.city,
			'country_id': lead.country_id and lead.country_id.id or False,
			'state_id': lead.state_id and lead.state_id.id or False,
			'is_company': is_company,
			'type': 'contact',
			#Student Educational information
			'student_id': lead.student_id,
			'student_mother_tongue': lead.student_mother_tongue,
			'student_first_foreign_language': lead.student_first_foreign_language,
			'student_second_foreign_language': lead.student_second_foreign_language,
			#student personal inforamtion
			'student_first_name': lead.student_first_name,
			'student_middle_name': lead.student_middle_name,
			'student_surname': lead.student_surname,
			'student_arabic_full_name': lead.student_arabic_full_name,
			'student_birth_date': lead.student_birth_date,
			'student_place_of_birth': lead.student_place_of_birth,
			'student_gender': lead.student_gender,
			'student_nationality': lead.student_nationality.id,
			'student_religion': lead.student_religion,
			'student_national_id': lead.student_national_id,
			'student_birth_certificate_no': lead.student_birth_certificate_no,
			'student_issue_date': lead.student_issue_date,
			#father inforamtion
			'father_full_name': lead.father_full_name,
			'father_nationality': lead.father_nationality.id,
			'father_religion': lead.father_religion,
			'father_acadimic': lead.father_acadimic,
			'father_mob_no': lead.father_mob_no,
			'father_mob_no2': lead.father_mob_no2,
			'father_email': lead.father_email,
			'father_home_address': lead.father_home_address,
			'father_home_tel': lead.father_home_tel,
			'father_job': lead.father_job,
			'father_employer_address': lead.father_employer_address,
			'father_occupation_phone': lead.father_occupation_phone,
			'father_status': lead.father_status,
			'father_id_type': lead.father_id_type,
			'father_id_no': lead.father_id_no,
			#mother inforamtion
			'mother_full_name': lead.mother_full_name,
			'mother_nationality': lead.mother_nationality.id,
			'mother_religion': lead.mother_religion,
			'mother_acadimic': lead.mother_acadimic,
			'mother_mob_no': lead.mother_mob_no,
			'mother_mob_no2': lead.mother_mob_no2,
			'mother_email': lead.mother_email,
			'mother_home_address': lead.mother_home_address,
			'mother_home_tel': lead.mother_home_tel,
			'mother_job': lead.mother_job,
			'mother_employer_address': lead.mother_employer_address,
			'mother_occupation_phone': lead.mother_occupation_phone,
			'mother_status': lead.mother_status,
			'mother_id_type': lead.mother_id_type,
			'mother_id_no': lead.mother_id_no,
			#gardian details
			'first_guardian': lead.first_guardian,
			'fg_full_name': lead.fg_full_name,
			'fg_relationship': lead.fg_relationship,
			'fg_relative': lead.fg_relative,
			'fg_job': lead.fg_job,
			'fg_address': lead.fg_address,
			'fg_tel': lead.fg_tel,
			'fg_mob': lead.fg_mob,
			'fg_work_tel': lead.fg_work_tel,
			'second_guardian': lead.second_guardian,
			'sg_full_name': lead.sg_full_name,
			'sg_relationship': lead.sg_relationship,
			'sg_relative': lead.sg_relative,
			'sg_job': lead.sg_job,
			'sg_address': lead.sg_address,
			'sg_tel': lead.sg_tel,
			'sg_mob': lead.sg_mob,
			'sg_work_tel': lead.sg_work_tel,
			#enrollment data
			'applicant_date': lead.applicant_date,
			'registeration_date': lead.registeration_date,
			'registeration_type': lead.registeration_type,
			'grade_level': lead.grade_level,
			'student_grade': lead.student_grade.id,
			'join_bus': lead.join_bus,
			'bus_status': lead.bus_status,
			'bus_route': lead.bus_route.id,
			'enrollment_date': lead.enrollment_date,
			'id_code': lead.id_code,
			'left_date': lead.left_date,
			'prev_school': lead.prev_school,
			'reason_of_transfer': lead.reason_of_transfer,
			#health info
			'health_info': lead.health_info,
			#make them as lead
			'lead' : True,
			'customer' : False,
			'parent' : context['parent'],
			'student' : context['student']
			
		}
		
		partner = partner.create(cr, uid, vals, context=context)
		
		return partner

		
	def on_change_partner_id(self, cr, uid, ids, partner_id, context=None):
		values = {}
		if partner_id:
			partner = self.pool.get('res.partner').browse(cr, uid, partner_id, context=context)
			partner_name = partner.name#(partner.parent_id and partner.parent_id.name) or (partner.is_company and partner.name) or False
			values = {
				#'partner_name': partner_name,
				'contact_name': partner_name,#(not partner.is_company and partner.name) or False,
				'title': partner.title and partner.title.id or False,
				'street': partner.street,
				'street2': partner.street2,
				'city': partner.city,
				'state_id': partner.state_id and partner.state_id.id or False,
				'country_id': partner.country_id and partner.country_id.id or False,
				'email_from': partner.email,
				'phone': partner.phone,
				'mobile': partner.mobile,
				'fax': partner.fax,
				'zip': partner.zip,
				'function': partner.function,
				'father_full_name': partner.father_full_name,
				'student_id': partner.student_id,
				'student_mother_tongue': partner.student_mother_tongue,
				'student_first_foreign_language': partner.student_first_foreign_language,
				'student_second_foreign_language': partner.student_second_foreign_language,
				'father_religion': partner.father_religion,
				#Student Educational information
				'student_id': partner.student_id,
				'student_mother_tongue': partner.student_mother_tongue,
				'student_first_foreign_language': partner.student_first_foreign_language,
				'student_second_foreign_language': partner.student_second_foreign_language,
				#student personal inforamtion
				'student_first_name': partner.student_first_name,
				'student_middle_name': partner.student_middle_name,
				'student_surname': partner.student_surname,
				'student_arabic_full_name': partner.student_arabic_full_name,
				'student_birth_date': partner.student_birth_date,
				'student_place_of_birth': partner.student_place_of_birth,
				'student_gender': partner.student_gender,
				'student_nationality': partner.student_nationality.id,
				'student_religion': partner.student_religion,
				'student_national_id': partner.student_national_id,
				'student_birth_certificate_no': partner.student_birth_certificate_no,
				'student_issue_date': partner.student_issue_date,
				#father inforamtion
				'father_full_name': partner.father_full_name,
				'father_nationality': partner.father_nationality.id,
				'father_religion': partner.father_religion,
				'father_acadimic': partner.father_acadimic,
				'father_mob_no': partner.father_mob_no,
				'father_mob_no2': partner.father_mob_no2,
				'father_email': partner.father_email,
				'father_home_address': partner.father_home_address,
				'father_home_tel': partner.father_home_tel,
				'father_job': partner.father_job,
				'father_employer_address': partner.father_employer_address,
				'father_occupation_phone': partner.father_occupation_phone,
				'father_status': partner.father_status,
				'father_id_type': partner.father_id_type,
				'father_id_no': partner.father_id_no,
				#mother inforamtion
				'mother_full_name': partner.mother_full_name,
				'mother_nationality': partner.mother_nationality.id,
				'mother_religion': partner.mother_religion,
				'mother_acadimic': partner.mother_acadimic,
				'mother_mob_no': partner.mother_mob_no,
				'mother_mob_no2': partner.mother_mob_no2,
				'mother_email': partner.mother_email,
				'mother_home_address': partner.mother_home_address,
				'mother_home_tel': partner.mother_home_tel,
				'mother_job': partner.mother_job,
				'mother_employer_address': partner.mother_employer_address,
				'mother_occupation_phone': partner.mother_occupation_phone,
				'mother_status': partner.mother_status,
				'mother_id_type': partner.mother_id_type,
				'mother_id_no': partner.mother_id_no,
				#gardian details
				'first_guardian': partner.first_guardian,
				'fg_full_name': partner.fg_full_name,
				'fg_relationship': partner.fg_relationship,
				'fg_relative': partner.fg_relative,
				'fg_job': partner.fg_job,
				'fg_address': partner.fg_address,
				'fg_tel': partner.fg_tel,
				'fg_mob': partner.fg_mob,
				'fg_work_tel': partner.fg_work_tel,
				'second_guardian': partner.second_guardian,
				'sg_full_name': partner.sg_full_name,
				'sg_relationship': partner.sg_relationship,
				'sg_relative': partner.sg_relative,
				'sg_job': partner.sg_job,
				'sg_address': partner.sg_address,
				'sg_tel': partner.sg_tel,
				'sg_mob': partner.sg_mob,
				'sg_work_tel': partner.sg_work_tel,
				#enrollment data
				'applicant_date': partner.applicant_date,
				'registeration_date': partner.registeration_date,
				'registeration_type': partner.registeration_type,
				'grade_level': partner.grade_level,
				'student_grade': partner.student_grade,
				'join_bus': partner.join_bus,
				'bus_status': partner.bus_status,
				'bus_route': partner.bus_route,
				'enrollment_date': partner.enrollment_date,
				'id_code': partner.id_code,
				'left_date': partner.left_date,
				'prev_school': partner.prev_school,
				'reason_of_transfer': partner.reason_of_transfer,
				#health info
				'health_info': partner.health_info				
			}
		return {'value': values}


	def _create_lead_partner(self, cr, uid, lead, context=None):
		partner_id = lead.partner_id and lead.partner_id.id or False
		
		if(not partner_id):
			context['student'] = False
			context['parent'] = True
			partner_id = self._lead_create_contact(cr, uid, lead, lead.contact_name, False, context=context)
		
		context['student'] = True
		context['parent'] = False
		partner_id = self._lead_create_contact(cr, uid, lead, lead.partner_name, True ,partner_id,context=context)
		
		return partner_id

	def handle_partner_assignation(self, cr, uid, ids, action='create', partner_id=False, context=None):
		"""
		Handle partner assignation during a lead conversion.
		if action is 'create', create new partner with contact and assign lead to new partner_id.
		otherwise assign lead to the specified partner_id

		:param list ids: leads/opportunities ids to process
		:param string action: what has to be done regarding partners (create it, assign an existing one, or nothing)
		:param int partner_id: partner to assign if any
		:return dict: dictionary organized as followed: {lead_id: partner_assigned_id}
		"""
		#TODO this is a duplication of the handle_partner_assignation method of crm_phonecall
		partner_ids = {}
		for lead in self.browse(cr, uid, ids, context=context):
			# If the action is set to 'create' and no partner_id is set, create a new one
			# if lead.partner_id:
				# partner_ids[lead.id] = lead.partner_id.id
				# continue
			
			
			partner_id = self._create_lead_partner(cr, uid, lead, context)
			self.pool['res.partner'].write(cr, uid, partner_id, {'section_id': lead.section_id and lead.section_id.id or False})
			if partner_id:
				lead.write({'partner_id': partner_id})
			partner_ids[lead.id] = partner_id
		return partner_ids
	
	def send_mail_without_pop(self, cr, uid, ids, context=None):
		assert len(ids) == 1, 'This option should only be used for a single id at a time.'
		email_template_obj = self.pool.get('email.template')
		ir_model_data = self.pool.get('ir.model.data')
		try:
			template_id = ir_model_data.get_object_reference(cr, uid, 'school_admission', 'email_template_manarat_no_available_spot1')[1]
		except ValueError:
			template_id = False
		if template_id:
			email_template_obj.send_mail(cr,uid,template_id,ids[0],True)
			# values = email_template_obj.generate_email(cr, uid, int(template_id), ids, context=context)
			# values['subject'] = subject 
			# values['email_to'] = email_to
			# values['body_html'] = body_html
			# values['body'] = body_html
			# values['res_id'] = ids[0]
			# mail_mail_obj = self.pool.get('mail.mail')
			# msg_id = mail_mail_obj.create(cr, uid, values, context=context)
			# if msg_id:
					# mail_mail_obj.send(cr, uid, [msg_id], context=context) 
		return True
		
	def action_notification_send(self, cr, uid, ids, context=None):
		'''
		This function opens a window to compose an email, with the edi sale template message loaded by default
		'''
		assert len(ids) == 1, 'This option should only be used for a single id at a time.'
		ir_model_data = self.pool.get('ir.model.data')
		try:
			template_id = ir_model_data.get_object_reference(cr, uid, 'school_admission', 'email_template_manarat_no_available_spot1')[1]
		except ValueError:
			template_id = False
		try:
			compose_form_id = ir_model_data.get_object_reference(cr, uid, 'mail', 'email_compose_message_wizard_form')[1]
		except ValueError:
			compose_form_id = False 
		# parentId = self.browse(cr, uid, ids, context=context)[0].partner_id.parent_id.id
		ctx = dict()
		ctx.update({
			'default_model': 'crm.lead',
			'default_res_id': ids[0],
			'default_use_template': bool(template_id),
			'default_template_id': template_id,
			'default_composition_mode': 'comment',
			'mark_so_as_sent': True
		})
		
		return {
			'type': 'ir.actions.act_window',
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'mail.compose.message',
			'views': [(compose_form_id, 'form')],
			'view_id': compose_form_id,
			'target': 'new',
			'context': ctx,
		}
		
	def action_notification_send2(self, cr, uid, ids, context=None):
		'''
		This function opens a window to compose an email, with the edi sale template message loaded by default
		'''
		assert len(ids) == 1, 'This option should only be used for a single id at a time.'
		ir_model_data = self.pool.get('ir.model.data')
		try:
			template_id = ir_model_data.get_object_reference(cr, uid, 'school_admission', 'email_template_manarat_no_available_spot1')[1]
		except ValueError:
			template_id = False
		try:
			compose_form_id = ir_model_data.get_object_reference(cr, uid, 'mail', 'email_compose_message_wizard_form')[1]
		except ValueError:
			compose_form_id = False 
		# parentId = self.browse(cr, uid, ids, context=context)[0].partner_id.parent_id.id
		ctx = dict()
		ctx.update({
			'default_model': 'crm.lead',
			'default_res_id': ids[0],
			'default_use_template': bool(template_id),
			'default_template_id': template_id,
			'default_composition_mode': 'comment',
			'mark_so_as_sent': True
		})
		mail_model = self.pool.get('mail.compose.message')
		
		mail_obj_id = mail_model.create(cr, uid, ctx, context=context)
		#mail_obj = mail_model.search(cr, uid, [('id', '=',mail_obj_id)])[0]
		mail_model.send_mail(cr, uid, [mail_obj_id])
		return True
class res_partner(models.Model, AdmetionInfo):
	_inherit = 'res.partner'
	
	#is lead
	lead = fields.Boolean(String="Lead")
	parent = fields.Boolean(String="Parent")
	student = fields.Boolean(String="Student")
	documents = fields.One2many('manarat.document','partner_id_rel',string='Documents')
	
	
	# father info
	# father_full_name = fields.Char(string="Full Name")
	# father_nationality = fields.Many2one("res.country", string="Nationality")
	# father_religion =  fields.Selection(RELIGION, string="Religion")
	# father_acadimic = fields.Char(string="Academic Qualification")
	# father_mob_no = fields.Char(string="Mobile Number")
	# father_mob_no2 = fields.Char(string="Mobile Number 2")
	# father_home_address = fields.Char(string="Home Address")
	# father_home_tel = fields.Char(string="Home Telephone")
	# father_job = fields.Char(string="Job")
	# father_employer_address = fields.Char(string="Current Employer Address")
	# father_occupation_phone = fields.Char(string="Curent Occupation Phone")
	# father_status =  fields.Selection(LIVE_STATUS, string="Status")
	# father_id_type = fields.Selection(ID_TYPYE, string="ID Type")
	# father_id_no = fields.Char(string="ID Number")
	
	# education info
	# student_id = fields.Char(string="Student ID")
	# student_mother_tongue = fields.Selection(LANGUAGS, string="Mother Tongue")
	# student_first_foreign_language = fields.Selection(LANGUAGS, string="First Foregin Language")
	# student_second_foreign_language = fields.Selection(LANGUAGS, string="Second Foreign Language")
	
	# student personal info
	# student_first_name = fields.Char(string="First Name")
	# student_middle_name = fields.Char(string="Middle Name")
	# student_surname = fields.Char(string="Surname")
	# student_arabic_full_name = fields.Char(string="Arabic Full Name")
	# student_birth_date = fields.Date(string="Birth Date")
	# student_place_of_birth = fields.Char(string="Place Of Birth")
	# student_gender = fields.Selection(GENDER, string="Gender")
	# student_nationality = fields.Many2one("res.country", string="Nationality")
	# student_religion = fields.Selection(RELIGION, string="Religion")
	# student_national_id = fields.Char(string="National ID")
	# student_birth_certificate_no = fields.Char(string="Birth Certificate Number")
	# student_issue_date = fields.Date(string="Date Of Issue")
	
class Level(models.Model):
	_name = 'manarat.level'
	
	name = fields.Char(string='Level')
	available_spots = fields.Integer(string='Available spots')

DOC_STATUS = [('Waiting','Waiting'),('Received','Received'),('Not Received','Not Received')]

class Document(models.Model):
	_name = 'manarat.document'
	
	name = fields.Many2one('manarat.document.title',string='Document')
	date = fields.Date(string='Date')
	status = fields.Selection(DOC_STATUS, string='Status')
	
	lead_id_rel = fields.Many2one('crm.lead')
	partner_id_rel = fields.Many2one('res.partner')
	

	
class Document_Title(models.Model):
	_name = 'manarat.document.title'
	
	name = fields.Char(string='title')
